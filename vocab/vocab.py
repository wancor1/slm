import os,ast

if __name__ == "__main__":
    FILE="text"
    TOKEN_FILEPATH=os.path.join("data",f"{FILE}.tkn")
    DICT_FILEPATH = os.path.join("data", f"dict.dict")
    token_original=ast.literal_eval(open(TOKEN_FILEPATH, "r", encoding="utf-8").read()) if os.path.exists(TOKEN_FILEPATH) else []
    dict_data=ast.literal_eval(open(DICT_FILEPATH, "r", encoding="utf-8").read()) if os.path.exists(DICT_FILEPATH) else {}

#def gendict(original, *dictdata):
#    return dict.fromkeys(original)
#
#def idxdict(original) -> list:
#    return [gendict(original)[k] for k in original]

def update_dictionary(original, dict_data):
    dict_data.update({element: i for i, element in enumerate(sorted(list({element for element in original if element not in dict_data})), start=max(dict_data.values(), default=-1) + 1)})
    return dict_data

def write_file_tokenize(filepath, token_original, dict_data):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(update_dictionary(token_original,dict_data).__str__())


if __name__ == "__main__":
    print(update_dictionary(token_original, dict_data))
    write_file_tokenize(DICT_FILEPATH, token_original, dict_data)
