from fastapi import FastAPI
from random import randint, choice

app = FastAPI()

# Sample weather conditions for simulation
weather_conditions = ["Sunny", "Cloudy", "Rainy", "Stormy", "Snowy"]

@app.get("/forecast/{city_name}")
async def get_weather_forecast(city_name: str):
    """Get a 3-day weather forecast for a specific city."""
    ...

    return {"city": city_name, "forecasts": forecast_data}

@app.get("/forecast/{city_name}/{day}")
async def get_specific_day_forecast(city_name: str, day: int):
    """Get the forecast for a specific day in the 3-day range."""
    ...

    return {"city": city_name, "forecast": forecast}