import pandas as pd  # Импортируем библиотеку для работы с данными
import matplotlib.pyplot as plt  # Импортируем библиотеку для построения графиков

print('прочтение файла titanic.parquet...')
df = pd.read_parquet('titanic.parquet')  #Читаем файл в формате parquet, загружаем данные из файла в DataFrame
print('сохраняю в csv...')
df.to_csv('titanic.csv', index=False)  #Сохраняем таблицу в CSV файл (index=False чтобы не сохранять индексы строк)
print('открываю файл для проверки...')
df_csv = pd.read_csv('titanic.csv')  #Читаем только что созданный CSV файл (проверяем)
print(f'файл успешно открыт. Всего пассажиров в базе: {len(df_csv)}.')
print('подсчёт процентов выживших и не выживших для каждого класса...')
#Далее будем считать проценты выживших и не выживших для каждого класса
classes = [1, 2, 3]  # Три класса билета
survived_percent = []  # Сюда будем класть проценты выживших
died_percent = []  # Сюда будем класть проценты не выживших
for cls in classes:  # Перебираем классы
    class_data = df_csv[df_csv['Pclass'] == cls]  # Берём только пассажиров этого класса
    total = len(class_data)  # Считаем всего пассажиров в классе
    survived = len(class_data[class_data['Survived'] == 1])  # Считаем выживших (где 1)
    died = len(class_data[class_data['Survived'] == 0])  # Считаем не выживших (где 0)
    survived_percent.append(survived / total * 100)  # Добавляем процент выживших
    died_percent.append(died / total * 100)  # Добавляем процент не выживших
plot_data = pd.DataFrame({ # Создаём таблицу для графика
    'Выжил': survived_percent,
    'Не выжил': died_percent
}, index=classes)
print('подсчёт завершён, построение гистограммы выживаемости...')
#Строим составную столбчатую диаграмму (stacked=True делает столбцы составными)
plot_data.plot(kind='bar', stacked=True, color=['steelblue', 'orange'])  # stacked=True делает столбцы составными
plt.title('Выживаемость пассажиров Титаника')  #Заголовок графика
plt.xlabel('Класс билета')  #ось x
plt.ylabel('Процент')  #ось y
plt.xticks(rotation=0)  #Подписи классов горизонтально
plt.legend(loc='upper center')  #Легенда сверху по центру
plt.ylim(0, 100)  #Ось Y от 0 до 100%
plt.show()  #Выводим
print('на графике: синий цвет — выжившие, оранжевый — не выжившие.')
print('файл titanic.csv создан')