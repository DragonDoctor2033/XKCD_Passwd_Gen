import random
from os.path import exists


def save_password():
    if not exists('password_store.txt'):
        file_to_save = open('password_store.txt', 'x')
    else:
        file_to_save = open('password_store.txt', 'a')
    file_to_save.write(password + '\n')
    file_to_save.close()


words_text = open('enlist_words.txt', 'r')
words_list, symbols, a = words_text.read().split(), '-+=*_.,:;', ''
words_text.close()
random_symbol = random.choice(symbols)
for _ in range(4):
    if random.randint(0, 1) == 1:
        a += random.choice(words_list) + random_symbol
    else:
        a += random.choice(words_list).upper() + random_symbol
password = a + str(random.randrange(1000, 10000))
print(password)
if input('Want to Save the password? Y/N: ').upper() == 'Y':
    save_password()
