import pandas as pd 
from sqlalchemy import create_engine
from pathlib import  Path

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "sales.db"
CSV_PATH = ROOT / "data" / "mobile_sales_data.csv"



engine = create_engine(f"sqlite:///{DB_PATH.as_posix()}")

df = pd.read_csv(CSV_PATH)

df.to_sql("sales", engine,if_exists="replace" , index=False)

print(f'loaded rows into sales: {len(df)}')