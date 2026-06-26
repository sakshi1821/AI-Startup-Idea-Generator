import random

industry = input("Enter an industry: ")

ideas = [
    "AI Assistant",
    "AI Analytics Platform",
    "AI Marketplace",
    "AI Automation Tool",
    "AI Recommendation System",
    "AI Chatbot",
    "AI Hiring Platform",
    "AI Productivity Tool"
]

startup = random.choice(ideas)

print("\n🚀 Your AI Startup Idea:")
print(startup, "for", industry)