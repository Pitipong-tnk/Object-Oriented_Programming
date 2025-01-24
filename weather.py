import requests

api_key = '80ab7943c5d2c9e5857c492f2dd6bc5f'
city = 'bangkok'
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
url_jason = 'https://api.openweathermap.org/data/2.5/weather?q=bangkok&appid=80ab7943c5d2c9e5857c492f2dd6bc5f'

result = requests.get(url).json()

city = result['name']
country = result['sys']['country']
weather = result['weather'][0]['main']
descripttion = result['weather'][0]['description']
temp = result['main']['temp'] - 273.15

print(f'เมือง {city} ประเทศ {country}')
print(f'สภาพอากาศวันนี้ {weather} มีลักษณะ {descripttion}')
print(f'อุณหภูมิตอนนี้ {temp:.2f} C ')