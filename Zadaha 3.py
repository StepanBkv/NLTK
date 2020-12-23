import nltk

#модуль обработки первого предложения
def first():

    #создание грамматики
    grammar = nltk.CFG.fromstring(""" 
    S -> NP VP 
    VP -> V NP | VP PP 
    PP -> P NP 
    NP -> Det N | Det N PP | "Путешесетвенник" 
    V -> "шел" 
    Det -> "несколько" | "небольшими" 
    N -> "дней" | "привалами" 
    P -> "с" 
    """)
    text = "Путешесетвенник шел несколько дней с небольшими привалами"
    words = nltk.word_tokenize(text)

    #создание деревьев синтаксического разбора
    trees = nltk.ChartParser(grammar)

    #вывод каждого дерева
    print("\t\t" + text)
    for t in trees.parse(words):
        print(t)

def second():
    # создание грамматики
    grammar = nltk.CFG.fromstring(""" 
    S -> NP VP 
    VP -> V NP | VP PP 
    PP -> P NP 
    NP -> Det N | Det N PP | "Путешесетвенник" 
    V -> "шел" 
    Det -> "Несколько" | "небольшими" 
    N -> "дней" | "привалами" 
    P -> "с" 
    """)
    text = "Несколько дней с небольшими привалами шел Путешесетвенник"
    words = nltk.word_tokenize(text)

    # создание деревьев синтаксического разбора
    trees = nltk.ChartParser(grammar)

    # вывод каждого дерева
    print("\t\t" + text)
    for t in trees.parse(words):
        print(t)
        # модуль обработки третьего предложения

def third():
    # создание грамматики
    grammar = nltk.CFG.fromstring(""" 
    S -> NP VP 
    VP -> V NP | VP PP 
    PP -> P NP 
    NP -> Det N | Det N PP | "Он" 
    V -> "лежал" 
    Det -> "накрывшись" | "мягком" 
    N -> "диване" | "пледом" 
    P -> "на" 
    """)
    text = "Он лежал накрывшись пледом на мягком диване"
    words = nltk.word_tokenize(text)

    # создание деревьев синтаксического разбора
    trees = nltk.ChartParser(grammar)

    # вывод каждого дерева
    print("\t\t" + text)
    for t in trees.parse(words):
        print(t)

first()
second()
third()