import pandas as pd 
from sqlalchemy import create_engine
from pathlib import  Path

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "sales.db"
TRAIN_PATH = ROOT / "data" / "train.csv"
STORE_PATH = ROOT / "data" / "store.csv"

engine = create_engine(f"sqlite:///{DB_PATH.as_posix()}")

def load_sales_data(csv_path , table_name):
   df = pd.read_csv(csv_path)
   df.to_sql(table_name, engine,if_exists="replace" , index=False)
   print(f"{table_name} : {len(df)} rows")

load_sales_data(TRAIN_PATH , "train")
load_sales_data(STORE_PATH , "store")