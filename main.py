# ----------------------------- #
# Графематический анализатор #
# ----------------------------- #

from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
# Чтение файла с Dataset и деление на отдельные предложения;
with open("input", encoding='utf-8') as f:
    line = f.read()
sent_line = sent_tokenize(line)

with open('output', 'w', encoding='utf-8') as f:
    f.write("Пример работы метода разбиения текста на предложения(sent_tokenize):\n\n")
    for letter in sent_line:
        f.write(letter)
        if letter != sent_line[-1]:
            f.write('     ********     \n')
    f.write("\nКоличество предложений: " + str(len(sent_line)) + "\n\n")
word_line = word_tokenize(line)

with open('output', 'a', encoding='utf-8') as f:
    f.write("Пример работы метода разбиения предложений текста на слова и знаки(word_tokenize):\n\n")
    for letter in word_line:
        f.write(letter)
        if letter != word_line[-1]:
            f.write(' *** ')
    f.write("\nКоличество слов: " + str(len(word_line)) + "\n\n")
without_stop_words = [word for word in word_line if not word.lower() in stopwords.words('russian')]

with open('output', 'a', encoding='utf-8') as f:
    f.write("Удаление русских стоп-слов из исходного текста файла:\n\n")
    for letter in without_stop_words:
        f.write(letter)
        if letter != without_stop_words[-1]:
            f.write(' ')
    f.write("\nКоличество слов: " + str(len(without_stop_words)))
    print('Данные занесены в файл \'output\'')

