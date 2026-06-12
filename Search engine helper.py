names = ['Jujutsu Kaisen', 'Mo Dao Zu Shi', 'One Piece', 'Apothecary Diaries']
user_input = None

def check_in_list(user_input):
    user_input = user_input.lower()
    possible_names = []

    for name in names:
        same_letters = []

        for letter in user_input:
            if letter in name.lower() and same_letters.count(letter) < name.count(letter):
                same_letters.append(letter)

        if len(same_letters) / len(name) > 0.54:
            possible_names.append(name)

    print(possible_names)

while True:
    user_input = input('Enter name: (x to exit) ')

    if user_input != 'x':
        check_in_list(user_input)
        
    else:
        break