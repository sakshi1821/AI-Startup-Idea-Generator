from flask import Flask, render_template, request
import random
import json

app = Flask(__name__)

# Load data from JSON
with open("data.json", "r") as file:
    data = json.load(file)


def generate_startup(industry):
    return {
        "name": random.choice(data["startup_names"]),
        "idea": random.choice(data["startup_ideas"]),
        "customer": random.choice(data["customers"]),
        "revenue": random.choice(data["revenue_models"]),
        "score": random.randint(60, 100),
        "industry": industry
    }


@app.route("/", methods=["GET", "POST"])
def home():

    startup = None

    if request.method == "POST":
        industry = request.form["industry"]
        startup = generate_startup(industry)

    return render_template("index.html", startup=startup)


if __name__ == "__main__":
    app.run(debug=True)