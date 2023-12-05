import tkinter as tk
import requests
import json

def get_repository_info():
    repo_name = entry.get()
    url = f"https://api.github.com/repos/{repo_name}"
    response = requests.get(url)
    
    if response.status_code == 200:
        repository_info = response.json()
        filtered_info = {
            'company': repository_info['owner'].get('company', None),
            'created_at': repository_info.get('created_at', None),
            'email': repository_info['owner'].get('email', None),
            'id': repository_info['owner'].get('id', None),
            'name': repository_info['owner'].get('login', None),
            'url': repository_info['owner'].get('url', None)
        }
        with open("TOP 9 READY.Json", "w", encoding="utf-8") as file:
            json.dump(filtered_info, file, indent=4, ensure_ascii=False)
            status_label.config(text="Информация сохранена в файле 'TOP 9 READY.Json'")
    else:
        status_label.config(text=f"Ошибка: {response.status_code}")

root = tk.Tk()
root.title("Получение информации о репозитории")

label = tk.Label(root, text="Введите имя репозитория:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Получить информацию", command=get_repository_info)
button.pack()

status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()

