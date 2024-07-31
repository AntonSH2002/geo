from geopy.geocoders import Nominatim

# Инициализация геокодера
geolocator = Nominatim(user_agent="GetLoc")

# Местоположение для поиска
location_name = "Алтайский край, Барнаул, улица Короленко, 8"

# Получение местоположения
location = geolocator.geocode(location_name)

# Вывод координат
if location:
    print(f"Координаты {location_name}: Широта {location.latitude}, Долгота {location.longitude}")
else:
    print("Местоположение не найдено.")
