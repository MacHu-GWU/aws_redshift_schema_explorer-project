# -*- coding: utf-8 -*-

if __name__ == "__main__":
    from aws_redshift_schema_explorer.tests import run_cov_test

    run_cov_test(
        __file__,
        "aws_redshift_schema_explorer",
        is_folder=True,
        preview=False,
    )
