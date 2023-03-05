# coding: utf-8

"""
    DJ server

    A DataJunction metrics layer  # noqa: E501

    The version of the OpenAPI document: 0.0.post1.dev1+gd8cb070
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


class CreateNode(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Create non-source node object.
    """


    class MetaOapg:
        required = {
            "mode",
            "name",
            "description",
            "type",
        }
        
        class properties:
            description = schemas.StrSchema
        
            @staticmethod
            def mode() -> typing.Type['NodeMode']:
                return NodeMode
            name = schemas.StrSchema
        
            @staticmethod
            def type() -> typing.Type['NodeType']:
                return NodeType
            display_name = schemas.StrSchema
            query = schemas.StrSchema
            __annotations__ = {
                "description": description,
                "mode": mode,
                "name": name,
                "type": type,
                "display_name": display_name,
                "query": query,
            }
    
    mode: 'NodeMode'
    name: MetaOapg.properties.name
    description: MetaOapg.properties.description
    type: 'NodeType'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mode"]) -> 'NodeMode': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'NodeType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["display_name"]) -> MetaOapg.properties.display_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["query"]) -> MetaOapg.properties.query: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["description", "mode", "name", "type", "display_name", "query", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mode"]) -> 'NodeMode': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'NodeType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["display_name"]) -> typing.Union[MetaOapg.properties.display_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["query"]) -> typing.Union[MetaOapg.properties.query, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["description", "mode", "name", "type", "display_name", "query", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        mode: 'NodeMode',
        name: typing.Union[MetaOapg.properties.name, str, ],
        description: typing.Union[MetaOapg.properties.description, str, ],
        type: 'NodeType',
        display_name: typing.Union[MetaOapg.properties.display_name, str, schemas.Unset] = schemas.unset,
        query: typing.Union[MetaOapg.properties.query, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreateNode':
        return super().__new__(
            cls,
            *_args,
            mode=mode,
            name=name,
            description=description,
            type=type,
            display_name=display_name,
            query=query,
            _configuration=_configuration,
            **kwargs,
        )

from djclient.model.node_mode import NodeMode
from djclient.model.node_type import NodeType
