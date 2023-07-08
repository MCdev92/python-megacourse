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
    
    # Get the content of each text file
    with open(filepath, "r") as file:
        content = file.read()
    # Add the text file content to the PDF
    pdf.set_font(family="Times", size=12)
    pdf.multi_cell(w=0, h=6, txt=content)
    
    # Add Footer Signature
    pdf.footer()
    pdf.cell(w=0, h=10, txt="Mcdev92", align="R") 
    
# produce the PDF in desire Dir
pdf.output(f"intermediate/txt-to-pdf/PDFs/output.pdf")
    