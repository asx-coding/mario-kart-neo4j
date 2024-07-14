import os
from neo4j import GraphDatabase


def reset_neo4j_database() -> None:

    driver = GraphDatabase.driver(
        uri=os.environ.get("NEO4J_URI"),
        auth=(os.environ.get("NEO4J_USERNAME"), os.environ.get("NEO4J_PASSWORD")),
    )
    with driver.session() as session:
        session.run(
            """
MATCH (n) DETACH DELETE n
"""
        )
        session.run(
            """
CALL apoc.schema.assert({},{},true) YIELD label, key RETURN *  
"""
        )
