import re

def code():
    path = "C:\\Users\\Bheki Lushaba\\Desktop\\North-West\\NaturalScience.txt"

    with open(path, "r", encoding="utf-8") as file1:
        data = file1.read()

        pattern = r"([A-Z]+\d{3}\s*Semester|[A-Z]+\d{3}\s*\(|[A-Z]+\s*\d{3}\s*\(|[A-Z]+\d+\s*\d+\s*\()"

        file_new = re.sub(pattern, r"Code: \1", data)
    with open("C:\\Users\\Bheki Lushaba\\Desktop\\North-West\\NaturalScienceFinal.txt", "w", encoding="utf-8") as file2:
        file2.write(file_new)

def duration():
    with open("C:\\Users\\Bheki Lushaba\\Desktop\\North-West\\NaturalScienceFinal.txt", "r", encoding="utf-8") as file1:
        data = file1.read()

        pattern = r"(Code:\s*\s*[A-Z]+\s*\d+)\s*(.+)"

        file_new = re.sub(pattern, r"\n\1\nDuration: \2", data)
    with open("C:\\Users\\Bheki Lushaba\\Desktop\\North-West\\NaturalScienceFinal.txt", "w", encoding="utf-8") as file2:
        file2.write(file_new)

def nqf():
    with open("C:\\Users\\Bheki Lushaba\\Desktop\\North-West\\NaturalScienceFinal.txt", "r", encoding="utf-8") as file1:
        data = file1.read()

        pattern = r"(NQF\s*Level\s*:\s*|NQF\s*\-\s*Level\s*:\s*|NQF\s*level\s*)"

        file_new = re.sub(pattern, r"\nNQF: ", data)
    with open("C:\\Users\\Bheki Lushaba\\Desktop\\North-West\\NaturalScienceFinal.txt", "w", encoding="utf-8") as file2:
        file2.write(file_new)


def name():
    with open("C:\\Users\\Bheki Lushaba\\Desktop\\North-West\\NaturalScienceFinal.txt", "r", encoding="utf-8") as file1:
        data = file1.read()

        pattern = r"NQF:\s*(.+)\n(.+)"

        file_new = re.sub(pattern, r"NQF: \1\nName: \2", data)
    with open("C:\\Users\\Bheki Lushaba\\Desktop\\North-West\\NaturalScienceFinal.txt", "w", encoding="utf-8") as file2:
        file2.write(file_new)

def description():
    with open("C:\\Users\\Bheki Lushaba\\Desktop\\North-West\\NaturalScienceFinal.txt", "r", encoding="utf-8") as file1:
        data = file1.read()

        pattern = r"(Module\s*outcomes\s*:\s*|Module\s*outcome\s*:\s*|Module\s*Outcomes\s*:\s*)"

        file_new = re.sub(pattern, r"Description: ", data)
    with open("C:\\Users\\Bheki Lushaba\\Desktop\\North-West\\NaturalScienceFinal.txt", "w", encoding="utf-8") as file2:
        file2.write(file_new)

def assessments():
    with open("C:\\Users\\Bheki Lushaba\\Desktop\\North-West\\NaturalScienceFinal.txt", "r", encoding="utf-8") as file1:
        data = file1.read()

        pattern = r"(Assessment\s*modes:\s*)"

        file_new = re.sub(pattern, r"Assessments: ", data)
    with open("C:\\Users\\Bheki Lushaba\\Desktop\\North-West\\NaturalScienceFinal.txt", "w", encoding="utf-8") as file2:
        file2.write(file_new)


code()
duration()
nqf()
name()
description()
assessments()