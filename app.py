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

    name = random.choice(startup_names)
    idea = random.choice(startup_ideas)
    customer = random.choice(customers)
    revenue = random.choice(revenue_models)
    score = random.randint(60, 100)

    print("\n🚀 Startup Name:", name)
    print("💡 Startup Idea:", idea, "for", industry)
    print("🎯 Target Customers:", customer)
    print("💰 Revenue Model:", revenue)
    print("📈 Startup Score:", score, "/100")


industry = input("Enter an industry: ")
generate_startup(industry)
