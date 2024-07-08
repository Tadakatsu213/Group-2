import matplotlib.pyplot as plt

# Convert ISO_START_DATE to datetime format
data['ISO_START_DATE'] = pd.to_datetime(data['ISO_START_DATE'])

# Group by date and sum the cases to get the total daily cases across all countries
daily_cases = data.groupby('ISO_START_DATE')['DAILY_CASES'].sum().reset_index()

# Plot the trend of daily cases over time
plt.figure(figsize=(12, 6))
plt.plot(daily_cases['ISO_START_DATE'], daily_cases['DAILY_CASES'], label='Daily Cases')
plt.title('Daily COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.legend()
plt.grid(True)
plt.show()
