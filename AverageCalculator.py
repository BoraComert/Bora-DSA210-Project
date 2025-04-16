import pandas as pd

def process_all_months_total_precipitation(file_path):
    """
    Reads a full-year weather CSV file and computes monthly total precipitation data for 2020.
    
    Parameters:
    - file_path: str, path to the CSV file
    
    Returns:
    - DataFrame with monthly total precipitation, temperature, humidity, and wind speed
    """
    # Read the CSV
    df = pd.read_csv(file_path, parse_dates=['Date'])

    # Ensure only data from 2020 is included
    df = df[df['Date'].dt.year == 2019]

    # Create Year-Month column for grouping
    df['Year-Month'] = df['Date'].dt.to_period('M')

    # Group and compute totals for precipitation and averages for others
    monthly_totals = df.groupby('Year-Month').agg({
        'Avg Temperature (C)': 'mean',
        'Avg Humidity (%)': 'mean',
        'Avg Wind Speed (km/h)': 'mean',
        'Total Precipitation (mm)': 'sum'  # Sum the precipitation for the whole month
    }).reset_index()

    # Rename for clarity
    monthly_totals.columns = [
        'Date',
        'Avg Temperature (C)',
        'Avg Humidity (%)',
        'Avg Wind Speed (km/h)',
        'Total Precipitation (mm)'
    ]

    return monthly_totals

# Example usage
file_path = 'Istanbul_daily_weather_2019-01-01.csv'  # Make sure this matches your actual file
summary = process_all_months_total_precipitation(file_path)
print(summary)

# Optional: Save to CSV
summary.to_csv("monthly_totals_2019.csv", index=False)
