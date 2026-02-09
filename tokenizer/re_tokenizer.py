import os,re


FILE="code"
FILEPATH=os.path.join("data",f"{FILE}.txt")
text_original=open(FILEPATH, "r", encoding="utf-8").read()

def tokenize(original: str) -> list:
    delims = r'([?!.,\(\)\";])\1* ?'
    quote_part = r"'[^?!.,\(\)\";\s]* ?"
    whitespace = r"\s+"
    others = r"[^?!.,\(\)\";'\s]+ ?"
    pattern = f"{delims}|{quote_part}|{whitespace}|{others}"
    return [m.group(0).lower() for m in re.finditer(pattern, original)]

def write_file_tokenize(filepath):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(tokenize(text_original).__str__())

print(tokenize(text_original))
write_file_tokenize(os.path.join("data",f"{FILE}.tkn"))
