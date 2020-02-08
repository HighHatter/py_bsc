"""
Реализовать программу для подсчёта слов в тексте.

    Пользователь вводит с клавиатуры строки, состоящие из слов.
    Пустая строка означает прекратить ввод текста.
    Программа формирует словарь со статистикой слов в котором слова являются ключами, а значения - количество повторений слова
    Вывести словарь статистики на экран в виде форматированной таблицы.

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
    st = set(l)
    ls = list(st)
    d = {}
    for i in range(len(ls)):
        d[ls[i]] = l.count(ls[i])

    max_length = len(max(ls, key=len))

    for i in range(len(d)):
        print('|', ls[i], ' ' * (max_length - len(ls[i])), '|', d.get(ls[i]), '|',
              sep='')


        def exit_que():
            if input('Would you like to exit? (Y/y/Т/т/Д/д): ').lower()[0] in ['y', 'т', 'д']:
                return False
            else:
                return True
    exit_point = exit_que()
