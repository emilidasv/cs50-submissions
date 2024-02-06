from fpdf import FPDF


nameofstudent = input("Name:")
textonpdf = nameofstudent + " took CS50"
print(textonpdf)



pdf = FPDF(orientation="portrait", format="A4")

pdf.add_page()

# Add the image
pdf.image("shirtificate.png", x=0, y=0)


pdf.set_font('helvetica', size=30)
pdf.set_text_color(r=255, g=255, b=255)
#add the text
pdf.cell(w=0, h=200 , text = nameofstudent + " took CS50" , align= "C")



pdf.output("shirtificate.pdf")



#pdf.output("pdf-with-image.pdf")
