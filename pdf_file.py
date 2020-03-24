from reportlab.pdfgen import canvas

def create_pdf():
    c = canvas.Canvas("hellopdf.pdf")
    c.drawString(n, n , "hello world")
    ## add more information on system statistics 
    now = datetime.datetime.today()
    date_as_string = typecast_as_string(now)
    
    textObject.textLines("Disk Capacity Report: %s" % date_as_string)    

    c.drawText(textObject)
    c.showPage()
    c.save()


create_pdf()



