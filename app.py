from flask import Flask, render_template, request, send_file
from utils.ai_generator import generate_content
from database import init_db, save_history, get_history
from reportlab.pdfgen import canvas
import io

app = Flask(__name__)

# Initialize database
init_db()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    try:
        description = request.form.get("description")
        platform = request.form.get("platform")
        tone = request.form.get("tone")

        captions, hashtags, ctas = generate_content(
            description,
            platform,
            tone
        )

        # Save to database
        save_history(
            description,
            platform,
            tone,
            captions,
            hashtags,
            ctas
        )

        return render_template(
            "index.html",
            captions=captions,
            hashtags=hashtags,
            ctas=ctas,
            description=description,
            platform=platform,
            tone=tone
        )

    except Exception as e:
        return render_template(
            "index.html",
            error=str(e)
        )


@app.route("/history")
def history():
    rows = get_history()
    return render_template(
        "history.html",
        rows=rows
    )


@app.route("/download/txt")
def download_txt():
    rows = get_history()

    text = ""

    for row in rows:
        text += f"Description: {row[1]}\n"
        text += f"Platform: {row[2]}\n"
        text += f"Tone: {row[3]}\n"
        text += f"Captions:\n{row[4]}\n"
        text += f"Hashtags:\n{row[5]}\n"
        text += f"CTAs:\n{row[6]}\n"
        text += "-" * 60 + "\n\n"

    buffer = io.BytesIO()
    buffer.write(text.encode("utf-8"))
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="caption_history.txt",
        mimetype="text/plain"
    )


@app.route("/download/pdf")
def download_pdf():
    rows = get_history()

    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer)

    y = 800

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(200, y, "CaptionAI History")
    y -= 40

    pdf.setFont("Helvetica", 10)

    for row in rows:

        pdf.drawString(40, y, f"Description: {row[1]}")
        y -= 20

        pdf.drawString(40, y, f"Platform: {row[2]}")
        y -= 20

        pdf.drawString(40, y, f"Tone: {row[3]}")
        y -= 20

        pdf.drawString(40, y, f"Captions: {row[4][:80]}")
        y -= 20

        pdf.drawString(40, y, f"Hashtags: {row[5][:80]}")
        y -= 20

        pdf.drawString(40, y, f"CTAs: {row[6][:80]}")
        y -= 40

        if y < 100:
            pdf.showPage()
            pdf.setFont("Helvetica", 10)
            y = 800

    pdf.save()
    buffer.seek(0)

    return send_file(
        buffer,
        as_attachment=True,
        download_name="caption_history.pdf",
        mimetype="application/pdf"
    )


if __name__ == "__main__":
    init_db()  # Ensure the database is initialized before running the app
    app.run(debug=True)