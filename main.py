from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    Y_a = int(20)
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L",
             ln=1)
    pdf.line(10, Y_a, 200, Y_a)

    for m in range(23):
        pdf.line(10, Y_a, 200, Y_a)
        Y_a = Y_a + 12
    pdf.ln(263)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(w=0, h=8, txt=row["Topic"], align="R",
             ln=1)

    for i in range(int(row["Pages"]) - 1):
        Y_a = int(20)
        pdf.add_page()

        for m in range(23):
            pdf.line(10, Y_a, 200, Y_a)
            Y_a = Y_a + 12

        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(0, 0, 0)
        pdf.cell(w=0, h=8, txt=row["Topic"], align="R",
                 ln=1)


pdf.output("output.pdf")
