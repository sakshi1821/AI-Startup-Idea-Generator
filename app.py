from flask import Flask, render_template, request, session, send_file
import random
import json
import io
import os
from datetime import datetime

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    HRFlowable,
    Image
)

app = Flask(__name__)
app.secret_key = "startup_secret"

# -----------------------------
# Load Startup Data
# -----------------------------
with open("data.json", "r", encoding="utf-8") as file:
    data = json.load(file)


# -----------------------------
# Generate Startup
# -----------------------------
def generate_startup(industry):

    startup = random.choice(data).copy()

    startup["industry"] = industry
    startup["category"] = startup["idea"]

    return startup


# -----------------------------
# Home Page
# -----------------------------
@app.route("/", methods=["GET", "POST"])
def home():

    startup = None
    error = None

    stats = {
        "total": len(data),
        "favorites": len(session.get("favorites", [])),
        "searches": len(session.get("history", [])),
        "average": round(
            sum(item["score"] for item in data) / len(data)
        )
    }

    if request.method == "POST":

        industry = request.form.get("industry", "").strip().title()
        favorite = request.form.get("favorite")
        if industry:

            # Generate Startup
            startup = generate_startup(industry)

            session["last_startup"] = startup

            # -----------------------------
            # Search History
            # -----------------------------
            history = session.get("history", [])

            if industry in history:
                history.remove(industry)

            history.insert(0, industry)

            session["history"] = history[:5]

            # -----------------------------
            # Favorites
            # -----------------------------
            if favorite:

                favorites = session.get("favorites", [])

                if favorite not in favorites:
                    favorites.append(favorite)

                session["favorites"] = favorites

        else:
            error = "Please enter an industry."

    return render_template(
        "index.html",
        startup=startup,
        error=error,
        history=session.get("history", []),
        favorites=session.get("favorites", []),
        stats=stats
    )


# -----------------------------
# Download PDF
# -----------------------------
# -----------------------------
# Download PDF
# -----------------------------
@app.route("/download_pdf")
def download_pdf():

    startup = session.get("last_startup")

    if not startup:
        return "No startup generated yet!"

    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer)

    styles = getSampleStyleSheet()

    story = []

    # --------------------------------
    # Logo
    # --------------------------------
    logo_path = os.path.join(
        app.root_path,
        "static",
        "images",
        "logo.png"
    )

    if os.path.exists(logo_path):

        logo = Image(logo_path)
        logo.drawWidth = 70
        logo.drawHeight = 70

        story.append(logo)

    story.append(Spacer(1, 12))

    # --------------------------------
    # Title
    # --------------------------------
    story.append(
        Paragraph(
            "<font size='22'><b>AI Startup Report</b></font>",
            styles["Title"]
        )
    )

    story.append(Spacer(1, 10))

    current_date = datetime.now().strftime("%d %B %Y")
    current_time = datetime.now().strftime("%I:%M %p")

    story.append(
        Paragraph(
            f"<b>Date:</b> {current_date}",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            f"<b>Time:</b> {current_time}",
            styles["Normal"]
        )
    )

    story.append(Spacer(1, 10))

    story.append(HRFlowable(width="100%"))

    story.append(Spacer(1, 15))

    # --------------------------------
    # Startup Information
    # --------------------------------
    story.append(
        Paragraph(
            "<font size='16'><b>Startup Information</b></font>",
            styles["Heading2"]
        )
    )

    story.append(Spacer(1, 10))

    fields = [
        ("Name", startup["name"]),
        ("Idea", startup["idea"]),
        ("Industry", startup["industry"]),
        ("Customers", startup["customer"]),
        ("Revenue", startup["revenue"]),
        ("Location", startup["location"]),
        ("Funding", startup["funding"]),
        ("Founder", startup["founder"]),
        ("Age", startup["age"]),
        ("Success Rate", f"{startup['success']}%"),
        ("Score", f"{startup['score']}/100")
    ]

    for label, value in fields:

        story.append(
            Paragraph(
                f"<b>{label}:</b> {value}",
                styles["Normal"]
            )
        )

        story.append(Spacer(1, 4))

    story.append(Spacer(1, 15))

    story.append(HRFlowable(width="100%"))

    story.append(Spacer(1, 10))

    story.append(
        Paragraph(
            "<i>Generated by AI Startup Idea Generator</i>",
            styles["Italic"]
        )
    )
    doc.build(story)

    buffer.seek(0)

    print("PDF Built Successfully")

    return send_file(
    buffer,
    as_attachment=True,
    download_name="AI_Startup_Report.pdf",
    mimetype="application/pdf"
)
if __name__ == "__main__":
    app.run(debug=True)
