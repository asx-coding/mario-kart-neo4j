import os
from neo4j_runway import IngestionGenerator, DataModel


def generate_pyingest_config(data_model_file_path: str) -> None:
    dm = DataModel.from_arrows(data_model_file_path)
    gen = IngestionGenerator(
        data_model=dm,
        username=os.environ.get("NEO4J_USERNAME"),
        password=os.environ.get("NEO4J_PASSWORD"),
        uri=os.environ.get("NEO4J_URI"),
        database="neo4j",
        csv_dir="data/supabase/",
    )
    gen.generate_pyingest_yaml_file(
        file_name="pyingest_config", post_ingest_code="./ingest/post_ingest.cypher"
    )
    return gen.generate_pyingest_yaml_string(
        post_ingest_code="./ingest/post_ingest.cypher"
    )
