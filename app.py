from flask import Flask, request, send_file
from generate_pdf import SmartHRPDF
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "SmartHR PDF Generator is running!"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    pdf = SmartHRPDF()
    pdf.build(data)

    output_path = "generated_report.pdf"
    pdf.output(output_path)

    return send_file(output_path, as_attachment=True)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
