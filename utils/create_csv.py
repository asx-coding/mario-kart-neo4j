from typing import Any, Dict

import pandas as pd


def convert_to_csv(name: str, table: Dict[str, Any]) -> None:
    pd.DataFrame(table).to_csv(f"data/supabase/{name}.csv")


def create_race_mod_csv() -> pd.DataFrame:
    race = pd.read_csv(
        "data/supabase/race.csv",
        usecols=[
            "race_id",
            "grand_prix_id",
            "course_id",
            "engine_class_id",
            "create_date",
            "username_id",
        ],
    )
    engine_class = pd.read_csv("data/supabase/engine_class.csv", index_col=0)
    grand_prix = pd.read_csv("data/supabase/grand_prix.csv", index_col=0)

    engine_class.rename(columns={"name": "engine_class"})

    race_mod = race.merge(engine_class, on="engine_class_id")
    race_mod = race_mod.merge(grand_prix, on="grand_prix_id")
    race_mod["freeplay"] = race_mod.apply(
        lambda row: True if row["grand_prix_id"] in ["0", "1"] else False, axis=1
    )

    race_mod.to_csv("data/supabase/race_mod.csv")
    return race_mod


def create_player_to_race_player_csv() -> pd.DataFrame:
    player = pd.read_csv("data/supabase/player_roster.csv", index_col=0)
    race_player = pd.read_csv(
        "data/supabase/race_player.csv", usecols=["race_player_id", "player_id"]
    )

    player_to_race_player = player.merge(race_player, on="player_id")

    player_to_race_player.to_csv("data/supabase/player_to_race_player.csv")
    return player_to_race_player
