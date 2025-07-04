from flask import Flask, render_template, request, redirect, send_file
from processor import process_excel
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def get_output_filename(operation):
    return f"{OUTPUT_FOLDER}/output_{operation}.xlsx"

@app.route("/")
def home():
    return render_template("index.html")  # Simple upload form

@app.route("/upload", methods=["POST"])
def upload():
    files = request.files.getlist("excel_files[]")
    operation = request.form.get("operation")
    file_paths = []

    if not files or all(file.filename == '' for file in files):
        return render_template("index.html", error="No files selected.")

    try:
        for file in files:
            if not file or not file.filename:
                continue
            filename = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filename)
            file_paths.append(filename)

        if not file_paths:
            return render_template("index.html", error="No valid files uploaded.")

        output_file = get_output_filename(operation)
        process_excel(file_paths, output_file=output_file, operation=operation)

        # Check if output file was created
        if not os.path.exists(output_file):
            return render_template("index.html", error="Processing failed: Output file not created.")
    except Exception as e:
        return render_template("index.html", error=f"Processing failed: {e}")

    return render_template("download.html", output_file=output_file, operation=operation)

@app.route("/download")
def download():
    operation = request.args.get("operation", "merge")
    output_file = get_output_filename(operation)
    if not os.path.exists(output_file):
        return "Output file not found. Please process files first.", 404
    # Set download filename to include operation
    download_name = f"result_{operation}.xlsx"
    return send_file(output_file, as_attachment=True, download_name=download_name)

if __name__ == "__main__":
    app.run(debug=True)
