import pandas as pd 
from sqlalchemy import create_engine
from pathlib import  Path

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "sales.db"
engine = create_engine(f"sqlite:///{DB_PATH.as_posix()}")

def extract_sales_data():
    query = "SELECT * FROM train JOIN store ON train.Store = store.Store"
    df = pd.read_sql(query, engine)
    return df

df = extract_sales_data()
print(df.shape)
print(df.head())