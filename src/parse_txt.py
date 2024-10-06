
# create a set of stand ins to optimize the 'in' operation
stand_ins = {'ENTAILS','>>','->','BICONDITIONS','<>','<->','EQUIV','==','NOT','!','~','AND','&&','^','||','XOR','FOREACH','FORALL','EXISTS','EXISTS!','DOMAIN','DD','PROVES','TURNSTILE','|-','TTPROVES','DTURNSTILE','|=','THEREFORE','BECAUSE','DEFINED'}
# latex_code = ['\\rightarrow','\\rightarrow','\\rightarrow','\\leftrightarrow','\\leftrightarrow','\\leftrightarrow','\\equiv','\\equiv','\\neg','\\neg','\\neg','\\land','\\land','\\land','\\lor','\\oplus','\\forall','\\forall','\\mathbb{d}','\\mathbb{d}','\\vdash','\\vdash','\\vdash','\\vDash','\\vDash','\\vDash','\\therefore','\\because','\\:=']
symbol_dict = {'ENTAILS':'\\rightarrow','>>':'\\rightarrow','->':'\\rightarrow','BICONDITIONS':'\\leftrightarrow','<>':'\\leftrightarrow','<->':'\\leftrightarrow','EQUIV':'\\equiv','==':'\\equiv','NOT':'\\neg','!':'\\neg','~':'\\neg','AND':'\\land','&&':'\\land','^':'\\land','||':'\\lor','XOR':'\\oplus','FOREACH':'\\forall','FORALL':'\\forall','EXISTS':'\\mathbb{d}','EXISTS!':'\\mathbb{d}','DOMAIN':'\\vdash','DD':'\\vdash','PROVES':'\\vdash','TURNSTILE':'\\vDash','|-':'\\vDash','TTPROVES':'\\vDash','DTURNSTILE':'\\therefore','|=':'\\because','THEREFORE':':='}

def evaluate_word(word):
    if word in stand_ins:
        return symbol_dict[word]

    return word

def parse_text(path_to_txt_file):
    # parse_text expects a path to a .txt file
    # parse text goes through the text and replaces our keywords with the latex operation, as well as formats based on input formatting...

    new_content = ""

    with open(path_to_txt_file, "r") as file:
        
        # read through file line by line
        for line in file:


            words = line.split(" ")
            sentence = ""

            for word in words:
                if word[0] == '(':
                    setence += " (" + evaluate_word(word[1:])
                elif word[-1] == ')':
                    sentence += " " + evaluate_word(word[0:-1]) + ")"

                else:
                    sentence += " " + evaluate_word(word)

            new_content += sentence + "\n"

                                