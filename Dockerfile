FROM apache/airflow:3.1.8

USER airflow

RUN pip install --no-cache-dir \
    "dbt-core==1.10.*" \
    "dbt-postgres==1.10.*" \
    duckdb \
    psycopg2-binary \
    requests \
    python-dotenv