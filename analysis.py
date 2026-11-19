import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('data/clean_zomato.csv')


total_order=len(df)
average_deliver_time=df['Time_taken (min)'].mean()
median_delivery_time=df['Time_taken (min)'].median()
min_deliver_time=df['Time_taken (min)'].min()
max_deliver_time=df['Time_taken (min)'].max()
p90_delivery_time = df['Time_taken (min)'].quantile(0.90)
standard_devition=df['Time_taken (min)'].std()
delivery_time = df['Time_taken (min)'].dropna()



bins = [0, 15, 20, 30, 40, float('inf')]

labels = [
    '10-15 min',
    '15-20 min',
    '20-30 min',
    '30-40 min',
    'Above 40 min'
]

delivery_categories = pd.cut(
    delivery_time,
    bins=bins,
    labels=labels,
    right=True
)



# plt.figure(figsize=(10,5))
# plt.hist(delivery_time,bins=20,edgecolor='black')

# plt.title('Distribution of Delivery Time')
# plt.xlabel('Delivery Time (minutes)')
# plt.ylabel('Number of Orders')

# plt.grid(axis='y', alpha=0.3)
# plt.show()

# plt.figure(figsize=(8, 4))

# plt.boxplot(delivery_time, vert=False)

# plt.title('Delivery Time Box Plot')
# plt.xlabel('Delivery Time (minutes)')

# plt.show()

percentage = (
    (df['Time_taken (min)'] > 30).mean() * 100
)

#print(f"Orders taking more than 30 minutes: {percentage:.2f}%")
# t=df.groupby('Road_traffic_density')['Time_taken (min)'].mean()
# print(t)
# print(df['Road_traffic_density'].value_counts())

df['is_delayed'] = df['Time_taken (min)'] > 30
# t=df.groupby('Road_traffic_density')['is_delayed'].mean() * 100
# print(t)

#role of weather
weather_analysis = df.groupby('Weather_conditions')['Time_taken (min)'].agg(
    ['count', 'mean', 'median']
).sort_values(by='mean', ascending=False)



weather_delay = (
    df.groupby('Weather_conditions')['is_delayed']
    .mean()
    .mul(100)
    .sort_values(ascending=False)
)



# print(pd.crosstab(
#     df['Weather_conditions'],
#     df['Road_traffic_density'],
#     normalize='index'
# ).round(3) * 100)

weather_traffic = df.pivot_table(
    index='Weather_conditions',
    columns='Road_traffic_density',
    values='Time_taken (min)',
    aggfunc='mean'
)

# print(weather_traffic.round(2))


# Highest average delivery time
# print(weather_traffic.stack().idxmax())
# print(weather_traffic.stack().max())

# # Lowest average delivery time
# print(weather_traffic.stack().idxmin())
# print(weather_traffic.stack().min())


partner_orders = (
    df.groupby('Delivery_person_ID')
      .size()
      .reset_index(name='total_orders')
)


partner_performance = (
    df.groupby('Delivery_person_ID')
      .agg(
          total_orders=('ID', 'count'),
          avg_delivery_time=('Time_taken (min)', 'mean'),
          median_delivery_time=('Time_taken (min)', 'median'),
          avg_rating=('Delivery_person_Ratings', 'mean')
      )
      .reset_index()
)


reliable_partners = partner_performance[
    partner_performance['total_orders'] >= 20
].copy()

# print(reliable_partners.shape[0])

# print(reliable_partners.nsmallest(
#     5, 'avg_delivery_time'
# ))

# print(reliable_partners.nlargest(
#     5, 'avg_delivery_time'
# ))

reliable_partners[
    ['avg_delivery_time', 'avg_rating']
].corr()

reliable_partners[
    'avg_delivery_time'
].corr(
    reliable_partners['avg_rating']
)

vehicle_performance = (
    df.groupby('Vehicle_condition')
      .agg(
          total_orders=('ID', 'count'),
          avg_delivery_time=('Time_taken (min)', 'mean'),
          median_delivery_time=('Time_taken (min)', 'median'),
          avg_rating=('Delivery_person_Ratings', 'mean')
      )
      .reset_index()
)


df['is_delayed'] = (
    df['Time_taken (min)'] > 30
).astype(int)

df.groupby('Vehicle_condition').agg(
    total_orders=('ID', 'count'),
    delayed_orders=('is_delayed', 'sum'),
    delay_rate=('is_delayed', 'mean')
)


vehicle_type_performance = (
    df.groupby('Type_of_vehicle')
      .agg(
          total_orders=('ID', 'count'),
          avg_delivery_time=('Time_taken (min)', 'mean'),
          median_delivery_time=('Time_taken (min)', 'median'),
          avg_rating=('Delivery_person_Ratings', 'mean')
      )
      .reset_index()
)



th=df.groupby('Type_of_vehicle').agg(
    total_orders=('ID', 'count'),
    delayed_orders=('is_delayed', 'sum'),
    delay_rate=('is_delayed', 'mean')
)


condition_traffic = (
    df.groupby(
        ['Vehicle_condition', 'Road_traffic_density']
    )
    .agg(
        total_orders=('ID', 'count'),
        avg_delivery_time=('Time_taken (min)', 'mean'),
        delay_rate=('is_delayed', 'mean')
    )
    .reset_index()
)

condition_traffic


condition_traffic.pivot(
    index='Vehicle_condition',
    columns='Road_traffic_density',
    values='delay_rate'
).round(3) * 100


vehicle_condition_type = (
    df.groupby(
        ['Type_of_vehicle', 'Vehicle_condition']
    )
    .agg(
        total_orders=('ID', 'count'),
        avg_delivery_time=('Time_taken (min)', 'mean'),
        delay_rate=('is_delayed', 'mean')
    )
    .reset_index()
)

vehicle_condition_type


vehicle_condition_type.pivot(
    index='Type_of_vehicle',
    columns='Vehicle_condition',
    values='delay_rate'
).round(3).mul(100)


df['age_group'] = pd.cut(
    df['Delivery_person_Age'],
    bins=[0, 20, 30, 40, 50, 100],
    labels=[
        'Under 20',
        '20-30',
        '30-40',
        '40-50',
        'Above 50'
    ]
)

age_performance = (
    df.groupby('age_group', observed=True)
      .agg(
          total_orders=('ID', 'count'),
          avg_delivery_time=('Time_taken (min)', 'mean'),
          median_delivery_time=('Time_taken (min)', 'median'),
          avg_rating=('Delivery_person_Ratings', 'mean'),
          delay_rate=('is_delayed', 'mean')
      )
      .reset_index()
)


df[
    df['Delivery_person_Ratings'] > 5
][
    ['Delivery_person_Age', 'Delivery_person_Ratings']
].head(10)


df['Delivery_person_Ratings'].value_counts().sort_index()

df[df['Delivery_person_Ratings'] > 5].groupby(
    'Delivery_person_Age'
).agg(
    count=('ID', 'count'),
    avg_delivery_time=('Time_taken (min)', 'mean')
)


df['rating_invalid'] = (
    (df['Delivery_person_Ratings'] < 1) |
    (df['Delivery_person_Ratings'] > 5)
).astype(int)

valid_ratings = df[
    df['Delivery_person_Ratings'].between(1, 5)
]


age_traffic = (
    df.groupby(
        ['age_group', 'Road_traffic_density'],
        observed=True
    )
    .agg(
        total_orders=('ID', 'count'),
        avg_delivery_time=('Time_taken (min)', 'mean'),
        delay_rate=('is_delayed', 'mean')
    )
    .reset_index()
)


age_traffic.pivot(
    index='age_group',
    columns='Road_traffic_density',
    values='delay_rate'
).round(3).mul(100)

age_city = (
    df.groupby(['age_group', 'City'], observed=True)
      .agg(
          total_orders=('ID', 'count'),
          avg_delivery_time=('Time_taken (min)', 'mean'),
          delay_rate=('is_delayed', 'mean')
      )
      .reset_index()
)

age_city.sort_values(
    ['age_group', 'total_orders'],
    ascending=[True, False]
)

age_vehicle = (
    df.groupby(['age_group', 'Type_of_vehicle'], observed=True)
      .agg(
          total_orders=('ID', 'count'),
          avg_delivery_time=('Time_taken (min)', 'mean'),
          delay_rate=('is_delayed', 'mean')
      )
      .reset_index()
)

age_vehicle

jam_orders = df[df['Road_traffic_density'] == 'Jam']

print("Total Jam orders:", len(jam_orders))
print("Delayed Jam orders:", jam_orders['is_delayed'].sum())
print("Jam delay rate:", jam_orders['is_delayed'].mean() * 100)

current_delayed = jam_orders['is_delayed'].sum()
target_delay_rate = 0.45
target_delayed = len(jam_orders) * target_delay_rate
potential_reduction = current_delayed - target_delayed
print("Potential delayed orders avoided:", potential_reduction)

jam_city = (
    df[df['Road_traffic_density'] == 'Jam']
    .groupby('City')
    .agg(
        total_orders=('ID', 'count'),
        delayed_orders=('is_delayed', 'sum'),
        delay_rate=('is_delayed', 'mean'),
        avg_delivery_time=('Time_taken (min)', 'mean')
    )
    .reset_index()
)

jam_city['delay_rate'] *= 100

print(jam_city.sort_values('delayed_orders', ascending=False))

metro_jam = df[
    (df['City'] == 'Metropolitian') &
    (df['Road_traffic_density'] == 'Jam')
].copy()

metro_jam['order_hour'] = pd.to_datetime(
    metro_jam['Time_Orderd'],
    format='%H:%M',
    errors='coerce'
).dt.hour

metro_hourly = (
    metro_jam.groupby('order_hour')
    .agg(
        total_orders=('ID', 'count'),
        delayed_orders=('is_delayed', 'sum'),
        delay_rate=('is_delayed', 'mean'),
        avg_delivery_time=('Time_taken (min)', 'mean')
    )
    .reset_index()
)

metro_hourly['delay_rate'] *= 100

evening_orders = metro_jam[
    metro_jam['order_hour'].between(19, 21)
]

current_delayed = evening_orders['is_delayed'].sum()

target_rate = 0.48

target_delayed = len(evening_orders) * target_rate

potential_reduction = current_delayed - target_delayed

print("Evening orders:", len(evening_orders))
print("Current delayed orders:", current_delayed)
print("Potential reduction:", potential_reduction)