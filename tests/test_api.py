# -*- coding: utf-8 -*-

from aws_redshift_schema_explorer import api


def test():
    _ = api
    _ = api.SVV_REDSHIFT_DATABASES_DATABASE_TYPE_ENUM
    _ = api.SVV_ALL_SCHEMAS_SCHEMA_TYPE_ENUM
    _ = api.SVV_ALL_TABLES_TABLE_TYPE_ENUM
    _ = api.SVV_TABLES_TABLE_TYPE_ENUM
    _ = api.SVV_EXTERNAL_TABLES_TABLE_TYPE_ENUM
    _ = api.SVV_TABLE_INFO_DISTSTYLE_ENUM
    _ = api.SVV_ALL_COLUMNS_DATA_TYPE_ENUM
    _ = api.PG_CLASS_REL_KIND_ENUM
    _ = api.Database
    _ = api.Schema
    _ = api.Table
    _ = api.View
    _ = api.Column
    _ = api.ListDatabaseCommand
    _ = api.ListSchemaCommand
    _ = api.ListTableCommand
    _ = api.ListColumnsCommand


if __name__ == "__main__":
    from aws_redshift_scehema_explorer.tests import run_cov_test

    run_cov_test(
        __file__,
        "aws_redshift_schema_explorer.api",
        preview=False,
    )
