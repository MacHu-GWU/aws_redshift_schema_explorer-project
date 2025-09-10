# -*- coding: utf-8 -*-

from aws_redshift_schema_explorer.explore import (
    ListDatabaseCommand,
)

from text2sqlpoc.one.api import one
from rich import print as rprint


cmd = ListDatabaseCommand(
    redshift_data_api_client=one.bsm.redshiftdataapiservice_client,
    database=one.env.redshift_serverless_database_name,
    workgroup_name=one.env.redshift_serverless_workgroup_name,
)
databases = cmd.exec()
rprint(databases)
print(f"n_databases = {len(databases)}")
