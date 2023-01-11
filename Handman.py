import random

def match(text, alphabet=set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')):
    return not alphabet.isdisjoint(text.lower())

hangman = (
"""
------
|    |
|
|
|
|
|
|
|
--------
""",
"""
------
|    |
|    O  |
|
|
|
|
|
|
--------
""",
"""
------
|    |
|    O
|   -+-
|
|
|
|
|
--------
""",
"""
------
|    |
|    O
|  /-+-/
|
|
|
|
|
--------
""",
"""
------
|    |
|    O
|  /-+-/
|    |
|
|
|
|
--------
""",
"""
------
|    |
|    O
|  /-+-/
|    |
|    |
|   |
|   |
|
--------
""",
"""
------
|    |
|    O
|  /-+-/
|    |
|    |
|   | |
|   | |
|
--------
"""
)

max_wrong = len(hangman) - 1
words = ("АВТОМОБИЛЬ", "ПОИСК", "ЭСКАЛАТОР")
used = []
wrong = 0

word = random.choice(words)
guess = "-" * len(word)

print("Виселица")
print("Все слова русские")
while wrong < max_wrong and guess != word:
    print(hangman[wrong])
    print("Уже использованные буквы:", used)
    print("Отгаданное слово выгляжит так:", guess)
    
    user_input = input("Введите букву:")
    user_input = user_input.upper()
    # Проверка на цифру
    while user_input.isalpha() == False:
        print("Вы ввели цифру или символ")
        user_input = input("Введите букву:")
        user_input = user_input.upper() 
    # Проверка на английскую букву
    while match(user_input) == False:
        print("Вы ввели английскую букву")
        user_input = input("Введите букву:")
        user_input = user_input.upper() 
    # Использованна ли буква
    while user_input in used:
        print("Вы уже предлагали эту букву")
        user_input = input("Введите букву:")
        user_input = user_input.upper() 
    used.append(user_input)
    if user_input in word:
        print("Такая буква есть в слове")
        new = ""
        for i in range(len(word)):
            if user_input == word[i]:
                new += user_input
            else:
                new += guess[i]
        guess = new
    else:
        print("Такой буквы не существует")
        wrong +=1

if wrong == max_wrong:
    print(hangman[wrong])
    print("Вы проиграли")
else:
    print("Вы отгадали")

print("Было загадано слово:", word)
