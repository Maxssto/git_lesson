def word_finder(txt, users_word):
    word_list = []

# Добавление слов в список
    for word in txt.split():
        clear_word = ""
        for letter in word:
            if letter.isalpha():
                clear_word += letter.lower()
        word_list.append(clear_word)

# Удаление пустых элеметов списка
    while "" in word_list:
        word_list.remove("")

    num_of_words = word_list.count(users_word.lower())
    return num_of_words


print(word_finder("Лексический повтор – это повторение одного и того же или однокоренного слова, а то и нескольких"
                  "слов. Это может быть специально примененным приемом. Но нередко бывает просто ошибкой и "
                  "объясняется не стремлением подчеркнуть какую-то мысль особо, а невнимательностью, недостаточным "
                  "словарным запасом и другими причинами, не имеющими отношения к выразительности текста", 'И'))
print("Теперь я в гит")