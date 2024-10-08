import fitz # PyMUPDF


# have to do bold and italics here i think
# they should be inserted with spaces before the content so that parse_txt can work accurately.

def get_font_style(flags):
    bold = flags & 2 != 0
    italics = flags & 1 != 0

    return 3 if bold and italics else 2 if bold else 1 if italics else 0



def parse_blocks(blocks):
    # TEXT STYLING I CARE ABOUT
    # 0 = NO STYLING
    # 1 = ITALICS
    # 2 = BOLD
    # 3 = BOLD AND ITALICS


    style = 0
    curr_text = ""

    for b in blocks:
        if "lines" in b:  # true when block contains text
            for line in b["lines"]:
                for span in line["spans"]: # dictates differences in style

                    text = span["text"]
                    font_flags = span["flags"] # indicate different stylings

                    style = get_font_style(font_flags)

                    print(text)
                    print(style)

                    curr_text += ("\\textbf{\\textit{" + text + "}}}") if style == 3 else ("\\textbf{" + text + "}") if style == 2 else ("\\textit{" + text + "}") if style == 1 else text
                    # print(curr_text)

    return curr_text





def convert_pdf_to_txt(pdf_file_path):
    # open pdf doc
    doc = fitz.open(pdf_file_path)

    # open a temp txt file to store the pdf's text
    with open("temp.txt", "w") as f:

        blocks = []
        
        # page by page, add text from the pdf, separated by our 'newpage' escape
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            blocks.append(page.get_text("dict")["blocks"]) # get text from page block-by-block -- but we want to do ALL the text together (pages don't matter unless we indicate in the text)

            print(f"added page {page_num}'s blocks to blocks")

        
        parsed = parse_blocks(blocks)

        for b in blocks:
            print(b)
            print("\n")


        f.write(parsed)


    print("done") # DEBUGGING
    doc.close()
