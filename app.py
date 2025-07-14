from flask import Flask, request, send_file
from generate_pdf import SmartHRPDF
import io
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

    # Output to memory (not file system)
    pdf_output = io.BytesIO()
    pdf.output(pdf_output)
    pdf_output.seek(0)

    return send_file(
        pdf_output,
        mimetype='application/pdf',
        as_attachment=True,
        download_name='salary_report.pdf'
    ), 200, {
        'Content-Type': 'application/pdf',
        'Content-Disposition': 'attachment; filename="salary_report.pdf"'
    }

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

