import pandas as pd
from datetime import time

df=pd.read_csv('data/Zomato Dataset.csv')

print(df.head())
print(df.isna().sum())
print(df.describe())
print(df.duplicated())
print(df[['Time_Orderd', 'Time_Order_picked']].sample(15))

#cleaning part
df=df.drop_duplicates()
df['Delivery_person_Age']=df['Delivery_person_Age'].fillna(df['Delivery_person_Age'].median())
df['Delivery_person_Ratings']=df['Delivery_person_Ratings'].fillna(df['Delivery_person_Ratings'].median())


def clean_time(value):
    if pd.isna(value):
        return pd.NA

    value = str(value).strip()

    try:
        numeric_value = float(value)

        if 0 <= numeric_value <= 1:
            total_minutes = round(numeric_value*24*60)

            hours=(total_minutes//60)%24
            minutes=total_minutes%60

            return f"{hours:02d}:{minutes:02d}"

    except ValueError:
        pass

    return value

df['Time_Orderd'] = df['Time_Orderd'].apply(clean_time)
df['Time_Order_picked'] = df['Time_Order_picked'].apply(clean_time)
df['Time_Orderd'] = df['Time_Orderd'].fillna('Unknown')

df['Weather_conditions']=df['Weather_conditions'].fillna('Unknown')
df['Road_traffic_density']=df['Road_traffic_density'].fillna('Unknown')

df['multiple_deliveries_missing'] = (
    df['multiple_deliveries'].isna().astype(int)
)

df['Festival']=df['Festival'].fillna('Unknown')
df['City']=df['City'].fillna('Unknown')

print(df.isna().sum())

df.to_csv('data/clean_zomato.csv')

