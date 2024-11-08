from fastapi import FastAPI
from random import randint, choice

app = FastAPI()

weather_conditions = ["Sunny", "Cloudy", "Rainy", "Stormy", "Snowy"]
forecasts_data = {}

def generate_forecast():
    forecast = []
    for day in range(1, 4):
        forecast.append({
            "day": f"Day {day}",
            "temperature_c": randint(-10, 35),
            "condition": choice(weather_conditions)
        })
    return forecast

@app.get("/forecast/{city_name}")
async def get_weather_forecast(city_name: str):
    if city_name not in forecasts_data:
        forecasts_data[city_name] = generate_forecast()

    forecast_data = forecasts_data[city_name]

    return {"city": city_name, "forecasts": forecast_data}

@app.get("/forecast/{city_name}/{day}")
async def get_specific_day_forecast(city_name: str, day: int):
    if day < 1 or day > 3:
        raise HTTPException(status_code=400, detail="Day must be within 1 to 3")

    if city_name not in forecasts_data:
        forecasts_data[city_name] = generate_forecast()

    forecast_data = forecasts_data[city_name]
    forecast = forecast_data[day - 1]

    return {"city": city_name, "forecast": forecast}