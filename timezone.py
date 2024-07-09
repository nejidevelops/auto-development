from datetime import datetime
import pytz

# List of time zones to check
time_zones = [
    'UTC',
    'America/New_York',
    'Europe/London',
    'Asia/Tokyo',
    'Australia/Sydney'
]

def get_current_time_in_timezones(time_zones):
    results = {}
    for zone in time_zones:
        # Get the timezone object
        timezone = pytz.timezone(zone)
        # Get the current time in the specified timezone
        current_time = datetime.now(timezone)
        # Format the time as a string
        formatted_time = current_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')
        results[zone] = formatted_time
    return results

def main():
    results = get_current_time_in_timezones(time_zones)
    for zone, time in results.items():
        print(f"The current time in {zone} is {time}")

if __name__ == "__main__":
    main()
