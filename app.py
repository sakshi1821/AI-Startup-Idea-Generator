import random
import json

# Load data from JSON file
with open("data.json", "r") as file:
    data = json.load(file)


def generate_startup(industry):
    startup = {
        "name": random.choice(data["startup_names"]),
        "idea": random.choice(data["startup_ideas"]),
        "customer": random.choice(data["customers"]),
        "revenue": random.choice(data["revenue_models"]),
        "score": random.randint(60, 100)
    }

    return startup


industry = input("Enter an industry: ")

print("\n🚀 AI Startup Ideas\n")

for i in range(5):
    startup = generate_startup(industry)

    print(f"Startup {i+1}")
    print("Name:", startup["name"])
    print("Idea:", startup["idea"], "for", industry)
    print("Customers:", startup["customer"])
    print("Revenue:", startup["revenue"])
    print("Score:", startup["score"])
    print("-" * 40)