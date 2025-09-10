# -*- coding: utf-8 -*-

from aws_redshift_schema_explorer.explore import (
    ListColumnsCommand,
)

from text2sqlpoc.one.api import one
from rich import print as rprint


cmd = ListColumnsCommand(
    redshift_data_api_client=one.bsm.redshiftdataapiservice_client,
    database=one.env.redshift_serverless_database_name,
    workgroup_name=one.env.redshift_serverless_workgroup_name,
    max_rows=1_000_000,
)
columns = cmd.exec()
rprint(columns)
print(f"n_columns = {len(columns)}")
