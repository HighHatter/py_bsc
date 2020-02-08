"""
Изменить программу из Задачи №1 для сортировки слов из текста.

    Пользователь вводит с клавиатуры строки, состоящие из слов.
    Пустая строка означает прекратить ввод текста.
    Программа выводит на экран слова из текста, отсортированные по алфавиту.
"""

from string import whitespace, punctuation


def word_enter(string):
    tab = []
    wrd = ['']
    while wrd:
        tab1 = str.maketrans("""!"#$%&()*+,./:;<=>?@[\\]^_`{|}~""", '                              ')
        wrd = input(string).replace(" - ", ' ').translate(tab1).lower().split()
        tab.extend(wrd)
    return tab


exit_point = True
while exit_point:
    l = word_enter('Please, enter some words: ')
    l.sort()

    for i in range(len(l)):
        print(l[i])

    def exit_que():
        if input('Would you like to exit? (Y/y/Т/т/Д/д): ').lower()[0] in ['y', 'т', 'д']:
            return False
        else:
            return True

exit_point = exit_que()

