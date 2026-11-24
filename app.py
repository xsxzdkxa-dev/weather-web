from weather_service import get_weather
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"],)
def index():
    weather = None
    error = None
    if request.method == "POST":
        city = request.form.get("city", "").strip()
        if not city:
            error = "Не вдалося знайти погоду"
        else:
            weather = get_weather(city)

    return render_template("index.html", weather=weather, error=error)

if __name__ == "__main__":
    app.run(debug=True)