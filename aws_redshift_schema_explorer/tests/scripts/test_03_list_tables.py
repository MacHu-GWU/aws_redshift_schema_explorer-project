# -*- coding: utf-8 -*-

from aws_redshift_schema_explorer.explore import (
    ListTableCommand,
)

from text2sqlpoc.one.api import one
from rich import print as rprint


cmd = ListTableCommand(
    redshift_data_api_client=one.bsm.redshiftdataapiservice_client,
    database=one.env.redshift_serverless_database_name,
    workgroup_name=one.env.redshift_serverless_workgroup_name,
)
tables, views = cmd.exec()
rprint(tables)
rprint(views)
print(f"n_tables = {len(tables)}")
print(f"n_views = {len(views)}")
