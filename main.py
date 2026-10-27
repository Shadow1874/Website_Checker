import requests
from requests.exceptions import RequestException
from urllib.parse import urlparse


while True:
    address = input("\nВведите URL (или exit для выхода): ").strip()

    if address.lower() == "exit":
        print("Программа завершена.")
        break

    if not address:
        print("Введите адрес сайта.")
        continue

    if not urlparse(address).scheme:
        address = "https://" + address

    try:
        response = requests.get(address, timeout=10)

        elapsed_ms = round(response.elapsed.total_seconds() * 1000)

        print(f"\nURL: {address}")
        print(f"HTTP-статус: {response.status_code}")
        print(f"Время ответа: {elapsed_ms} мс")

        if 200 <= response.status_code < 400:
            print("Сайт доступен.")
        else:
            print("Сервер ответил, но запрос завершился с ошибкой.")

    except RequestException as e:
        print(f"Не удалось выполнить запрос: {e}")