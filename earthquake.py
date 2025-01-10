import requests
import json

API_URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"

def fetch_earthquake_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from USGS API: {e}")
        return None

def extract_top_earthquakes(data, top_n=10):
    try:
        earthquakes = data['features']
        earthquake_details = [
            {
                "magnitude": feature['properties']['mag'],
                "location": feature['properties']['place'],
                "url": feature['properties']['url']
            }
            for feature in earthquakes
        ]
        earthquake_details.sort(key=lambda x: x['magnitude'], reverse=True)
        return earthquake_details[:top_n]
    except KeyError as e:
        print(f"Error processing data: Missing key {e}")
        return []

def display_earthquakes(earthquakes):
    if not earthquakes:
        print("No earthquake data available.")
        return
    
    print("Top 10 Strongest Earthquakes of the Week:")
    print("-" * 50)
    for i, quake in enumerate(earthquakes, start=1):
        print(f"{i}. Magnitude: {quake['magnitude']}")
        print(f"   Location: {quake['location']}")
        print(f"   More Info: {quake['url']}")
        print("-" * 50)

def main():
    print("Fetching earthquake data...")
    data = fetch_earthquake_data()
    if data:
        top_earthquakes = extract_top_earthquakes(data)
        display_earthquakes(top_earthquakes)

if __name__ == "__main__":
    main()
