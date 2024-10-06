import fitz # PyMUPDF

# have to do bold and italics here i think
# they should be inserted with spaces before the content so that parse_txt can work accurately.

def convert_pdf_to_txt(pdf_file_path):
    # open pdf doc
    pdf_doc = fitz.open(pdf_file_path)

    # open a temp txt file to store the pdf's text
    with open("temp.txt", "w") as f:
        
        # page by page, add text from the pdf, separated by our 'newpage' escape
        for page in pdf_doc:
            f.write(page.get_text())


    print("done")
    pdf_doc.close()
