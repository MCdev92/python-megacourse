from fpdf import FPDF
import glob
from pathlib import Path

# Create a list of text filepaths
filepaths = glob.glob("intermediate/txt-to-pdf/files/*.txt")
# Create one PDF file
pdf = FPDF(orientation="P", unit="mm", format="A4")

# Go through each text file
for filepath in filepaths:
    pdf.add_page() # Add a page to PDF doc for each txt file
    filename = Path(filepath).stem # Get the filename without ext
    name = filename.title() # convert to title case (i.e: Cat)
    
    # Add name to PDF
    pdf.set_font(family="Times", style="B", size=24)
    pdf.cell(w=50, h=8, txt=name, ln=1) 
    
# produce the PDF in desire Dir
pdf.output(f"intermediate/txt-to-pdf/PDFs/output.pdf")
    