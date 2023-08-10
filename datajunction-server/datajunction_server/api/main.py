"""
Main DJ server app.
"""

# All the models need to be imported here so that SQLModel can define their
# relationships at runtime without causing circular imports.
# See https://sqlmodel.tiangolo.com/tutorial/code-structure/#make-circular-imports-work.
# pylint: disable=unused-import,ungrouped-imports

import logging
from logging import config
from os import path
from typing import TYPE_CHECKING

from fastapi import Depends, FastAPI, Request
from fastapi.responses import JSONResponse, RedirectResponse, Response
from jose import JWTError
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from sqlmodel import select
from starlette.middleware.cors import CORSMiddleware

from datajunction_server import __version__
from datajunction_server.api import (
    attributes,
    catalogs,
    client,
    cubes,
    data,
    dimensions,
    djsql,
    engines,
    health,
    history,
    materializations,
    metrics,
    namespaces,
    nodes,
    sql,
    tags,
)
from datajunction_server.api.attributes import default_attribute_types
from datajunction_server.errors import DJError, DJException
from datajunction_server.internal.authentication.basic import parse_basic_auth_cookie
from datajunction_server.internal.authentication.github import parse_github_auth_cookie
from datajunction_server.models.catalog import Catalog
from datajunction_server.models.column import Column
from datajunction_server.models.engine import Engine
from datajunction_server.models.node import NodeRevision
from datajunction_server.models.table import Table
from datajunction_server.models.user import User
from datajunction_server.utils import get_settings

if TYPE_CHECKING:  # pragma: no cover
    from opentelemetry import trace

_logger = logging.getLogger(__name__)
settings = get_settings()

UNAUTHENTICATED_ENDPOINTS = [
    "/docs",
    "/openapi.json",
    "/basic/user/",
    "/basic/login/",
    "/github/login/",
    "/github/token/",
]
BASIC_OAUTH_CONFIGURED = settings.secret or False


config.fileConfig(
    path.join(path.dirname(path.abspath(__file__)), "logging.conf"),
    disable_existing_loggers=False,
)

dependencies = [Depends(default_attribute_types)]

# Only inject basic auth middleware if a server secret is configured
if settings.secret:  # pragma: no cover
    dependencies.append(Depends(parse_basic_auth_cookie))
if all(
    [
        settings.secret,
        settings.github_oauth_client_id,
        settings.github_oauth_client_secret,
    ],
):  # pragma: no cover
    dependencies.append(Depends(parse_github_auth_cookie))

app = FastAPI(
    title=settings.name,
    description=settings.description,
    version=__version__,
    license_info={
        "name": "MIT License",
        "url": "https://mit-license.org/",
    },
    dependencies=dependencies,
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origin_whitelist,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(catalogs.router)
app.include_router(engines.router)
app.include_router(metrics.router)
app.include_router(djsql.router)
app.include_router(nodes.router)
app.include_router(namespaces.router)
app.include_router(materializations.router)
app.include_router(data.router)
app.include_router(health.router)
app.include_router(history.router)
app.include_router(cubes.router)
app.include_router(tags.router)
app.include_router(attributes.router)
app.include_router(sql.router)
app.include_router(client.router)
app.include_router(dimensions.router)


@app.exception_handler(DJException)
async def dj_exception_handler(  # pylint: disable=unused-argument
    request: Request,
    exc: DJException,
) -> JSONResponse:
    """
    Capture errors and return JSON.
    """
    _logger.exception(exc)
    return JSONResponse(
        status_code=exc.http_status_code,
        content=exc.to_dict(),
        headers={"X-DJ-Error": "true", "X-DBAPI-Exception": exc.dbapi_exception},
    )


# Only mount basic auth router if a server secret is configured
if settings.secret:  # pragma: no cover
    from datajunction_server.api.authentication import basic

    app.include_router(basic.router)

# Only mount github auth router if a github client id and secret are configured
if all(
    [
        settings.secret,
        settings.github_oauth_client_id,
        settings.github_oauth_client_secret,
    ],
):  # pragma: no cover
    from datajunction_server.api.authentication import github

    app.include_router(github.router)
