from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("intermediate/pdf-template/topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L",
             ln=1)
    # commented out clear pages with no lines
    # pdf.line(10, 21, 200, 21) 
    
    for y in range(20, 298, 10): # add lines to your pages
        pdf.line(10, y, 200, y)
    
    
    # Set the footer master
    pdf.ln(265)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
    
    for i in range(row["Pages"] - 1):
        pdf.add_page()
            
        # Set the footer
        pdf.ln(275)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180,180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
        
        for y in range(20, 298, 10): # add lines to your pages
            pdf.line(10, y, 200, y)
        
pdf.output("output.pdf")