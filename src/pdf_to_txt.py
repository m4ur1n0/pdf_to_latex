import fitz # PyMUPDF
import re


# have to do bold and italics here i think
# they should be inserted with spaces before the content so that parse_txt can work accurately.

def get_font_style(flags, font_name):
    italics = flags & 1 == 1

    bold = True if 'bold' in font_name.lower() else False
    italics = True if 'italics' in font_name.lower() or 'italic' in font_name.lower() else italics


    return 3 if (bold and italics) else 2 if bold else 1 if italics else 0

def recognize_math(text):
    # recognize_match takes in text and returns a dict of text inside our {} escape chars, and the beginning and end indices of the match

    pattern = r"\{([^{}]*)\}"
    matches = re.finditer(pattern, text)
    match_dict = {}

    for match in matches: # for each of the specially formatted matches
        match_text = match.group(1)
        m_start = match.start() # the index of the {
        m_end = match.end() # the index AFTER the }
        match_dict[match_text] = (m_start, m_end)
    
    return match_dict


def parse_blocks(blocks):
    # TEXT STYLING I CARE ABOUT
    # 0 = NO STYLING
    # 1 = ITALICS
    # 2 = BOLD
    # 3 = BOLD AND ITALICS

    # MY STYLING CRITERIA
    # 10000000 = PROBLEM
    # 01000000 = SOLUTION
    # 00100000 = SHADED
    # 00010000 = CENTERED
    # 00001000 = MATH
    # 00000100 = BOLD
    # 00000010 = ITALICS
    # 00000001 = TBD
    # THIS WAY WE CAN BITMASK WITH MAX EFFICIENCY


    style = 0


    curr_text = ""

    for i, b in enumerate(blocks):
        if "lines" in b:  # true when block contains text
            for line in b["lines"]:        

                # I don't see how to avoid O(2n) here....
                full_line_text = ''.join(s['text'] for s in line['spans'])
                print(f"LINE : {full_line_text}")

                for span in line["spans"]: # dictates differences in style
                    pass

                curr_text += full_line_text


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
            blocks = blocks + page.get_text("dict")["blocks"] # get text from page block-by-block -- but we want to do ALL the text together (pages don't matter unless we indicate in the text)

            print(f"added page {page_num}'s blocks to blocks")

        
        parsed = parse_blocks(blocks)

        # for b in blocks:
        #     print(b)
        #     print("\n")


        f.write(parsed)


    print("done") # DEBUGGING
    doc.close()
