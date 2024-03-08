class WeatherData:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

# 입력 처리
n = int(input())
weather_data_list = []
for _ in range(n):
    date, day, weather = input().split()
    weather_data_list.append(WeatherData(date, day, weather))

# 비가 오는 날 찾기
for data in weather_data_list:
    if data.weather == "Rain":
        print(data.date, data.day, data.weather)
        break