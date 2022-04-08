"""
Utility functions.
"""

import logging
import os
from functools import lru_cache
from pathlib import Path
from typing import Iterator, Optional

from dotenv import load_dotenv
from rich.logging import RichHandler
from sqlalchemy.engine import Engine
from sqlmodel import Session, SQLModel, create_engine

from datajunction.config import Settings
from datajunction.typing import ColumnType

DJ_DATABASE_ID = 0


def setup_logging(loglevel: str) -> None:
    """
    Setup basic logging.
    """
    level = getattr(logging, loglevel.upper(), None)
    if not isinstance(level, int):
        raise ValueError(f"Invalid log level: {loglevel}")

    logformat = "[%(asctime)s] %(levelname)s: %(name)s: %(message)s"
    logging.basicConfig(
        level=level,
        format=logformat,
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True)],
        force=True,
    )


def get_project_repository() -> Path:
    """
    Return the project repository.

    This is used for unit tests.
    """
    return Path(__file__).parent.parent.parent


@lru_cache
def get_settings() -> Settings:
    """
    Return a cached settings object.
    """
    load_dotenv()
    return Settings()


def get_engine() -> Engine:
    """
    Create the metadata engine.
    """
    settings = get_settings()
    connect_args = {"check_same_thread": False}
    engine = create_engine(settings.index, echo=False, connect_args=connect_args)

    return engine


def create_db_and_tables() -> None:
    """
    Create the database and tables.
    """
    engine = get_engine()
    SQLModel.metadata.create_all(engine)


def get_session() -> Iterator[Session]:
    """
    Per-request session.
    """
    engine = get_engine()

    with Session(engine, autoflush=False) as session:
        yield session


def get_name_from_path(repository: Path, path: Path) -> str:
    """
    Compute the name of a node given its path and the repository path.
    """
    # strip anything before the repository
    relative_path = path.relative_to(repository)

    if len(relative_path.parts) < 2 or relative_path.parts[0] not in {
        "nodes",
        "databases",
    }:
        raise Exception(f"Invalid path: {path}")

    # remove the "nodes" directory from the path
    relative_path = relative_path.relative_to(relative_path.parts[0])

    # remove extension
    relative_path = relative_path.with_suffix("")

    # encode percent symbols and periods
    encoded = (
        str(relative_path)
        .replace("%", "%25")
        .replace(".", "%2E")
        .replace(os.path.sep, ".")
    )

    return encoded


def get_more_specific_type(
    current_type: Optional[ColumnType],
    new_type: ColumnType,
) -> ColumnType:
    """
    Given two types, return the most specific one.

    Different databases might store the same column as different types. For example, Hive
    might store timestamps as strings, while Postgres would store the same data as a
    datetime.

        >>> get_more_specific_type(ColumnType.STR, ColumnType.DATETIME)
        <ColumnType.DATETIME: 'DATETIME'>
        >>> get_more_specific_type(ColumnType.STR, ColumnType.INT)
        <ColumnType.INT: 'INT'>

    """
    if current_type is None:
        return new_type

    hierarchy = [
        ColumnType.BYTES,
        ColumnType.STR,
        ColumnType.FLOAT,
        ColumnType.INT,
        ColumnType.DECIMAL,
        ColumnType.BOOL,
        ColumnType.DATETIME,
        ColumnType.DATE,
        ColumnType.TIME,
        ColumnType.TIMEDELTA,
        ColumnType.LIST,
        ColumnType.DICT,
    ]

    return sorted([current_type, new_type], key=hierarchy.index)[1]
