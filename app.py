industry = input("Enter an industry: ")

print("\nStartup Ideas:\n")

if industry.lower() == "healthcare":
    print("- AI Doctor Assistant")
    print("- AI Medical Report Analyzer")
    print("- AI Patient Monitoring System")

elif industry.lower() == "education":
    print("- AI Homework Helper")
    print("- AI Study Planner")
    print("- AI Exam Preparation Coach")

else:
    print("- AI Assistant for", industry)
    print("- AI Analytics Platform for", industry)
    print("- AI Marketplace for", industry)