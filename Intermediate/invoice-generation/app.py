import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("intermediate/invoice-generation/invoices/*.xlsx")

for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1") #read
    
    pdf = FPDF(orientation="P", unit="mm", format="A4") # create
    pdf.add_page()
    
    filename = Path(filepath).stem # Get filename
    invoice_nr, date = filename.split("-") # Get invoice
    
    pdf.set_font(family="Times", size=16, style="B") 
    pdf.cell(w=50, h=8, txt=f"Invoice nr.{invoice_nr}", ln=1) 
    
    pdf.set_font(family="Times", size=16, style="B") 
    pdf.cell(w=50, h=8, txt=f"Date:{date}") # create cell

    pdf.output(f"intermediate/invoice-generation/PDFs/{filename}.pdf")
