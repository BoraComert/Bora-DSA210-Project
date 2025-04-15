import requests
import pandas as pd
from datetime import datetime, timedelta

API_KEY = "1a265a09184c43d18b2174304251203"
CITY = "Istanbul"
DAYS_TO_FETCH = 2
START_DATE = "2021-12-30"
BASE_URL = "https://api.worldweatheronline.com/premium/v1/past-weather.ashx"

current_date = datetime.strptime(START_DATE, "%Y-%m-%d")
all_weather_data = []

# Loop through DAYS_TO_FETCH and fetch daily average data
for _ in range(DAYS_TO_FETCH):
    date_str = current_date.strftime("%Y-%m-%d")
    print(f"Fetching data for {date_str}...")

    params = {
        "key": API_KEY,
        "q": CITY,
        "date": date_str,
        "format": "json",
        "tp": 24  # Fetch daily averages (one entry per day)
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        weather = data["data"]["weather"][0]
        
        # Extract daily averages and total precipitation
        avg_temp = weather["avgtempC"]  # Daily average temperature
        condition = weather["hourly"][0]["weatherDesc"][0]["value"]  # Most representative weather condition
        avg_humidity = weather["hourly"][0]["humidity"]  # Daily average humidity
        avg_wind_speed = weather["hourly"][0]["windspeedKmph"]  # Daily average wind speed
        total_precip = weather["hourly"][0]["precipMM"]  # Total precipitation in mm

        all_weather_data.append([date_str, avg_temp, condition, avg_humidity, avg_wind_speed, total_precip])
        print(f"Saved data for {date_str}.")
    else:
        print(f"Error fetching data for {date_str}: {response.status_code}")
        break  # Stop if API fails

    current_date += timedelta(days=1)

# Convert the collected data into a pandas DataFrame
df = pd.DataFrame(all_weather_data, columns=[
    "Date", "Avg Temperature (C)", "Condition", "Avg Humidity (%)", "Avg Wind Speed (km/h)", "Total Precipitation (mm)"
])

# Save the weather data to a CSV file
csv_filename = f"{CITY}_daily_weather_{START_DATE}.csv"
df.to_csv(csv_filename, index=False, encoding="utf-8")

print(f"Weather data saved to {csv_filename}")
