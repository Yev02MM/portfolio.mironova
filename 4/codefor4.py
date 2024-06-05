print('Міронова Євгенія, 2 група, Лабораторна робота 7')
import re
import _sqlite3
import sys
import locale
import unicodedata

# Встановити польську локаль
locale.setlocale(locale.LC_ALL, 'pl_PL.utf8')

conn = _sqlite3.connect('pol_lab07.s3db')
curs = conn.cursor()

# Змінити кодування стандартного виводу на системне кодування
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding=sys.stdout.encoding, errors='replace', buffering=1)

# Знайти будь-яке одне слово в початковій формі
curs.execute("SELECT sgN FROM tnoun WHERE sgN='sprawa'")
print(curs.fetchone()[0])

# Вивести в консоль через кому всі слова, які починаються на задану літеру + відмінок
curs.execute("SELECT sgN FROM tnoun WHERE sgG LIKE 'r_%'")
words = [unicodedata.normalize('NFC', word[0]) for word in curs.fetchall()]
print(", ".join(words))

#додати до БД нове слово + рід
gender = "1"
nw = "ptak"
curs.execute(f"INSERT INTO tnoun (gender, sgN) VALUES(\'{gender}\', \'{nw}\')")
curs.execute("SELECT sgN, gender FROM tnoun ORDER BY id DESC LIMIT 1")
print(curs.fetchone())

####
def parse(lemma):
    pattern1 = re.compile(f"(?P<word>\w*)\t{lemma}\t(?P<tags>.+)")
    pattern2 = re.compile("(?<=sg:)[\w\.]+(?=:)")
    with open("parse_lab07.txt", "r", encoding="utf-8") as h:
        lines = h.readlines()

    valid = []
    for line in lines:
        check = re.match(pattern1, line)
        if check:
            valid.append(check.group("word", "tags"))

    for line in valid:
        iter = re.finditer(pattern2, line[1])
        if iter:
            for i in iter:
                if i.group(0) == "nom":
                    sgN = line[0]
                elif i.group(0) == "gen":
                    sgG = line[0]
                elif i.group(0) == "dat":
                    sgD = line[0]
                elif i.group(0) == "acc":
                    sgA = line[0]
                elif i.group(0) == "inst":
                    sgI = line[0]
                elif i.group(0) == "loc":
                    sgL = line[0]
                elif i.group(0) == "voc":
                    sgV = line[0]

    return [sgN, sgG, sgD, sgA, sgI, sgL, sgV]


forms = parse(nw)
column_list = ["N", "G", "D", "A", "I", "L", "V"]

for i, column in enumerate(column_list):
    curs.execute(f"UPDATE tnoun SET sg{column}=\'{forms[i]}\' WHERE sgN = \'{nw}\'")
curs.execute(f"SELECT * FROM tnoun ORDER BY id DESC LIMIT 1")
print(curs.fetchone())
conn.commit()

