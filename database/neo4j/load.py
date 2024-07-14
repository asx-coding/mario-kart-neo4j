from neo4j_runway import PyIngest


def load(pyingest_config_file_path: str) -> None:
    PyIngest(config=pyingest_config_file_path)
