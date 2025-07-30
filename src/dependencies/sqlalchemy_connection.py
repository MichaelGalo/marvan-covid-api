import os
from sqlalchemy import create_engine


def sqlalchemy_engine():
    account = os.getenv("SNOWFLAKE_ACCOUNT")
    user = os.getenv("SNOWFLAKE_USER")
    password = os.getenv("SNOWFLAKE_PASSWORD")
    database = os.getenv("SNOWFLAKE_DATABASE")
    schema = os.getenv("SNOWFLAKE_SCHEMA_SILVER")
    warehouse = os.getenv("SNOWFLAKE_WAREHOUSE")
    role = os.getenv("SNOWFLAKE_ROLE")

    engine = create_engine(
        f"snowflake://{user}:{password}@{account}/{database}/{schema}?warehouse={warehouse}&role={role}"
    )

    return engine
