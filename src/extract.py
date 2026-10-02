import pandas as pd 
from sqlalchemy import create_engine
from pathlib import  Path

ROOT = Path(__file__).resolve().parent.parent
DB_PATH = ROOT / "sales.db"
engine = create_engine(f"sqlite:///{DB_PATH.as_posix()}")

def extract_sales_data():
    query = """SELECT 
    train.store,
    train.DayOfWeek,
    train.Date,
    train.Sales,
    train.Customers,
    train.Open,
    train.Promo,
    train.StateHoliday,
    train.SchoolHoliday,
    store.StoreType,
    store.Assortment,
    store.CompetitionDistance,
    store.CompetitionOpenSinceMonth,
    store.CompetitionOpenSinceYear,
    store.Promo2,
    store.Promo2SinceWeek,
    store.Promo2SinceYear,
    store.PromoInterval 
    FROM train 
    JOIN store ON train.Store = store.Store 
    """
    df = pd.read_sql(query, engine)
    return df

df = extract_sales_data()
print(df.shape)
print(df.head())