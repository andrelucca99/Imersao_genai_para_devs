# Exercício

Crie um programa chamado weather.py que recebe como argumento de linha de
comando uma cidade e responde com a temperatura atual.

- Seu programa deverá fazer um request para o endpoint abaixo, de forma a obter a
latitude e longitude da cidade desejada.

  f"https://geocoding-api.open-meteo.com/v1/search?name={city}&count=1"

- Seu programa deverá fazer um request para o endpoint abaixo, para obter a temperatura local.

  f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m"

## Exemplo de saída esperada:

 python3 weather.py "Glasgow"

  - Current temperature in Glasgow, United Kingdom is 17.6 °C