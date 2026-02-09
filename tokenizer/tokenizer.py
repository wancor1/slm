import os

FILE="code"
FILEPATH=os.path.join("data",f"{FILE}.txt")

DELIMITER=[" ","\n","\t",",",".","!","?",";",":","'","\"","(",")","[","]","{","}","-","_","/","\\"]
SPACES=[" ","\t"]
NLINE=["\n"]
APOSTROPHE=["\'"]

text_original=open(FILEPATH, "r", encoding="utf-8").read()


def tokenize(original)->list:
    tokenized=[]
    buffer=[]
    buffer_=[]
    bfbf=[]
    for i in original:
        if i in DELIMITER:
            buffer.append(i)
            if buffer:
                if bfbf:
                    buffer.insert(0,''.join(bfbf))
                    bfbf.clear()
                for l in buffer:
                    if l in DELIMITER:
                        if not l in APOSTROPHE:
                            buffer.remove(l)
                            buffer_.append(l)
                if buffer and buffer[-1] == SPACES[0] and len(buffer)+len(buffer_) == 1:
                    buffer.clear()
                if buffer and buffer[-1] == APOSTROPHE[0]:
                    bfbf.append(buffer.pop())
                if buffer:
                    if buffer_:
                        buffer.append(''.join(buffer_))
                    tokenized.append(''.join(buffer))
                buffer=[]
                buffer_=[]
        else:
            buffer.append(i.lower())
    return tokenized

def write_file_tokenize(filepath):
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(tokenize(text_original).__str__())

print(tokenize(text_original))

write_file_tokenize(os.path.join("data",f"{FILE}.tkn"))
