# coding: utf-8

"""
    DJ server

    A DataJunction metrics repository  # noqa: E501

    The version of the OpenAPI document: 0.0.post1.dev1+g9c5d385
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from djclient import schemas  # noqa: F401


class NodeValidation(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A validation of a provided node definition
    """


    class MetaOapg:
        required = {
            "node",
            "node_revision",
            "columns",
            "message",
            "dependencies",
            "status",
        }
        
        class properties:
            message = schemas.StrSchema
        
            @staticmethod
            def status() -> typing.Type['NodeStatus']:
                return NodeStatus
        
            @staticmethod
            def node() -> typing.Type['Node']:
                return Node
        
            @staticmethod
            def node_revision() -> typing.Type['NodeRevision']:
                return NodeRevision
            
            
            class dependencies(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['NodeRevisionOutput']:
                        return NodeRevisionOutput
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['NodeRevisionOutput'], typing.List['NodeRevisionOutput']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'dependencies':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'NodeRevisionOutput':
                    return super().__getitem__(i)
            
            
            class columns(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['Column']:
                        return Column
            
                def __new__(
                    cls,
                    _arg: typing.Union[typing.Tuple['Column'], typing.List['Column']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'columns':
                    return super().__new__(
                        cls,
                        _arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'Column':
                    return super().__getitem__(i)
            __annotations__ = {
                "message": message,
                "status": status,
                "node": node,
                "node_revision": node_revision,
                "dependencies": dependencies,
                "columns": columns,
            }
    
    node: 'Node'
    node_revision: 'NodeRevision'
    columns: MetaOapg.properties.columns
    message: MetaOapg.properties.message
    dependencies: MetaOapg.properties.dependencies
    status: 'NodeStatus'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'NodeStatus': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["node"]) -> 'Node': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["node_revision"]) -> 'NodeRevision': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dependencies"]) -> MetaOapg.properties.dependencies: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["columns"]) -> MetaOapg.properties.columns: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["message", "status", "node", "node_revision", "dependencies", "columns", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["message"]) -> MetaOapg.properties.message: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> 'NodeStatus': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["node"]) -> 'Node': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["node_revision"]) -> 'NodeRevision': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dependencies"]) -> MetaOapg.properties.dependencies: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["columns"]) -> MetaOapg.properties.columns: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["message", "status", "node", "node_revision", "dependencies", "columns", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        node: 'Node',
        node_revision: 'NodeRevision',
        columns: typing.Union[MetaOapg.properties.columns, list, tuple, ],
        message: typing.Union[MetaOapg.properties.message, str, ],
        dependencies: typing.Union[MetaOapg.properties.dependencies, list, tuple, ],
        status: 'NodeStatus',
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NodeValidation':
        return super().__new__(
            cls,
            *_args,
            node=node,
            node_revision=node_revision,
            columns=columns,
            message=message,
            dependencies=dependencies,
            status=status,
            _configuration=_configuration,
            **kwargs,
        )

from djclient.model.column import Column
from djclient.model.node import Node
from djclient.model.node_revision import NodeRevision
from djclient.model.node_revision_output import NodeRevisionOutput
from djclient.model.node_status import NodeStatus
