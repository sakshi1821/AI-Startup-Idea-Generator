import random

def generate_startup(industry):
    startup_names = [
        "SmartSync",
        "AINova",
        "FutureMind",
        "NextGen AI",
        "VisionTech"
    ]

    startup_ideas = [
        "AI Assistant",
        "AI Analytics Platform",
        "AI Marketplace",
        "AI Automation Tool",
        "AI Recommendation System"
    ]

    customers = [
        "Students",
        "Hospitals",
        "Businesses",
        "Teachers",
        "Freelancers"
    ]

    revenue_models = [
        "Subscription",
        "Pay-per-use",
        "Freemium",
        "Advertisement",
        "Enterprise Licensing"
    ]

    startup = {
        "name": random.choice(startup_names),
        "idea": random.choice(startup_ideas),
        "customer": random.choice(customers),
        "revenue": random.choice(revenue_models),
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