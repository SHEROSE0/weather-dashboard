import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.form.get("city")
        api_key = "5c890ea3ebae95aae12a1b05f7c8d5b5"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)
        if response.status_code == 200:
            weather_data = response.json()
        else:
            error = "City not found. Please try again!"

    return render_template("index.html", weather=weather_data, error=error)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)