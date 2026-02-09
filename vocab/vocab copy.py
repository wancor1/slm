import os,ast

FILE="a"
TOKEN_FILEPATH=os.path.join("data",f"{FILE}.tkn")
DICT_FILEPATH = os.path.join("data", f"{FILE}.dict")
token_original=ast.literal_eval(open(TOKEN_FILEPATH, "r", encoding="utf-8").read()) if os.path.exists(TOKEN_FILEPATH) else []
dict_data=ast.literal_eval(open(DICT_FILEPATH, "r", encoding="utf-8").read()) if os.path.exists(DICT_FILEPATH) else []

# ["text","test","text"]
# ["text","test"]
# [0,1,0]

def gendict(original, *dictdata):
    return dict.fromkeys(original)

def idxdict(original) -> list:
    return [gendict(original)[k] for k in original]

def main(original, *dictdata):
    d=gendict(original,dictdata)
    print(d)
    n=idxdict(original)
    return n

def write_file_tokenize(filepath):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(gendict(filepath).__str__())

#print(main(token_original,dict_data))

print(gendict(token_original))
