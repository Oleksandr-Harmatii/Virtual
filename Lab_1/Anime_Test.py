from flask import Flask
import requests

app = Flask(__name__)

# URL API Jikan v4 для отримання епізодів аніме Hunter x Hunter (2011)
ANIME_ID = 11061  # ID Hunter x Hunter (2011)
API_URL = f"https://api.jikan.moe/v4/anime/{ANIME_ID}/episodes"

@app.route('/')
def home():
    response = requests.get(API_URL)  # Отримуємо дані від API
    data = response.json()  # Перетворюємо у формат JSON

    if "data" not in data:
        return "<p>Помилка: не вдалося отримати дані</p>"

    episodes_info = ""
    for episode in data["data"]:
        episodes_info += f"<p>Епізод {episode['mal_id']} - {episode['title']} (Оцінка: {episode.get('score', 'Немає оцінки')})</p>"

    return episodes_info

if __name__ == '__main__':
    app.run(debug=True)
