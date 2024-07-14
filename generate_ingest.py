from ingest import generate_pyingest_config

if __name__ == "__main__":
    print(
        generate_pyingest_config(
            data_model_file_path="data_model/mario-kart-graph-model-v1.json"
        )
    )
