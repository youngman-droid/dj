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


class NodeRevisionBase(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A base node revision.
    """


    class MetaOapg:
        required = {
            "name",
            "type",
        }
        
        class properties:
            name = schemas.StrSchema
        
            @staticmethod
            def type() -> typing.Type['NodeType']:
                return NodeType
            display_name = schemas.StrSchema
            description = schemas.StrSchema
            query = schemas.StrSchema
            
            
            class mode(
                schemas.ComposedSchema,
            ):
            
            
                class MetaOapg:
                    
                    @classmethod
                    @functools.lru_cache()
                    def all_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            NodeMode,
                        ]
            
            
                def __new__(
                    cls,
                    *_args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'mode':
                    return super().__new__(
                        cls,
                        *_args,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "name": name,
                "type": type,
                "display_name": display_name,
                "description": description,
                "query": query,
                "mode": mode,
            }
    
    name: MetaOapg.properties.name
    type: 'NodeType'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'NodeType': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["display_name"]) -> MetaOapg.properties.display_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["query"]) -> MetaOapg.properties.query: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mode"]) -> MetaOapg.properties.mode: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "type", "display_name", "description", "query", "mode", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'NodeType': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["display_name"]) -> typing.Union[MetaOapg.properties.display_name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["query"]) -> typing.Union[MetaOapg.properties.query, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mode"]) -> typing.Union[MetaOapg.properties.mode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "type", "display_name", "description", "query", "mode", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        type: 'NodeType',
        display_name: typing.Union[MetaOapg.properties.display_name, str, schemas.Unset] = schemas.unset,
        description: typing.Union[MetaOapg.properties.description, str, schemas.Unset] = schemas.unset,
        query: typing.Union[MetaOapg.properties.query, str, schemas.Unset] = schemas.unset,
        mode: typing.Union[MetaOapg.properties.mode, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'NodeRevisionBase':
        return super().__new__(
            cls,
            *_args,
            name=name,
            type=type,
            display_name=display_name,
            description=description,
            query=query,
            mode=mode,
            _configuration=_configuration,
            **kwargs,
        )

from djclient.model.node_mode import NodeMode
from djclient.model.node_type import NodeType
