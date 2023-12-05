import requests
import json

def get_repository_info(username, repository_name):
    url = f"https://api.github.com/repos/{username}/{repository_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        repository_info = response.json()
        return repository_info
    else:
        print(f"Ошибка при получении данных: {response.status_code}")
        return None

username = "Automattic"
repository_name = "wp-calypso"

repository_info = get_repository_info(username, repository_name)

if repository_info:
    with open("TOP 9.Json", "w", encoding="utf-8") as file:
        json.dump(repository_info, file, indent=4, ensure_ascii=False)
        print("Информация о репозитории сохранена в файле 'TOP 9.Json'")
