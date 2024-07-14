from database.neo4j import load, reset_neo4j_database

if __name__ == "__main__":
    reset_neo4j_database()
    load(pyingest_config_file_path="./pyingest_config.yml")
