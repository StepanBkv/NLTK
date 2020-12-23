import nltk
from nltk.corpus import stopwords
from pymorphy2 import MorphAnalyzer

# Морфологический анализатор
morph = MorphAnalyzer()
# Исполнение кода #
if __name__ == '__main__':
    # Считывание текста из dataset #
    with open('input', encoding='utf-8') as f:
        text = f.readlines()
    text = '\n'.join(text)

    # Удаление из текста стоп-слов #

    stop_words = set(stopwords.words('russian'))  # Стоп-слова

    words = nltk.word_tokenize(text)  # Токенизация текста

    without_stop_words = set([word for word in words if word not in stop_words and word.isalnum()])

    # Морфологический разбор каждого слова #
    result = []
    for word in without_stop_words:
        p = morph.parse(word)[0]
        result.append("Слово: " + word + "\nНормальная форма: " + str(
            p.normal_form) + "\nМорфологический разбор слова: " + p.tag.cyr_repr + '\n\n')
        # ----------------------------- #
    # Запись в файл #
    with open('output', 'w', encoding='utf-8') as f:
        f.write(''.join(result))
        print('Данные занесены в файл \'output\'')
        # ----------------------------- #