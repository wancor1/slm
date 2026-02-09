import os,re

if __name__ == "__main__":
    FILE="ch00"
    DATA_DIR="data/src"
    FILEPATH=os.path.join(DATA_DIR,f"{FILE}.md")
    text_original=open(FILEPATH, "r", encoding="utf-8").read()

def tokenize(original: str) -> list:
    delim_chars = r'[\[\]{}#=\-><+\-*/%&|!?.,;:\(\)\"_`~_“~]'
    delims = rf"{delim_chars}+ ?"
    quote_part = r"'[^" + delim_chars[1:-1] + r"\s]* ?"
    whitespace = r"\s+"
    others = r"[^" + delim_chars[1:-1] + r"'\s]+ ?"
    pattern = f"{delims}|{quote_part}|{whitespace}|{others}"
    return [m.lower() for m in re.findall(pattern, original)]

def write_file_tokenize(filepath,text_original):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(tokenize(text_original).__str__())

if __name__ == "__main__":
    print(tokenize(text_original))
    write_file_tokenize(os.path.join(DATA_DIR,f"{FILE}.tkn"), text_original)
