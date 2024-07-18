# import PyPDF2

# path = "C:\\Users\\Bheki Lushaba\\Downloads\\FNAS-UG-2024-v1 (1).pdf"

# with open(path, "rb") as file1:
#     data = PyPDF2.PdfReader(file1)

#     Text = ""

#     for page in range(78, 140):
#         pages = data.pages[page]
#         File_Text = pages.extract_text()
#         Text += File_Text

# with open("C:\\Users\\Bheki Lushaba\\Desktop\\North-West\\Prerequisites.txt", "w", encoding="utf-8") as file2:
#     file2.write(Text)

import pdfplumber

path = "C:\\Users\\Bheki Lushaba\\Downloads\\FNAS-UG-2024-v1 (1).pdf"

# Open the PDF file with pdfplumber
with pdfplumber.open(path) as file1:
    Text = ""
    # Loop through the specified page range
    for page_num in range(78, 140):
        page = file1.pages[page_num]
        File_Text = page.extract_text()
        Text += File_Text

# Write the extracted text to a file
with open("C:\\Users\\Bheki Lushaba\\Desktop\\North-West\\Prerequisites.txt", "w", encoding="utf-8") as file2:
    file2.write(Text)
