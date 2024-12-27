# Завдання 1/2: Виконання GET-запиту
# import requests

# site = "https://jsonplaceholder.typicode.com"

# responce = requests.get(url=site)
# print(responce.text)

# Завдання 3/4: Параметри запиту

# import requests

# site = "https://jsonplaceholder.typicode.com/posts/"

# change = {
#     "username": "Ullya",
#     "password": "qwerty"
# }
# try:
#     recponce = requests.post(site, data = change)
#     for header in recponce.headers.items():
#         print(f"Header: {header}")

#     with open("responce_content.txt", "w", encoding="utf-8") as file:
#         file.write(recponce.text)

#     print(recponce.text)
#     print(recponce.status_code)
# except requests.exceptions.RequestException as e:
#     print(f"Error {e}")


















