from pathlib import Path
import pandas as pd

from tools.env_vars import GDRIVE_PROJECT_ROOT
from tools.database import Database


if __name__ == "__main__":

    db = Database()

    tables = [x[0] for x in db.tables()]

    data_folder = Path(GDRIVE_PROJECT_ROOT) / "data"

    csvs_to_import = data_folder.rglob("*.csv")

    for filepath in csvs_to_import:

        sql_tablename = filepath.stem.lower()

        if f"raw.{sql_tablename}" not in tables:

            df = pd.read_csv(filepath)

            print("Importing", sql_tablename)

            db.import_dataframe(df, sql_tablename)

        else:
            print(sql_tablename, "already exists. Skipping.")
