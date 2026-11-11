import docx
import pandas as pd 
import matplotlib.pyplot as plt

doc = docx.Document('lion.docx') #Читаем документ
text = []
for paragraph in doc.paragraphs: #Перебираем все абзацы в документе
    text.append(paragraph.text) #Загоняем весь документ в переменную
text_str = ' '.join(text)
text_str_lower = text_str.lower() #Делаем единообразный регистр (нижний), потому что одна и та же буква, но при этом большая и маленькая воспринимаются как две разные
letter_counts = {} #Пустой словарь для подсчёта букв
alphabet = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я',] #Вводим алфавит, чтобы не считать количество ненужных нам символов (французские буквы, символы)
for letter in text_str_lower: #Перебираем все буквы в тексте
    if letter in alphabet: #Условие для того чтобы мы не считали сколько раз употребляются символы, которые нас не интересуют
        if letter in letter_counts: #Если буква есть в словаре, увеличиваем счётчик на 1
            letter_counts[letter] +=1
        else:
            letter_counts[letter] = 1 #Если нету, присваиваем букве значение 1
total_letters = sum(letter_counts.values()) #Считаем общее кол-во всех букв
letters_data = [] #Пустой список для хранения данных о буквах
for letter, count in letter_counts.items(): #Перебираем все буквы, .items возвращает пару ключ-значение
    percent = (count/total_letters)*100 #Считаем проценты
    letters_data.append({ #Добавляем в раннее созданный список все данные о букве
        'Буква': letter,
        'Сколько раз встретилось': count,
        'Сколько процентов': round(percent, 2)
    })
punctuation = '.,!?;:()[]{}"\'«»—–\n\t' #Перебираем все знаки препинания, чтобы убрать их из нашего текста
text_clean = text_str_lower #Создаём "чистый" список (без спецсимволов, знаков препинания)
for symbol in punctuation: #Перебираем все символы, заменяем их на пробел
    text_clean = text_clean.replace(symbol, ' ') 
words_list = text_clean.split() #Разбиваем чистый список на слова (.split отвечает за это)
word_counts = {}
for word in words_list:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
total_words = sum(word_counts.values())
words_data = []
for word, count in word_counts.items():
    percent = (count / total_words) * 100
    words_data.append({
        'Слово': word,
        'Частота встречи, раз': count,
        'Частота встречи в %': round(percent, 2)
    }) #Начиная со строки 33 те же самые действия что и с буквами
df_letters = pd.DataFrame(letters_data) 
df_words = pd.DataFrame(words_data) #Сохраняем две таблицы (слова и буквы)
df_letters.to_excel('letters_result.xlsx', engine='openpyxl')
df_words.to_excel('words_result.xlsx', engine='openpyxl') #Перегоняем эти таблицы в excel
df_letters.plot(x='Буква', y='Сколько раз встретилось', kind='bar') #строим столбчатую диаграмму из таблицы (kind='bar' отвечает за столбчатую диаграмму)
plt.title('Встречаемость букв в тексте') #Заголовок
plt.xlabel('Буквы') # ось x
plt.ylabel('Количество') #ось y
plt.show() #выводим