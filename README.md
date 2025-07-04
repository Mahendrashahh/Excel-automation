

 # Excel Automation 

A modern Flask web app to automate Excel file processing. Users can upload multiple Excel files (with multiple sheets), select an operation (merge, clean, add total column, format), and download the processed result as a single Excel file.

## Features
- Upload multiple Excel files (with multiple sheets)
- Choose operation: Merge, Clean, Add Total Column, Format
- All sheets from all files are processed and merged
- Modern, responsive UI with loader, nav, and motivational footer
- Download result with operation-specific filename

## How to Run
1. Clone this repo:
   ```
   git clone https://github.com/Mahendrashahh/Excel-automation.git
   cd excel-automation
   ```
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the app:
   ```
   python app.py
   ```
4. Open your browser at [http://localhost:5000](http://localhost:5000)

## Folder Structure
- `app.py` - Main Flask app
- `processor.py` - Excel processing logic
- `templates/` - HTML templates
- `static/` - CSS and images
- `uploads/` - Uploaded files (ignored by git)
- `output/` - Processed output files (ignored by git)

## Author
Mahendra Shah

---
Enjoy automating your Excel workflows!

