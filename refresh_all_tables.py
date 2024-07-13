from dotenv import load_dotenv

from database.retrieve_postgres import TABLES, fetch_table, convert_to_csv

load_dotenv()

if __name__ == "__main__":
    for i in range(len(TABLES)):
        print(f"Retrieving table: {TABLES[i]}")
        table = fetch_table(TABLES[i])
        convert_to_csv(name=TABLES[i], table=table)
