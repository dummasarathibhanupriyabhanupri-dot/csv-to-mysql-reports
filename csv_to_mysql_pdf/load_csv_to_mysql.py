import pandas as pd
from sqlalchemy import create_engine
from db_config import DB_USER, DB_PASSWORD, DB_HOST, DB_NAME

# CSV file path
csv_path = "data/appointments.csv"

# Read CSV
df = pd.read_csv(csv_path)

# MySQL connection
engine = create_engine(
    f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
)

# Load data into MySQL
df.to_sql("appointments", con=engine, if_exists="replace", index=False)

print("✅ CSV data loaded into MySQL successfully")
