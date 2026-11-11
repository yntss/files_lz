import docx
import matplotlib
import pandas as pd 






#Буквы
doc = docx.Document('lion.docx')
text = []
for paragraph in doc.paragraphs:
    text.append(paragraph.text)
text_str = ' '.join(text)
text_str_lower = text_str.lower()
letter_counts = {}
alphabet = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я',]
for letter in text_str_lower:
    if letter in alphabet:
        if letter in letter_counts:
            letter_counts[letter] +=1
        else:
            letter_counts[letter] = 1
print(letter_counts)
wb = Workbook()
ws = wb.active
ws.append(['Буква', 'Встречаемость'])
for key, value in letter_counts():
    ws.apeend([key, value])
wb.save('lion.xlsx')
