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


class TranslatedSQL(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Class for SQL generated from a given metric.
    """


    class MetaOapg:
        required = {
            "database_id",
            "sql",
        }
        
        class properties:
            database_id = schemas.IntSchema
            sql = schemas.StrSchema
            __annotations__ = {
                "database_id": database_id,
                "sql": sql,
            }
    
    database_id: MetaOapg.properties.database_id
    sql: MetaOapg.properties.sql
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["database_id"]) -> MetaOapg.properties.database_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["sql"]) -> MetaOapg.properties.sql: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["database_id", "sql", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["database_id"]) -> MetaOapg.properties.database_id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["sql"]) -> MetaOapg.properties.sql: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["database_id", "sql", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *_args: typing.Union[dict, frozendict.frozendict, ],
        database_id: typing.Union[MetaOapg.properties.database_id, decimal.Decimal, int, ],
        sql: typing.Union[MetaOapg.properties.sql, str, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'TranslatedSQL':
        return super().__new__(
            cls,
            *_args,
            database_id=database_id,
            sql=sql,
            _configuration=_configuration,
            **kwargs,
        )
