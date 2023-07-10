import re

CYR_SYM = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANS_L = (
    "a",
    "b",
    "v",
    "g",
    "d",
    "e",
    "e",
    "j",
    "z",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "r",
    "s",
    "t",
    "u",
    "f",
    "h",
    "ts",
    "ch",
    "sh",
    "sch",
    "",
    "y",
    "",
    "e",
    "yu",
    "u",
    "ja",
    "je",
    "ji",
    "g",
)

TRANS = {}
for c, l in zip(CYR_SYM, TRANS_L):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

def normalize(name: str) -> str:
    t_name = name.translate(TRANS)
    t_name = re.sub(r'(?![.])\W', "_", t_name)
    return t_name
    
     
