import os
from typing import Any, Dict, List

import pandas as pd
from supabase import create_client, Client

TABLES: List[str] = [
    "character",
    "course",
    "cup",
    "engine_class",
    "game",
    "grand_prix",
    "player_roster",
    "race",
    "race_player",
    "rules",
    "system",
    "users",
]


def fetch_table(name: str) -> Dict[str, Any]:
    """Fetch the complete table from Supabase"""
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_API_KEY")
    print(url)
    supabase: Client = create_client(url, key)
    return supabase.table(name).select("*").execute().data


def convert_to_csv(name: str, table: Dict[str, Any]) -> None:
    pd.DataFrame(table).to_csv(f"data/supabase/{name}.csv")
