"""
GQL Node models and related APIs.
"""


from typing import TYPE_CHECKING, Annotated, List

import strawberry
from sqlmodel import select
from strawberry.types import Info

from datajunction.models.node import Node as _Node
from datajunction.models.node import NodeColumns as _NodeColumns
from datajunction.models.node import NodeRelationship as _NodeRelationship
from datajunction.models.node import NodeType as _NodeType


@strawberry.experimental.pydantic.type(model=_NodeRelationship, all_fields=True)
class NodeRelationship:
    """
    Join table for self-referential many-to-many relationships between nodes.
    """


@strawberry.experimental.pydantic.type(model=_NodeColumns, all_fields=True)
class NodeColumns:
    """
    Join table for node columns.
    """


NodeType = strawberry.enum(_NodeType)

if TYPE_CHECKING:
    from datajunction.api.graphql.table import Table
    from datajunction.api.graphql.column import Column


@strawberry.experimental.pydantic.type(
    model=_Node,
    fields=["id", "name", "description", "created_at", "updated_at", "query"],
)
class Node:  # type: ignore
    """
    A node.
    """

    type: NodeType
    tables: List[Annotated["Table", strawberry.lazy("datajunction.api.graphql.table")]]
    parents: List[Annotated["Node", strawberry.lazy("datajunction.api.graphql.node")]]
    children: List[Annotated["Node", strawberry.lazy("datajunction.api.graphql.node")]]
    columns: List[Annotated["Column", strawberry.lazy("datajunction.api.graphql.column")]]


def get_nodes(info: Info) -> List[Node]:
    """
    List the available nodes.
    """
    nodes = info.context["session"].exec(select(_Node)).all()
    return [Node.from_pydantic(node) for node in nodes]
