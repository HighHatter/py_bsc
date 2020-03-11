"""
Чтобы программа работала, необходим файл data.txt
"""


class Member:
    def __init__(self, last_name=None, name=None, phone_number=None, from_line=None):
        if from_line is None:
            self.last_name = last_name
            self.name = name
            self.phone_number = phone_number
        else:
            self.phone_number, self.name, self.last_name = str(from_line).replace(" ", '').split("|")

    def enter_characters(self):
        self.last_name = input('Input surname: ').capitalize()
        self.name = input('Input name: ').capitalize()
        self.phone_number = input('Input phone number: ').capitalize()

    def __str__(self):
        return '{0:10} | {1:10} | {2}'.format(self.last_name, self.name, self.phone_number) + '\n'


class Contacts:
    def search_member(self, query):
        with open('data.txt') as file:
            for line in file:
                member = Member(from_line=line)
                if (member.last_name, member.name) == query:
                    return member

    def add_member(self):
        m = Member()
        m.enter_characters()
        if c.search_member(query=(m.last_name, m.name)) is None:
            f = open('data.txt', 'a')
            f.write('{0:10} | {1:10} | {2}'.format(m.last_name, m.name, m.phone_number) + '\n')
            print('\n Contact {lastName} {name} successfully added\n'.format(lastName=m.last_name, name=m.name))
            f.close()
        else:
            print('Contact already exists')

    def del_member(self, query):
        objects = []
        f = open('data.txt', 'r+')
        for line in f.readlines():
            member = Member(from_line=line)
            objects.append(member)
        for object in objects:
            if (member.last_name, member.name) != query:
                f.write(object.__str__())
        string = open(data.txt).readlines()

        for i in string:
            if not i.isspace():
                print(i.replace('\n', ''))

    def show_all(self):
        with open('data.txt') as file:
            for line in file:
                member = Member(from_line=line)
                print(member)


def choice():
    selector = None
    try:
        selector = int(input('Press "1" if you want to find contact\n' + \
                             'Press "2" if you want to add new contact\n' + \
                             'Press "3" if you want to delete contact\n' + \
                             'Press "4" if you want to see all contacts\n' + \
                             'Input here ------->:'))
    except ValueError:
        print('\n\nIncorrect input!!!\n')
        print('You have to input int number!!!\n\n')
    return selector


c = Contacts()
while True:
    selector = choice()
    if selector == 1:
        query = ((input('To find a contact enter it`s surname: ').capitalize(),
                  input('To find a contact enter it`s name: ').capitalize()))
        print(c.search_member(query))
    elif selector == 2:
        c.add_member()
    elif selector == 3:
        query = ((input('If you want to delete a contact, enter it`s surname: ').capitalize(),
                  input('If you want to delete a contact, enter it`s name: ').capitalize()))
        c.del_member(query)
    elif selector == 4:
        c.show_all()
