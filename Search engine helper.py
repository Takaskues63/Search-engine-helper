names = ['Jujutsu Kaisen', 'Mo Dao Zu Shi', 'One Piece', 'Apothecary Diaries']
user_input = None

def check_in_list(user_input):
    user_input = user_input.lower()
    possible_names = []

    for name in names:
        words, same_letters_in_name = [], []
        words = name.split(' ')
        name = name.lower()

        for word in words:
            same_letters = []
            word = word.lower()

            for letter in user_input:
                if letter.lower() in word and same_letters.count(letter) < word.count(letter):
                    same_letters.append(letter)

                    if same_letters_in_name.count(letter) < user_input.count(letter):
                        same_letters_in_name.append(letter)

            if len(same_letters) / len(word) >= 0.70 and name not in possible_names or len(same_letters_in_name) / len(name) >= 0.54 and name not in possible_names:
                possible_names.append(name)

    print(possible_names)



while True:
    user_input = input('Enter name: (x to exit) ')

    if user_input != 'x':
        check_in_list(user_input)
        
    else:
        break