import sys
import requests

def main():
    if len(sys.argv) != 2:
      print("Erro: deve fornecer exatamente um argumento.")
    elif not sys.argv[1]:
      print("Erro: insira o nome da cidade entre aspas, exemplo: 'São Paulo'")
    else:
      city_name = sys.argv[1]

    # Busca cidade
    url_city = f"https://geocoding-api.open-meteo.com/v1/search?name={city_name}&count=1"
    res = requests.get(url_city)
    data = res.json()['results'][0]

    lat = data['latitude']
    lon = data['longitude']
    country = data['country']

    # Busca previsão do tempo
    forecast_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    res_forecast = requests.get(forecast_url)
    forecast_data = res_forecast.json()

    current_temp = forecast_data['current_weather']['temperature']
    print(f"Current temperature in {city_name}, {country}: {current_temp}°C")

if __name__ == "__main__":
    main()
