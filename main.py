import tokenizer.re_tokenizer as tokenizer
import vocab.vocab as vocab
import os,ast


def process_file(name):
    file=f"{name}"
    data_dir="data/src"
    text_filepath=os.path.join(data_dir,f"{file}.md")
    token_filepath=os.path.join(data_dir,f"{file}.tkn")
    dict_filepath = os.path.join("data", f"dict.dict")
    text_original=open(text_filepath, "r", encoding="utf-8").read()
    token_original=ast.literal_eval(open(token_filepath, "r", encoding="utf-8").read()) if os.path.exists(token_filepath) else []
    dict_data=ast.literal_eval(open(dict_filepath, "r", encoding="utf-8").read()) if os.path.exists(dict_filepath) else {}
    if __name__ == "__main__":
        tokenizer.write_file_tokenize(token_filepath, text_original)
        vocab.write_file_tokenize(dict_filepath, token_original, dict_data)

def all():
    for i in range(22):
        process_file(f"ch{str(i).zfill(2)}")
    process_file("foreword")
    process_file("title-page")
    process_file("SUMMARY")
    process_file("appendix")

if __name__ == "__main__":
    all()