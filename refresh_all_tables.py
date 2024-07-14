from dotenv import load_dotenv

from database.supabase import TABLES, fetch_table
from utils import (
    convert_to_csv,
    create_race_mod_csv,
    create_player_to_race_player_csv,
)

load_dotenv()

if __name__ == "__main__":
    for i in range(len(TABLES)):
        print(f"Retrieving table: {TABLES[i]}")
        table = fetch_table(TABLES[i])
        convert_to_csv(name=TABLES[i], table=table)
    create_race_mod_csv()
    create_player_to_race_player_csv()
