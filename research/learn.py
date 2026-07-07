# 1. Extracting text from a file 

# reading a text file

with open('text.txt', 'r') as f:
    # text = f.read()  # reads entire document
    # text = f.readline  # reads only the first line of the document
    # text = f.readlines()  # reads all lines of the document into a list
    text = f.read(12)  # reads the first 12 characters of the document
    # text = f.replace('old', 'new')  # replaces 'old' with 'new' in the text
    
print(text)
f.close()

# extracting text from a pdf
# library used: PyMuPDF (fitz) : (fastest), pdfplumber (better for tables), PyPDF2 (simple but less accurate)

# import fitz
# doc = fitz.open("Data Science Interview Ques. by Steve Nouri.pdf")
# text = ""
# for page in doc:
#     text += page.get_text()
# print(text)

# import pdfplumber
# text = ""
# with pdfplumber.open("paper.pdf") as pdf:
#     for page in pdf.pages:
#         text += page.extract_text()
# print(text)

# extracting text from a word document
# library used: python-docx

from docx import Document

doc = Document("word.docx")
text = ""
for para in doc.paragraphs:
    text += para.text + "\n"
print(text)

# 2. Processing extracted string (i.e.  as in all cases text from files are extracted as text only)

print(text.lower())  # convert to lower case
print(text.upper())  # convert to upper case
print(text.strip())  # remove leading and trailing whitespace
print(text.replace('PRATIK', 'OM'))  # replaces
print(text.split())  # splits the text into a list of words
print(text.splitlines())  # splits the text into a list of lines
textj = text.split()  # splits the text into a list of words
print(''.join(textj))  # joins the list of words into a single string
print(' '.join(textj))  # joins the list of words into a single string with spaces
print(text.find('ANIL'))  # returns the index of the first occurrence of 'ANIL' in the text
print(text.count('ANIL'))  # returns the number of occurrences of 'ANIL' in the text
print(text.startswith('HI'))  # returns True if the text starts with 'HI', else False
print(text.endswith('ANIL'))  # returns True if the text ends with 'ANIL', else False

# 3. Regular expressions
# Regex is a pattern matching language.
# library used: re

import re
text = "The rain in Spain"
pattern = "ai"
print(re.search(pattern,text)) # returns a match object if the pattern is found in the text, else returns None
print(re.findall(pattern,text)) # returns a list of all occurrences of the pattern in the text
print(re.sub(pattern,"oo",text)) # replaces all occurrences of the pattern in the text with "oo"
print(re.sub(r"\s+"," ",text)) # replaces all sequences of whitespace characters with a single space
print(re.sub(r"\d+","",text)) # removes all digits from the text
print(re.sub(r"[^\w\s]","",text)) # removes all punctuation from the text
print(re.sub(r"[^A-Za-z0-9]","",text)) # removes all special characters from the text

# 4. JSON
# almost every AI application uses JSON to store and exchange data.
# library used: json
import json

data = {
    "filename": "paper.pdf",
    "summary": "AI is changing the world."
}
json_string = json.dumps(data)
print(json_string)

# To convert JSON back into a Python dictionary:
python_data = json.loads(json_string)
print(python_data["summary"])

# You can also save JSON to a file:
with open("summary.json", "w") as file:
    json.dump(data, file, indent=4)