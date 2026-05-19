names_list = ['Jujutsu Kaisen', 'Mo Dao Zu Shi', 'One Piece', 'Apothecary Diaries']

def check_in_list(user_name_search):
    input_letters = set()
    possible_names = []

    for letter in user_name_search:
        input_letters.add(letter.lower())

    for name in names_list:
        name_by_letters, similar_letters, wrong_letters, other_letters = [], [], [], []
        
        for letter in name:
            if letter != ' ':
                name_by_letters.append(letter.lower())

        for letter in input_letters:
            if letter not in similar_letters and letter in name_by_letters:
                times = list(input_letters).count(letter)

                for i in range(times):
                    similar_letters.append(letter)

            if letter not in name_by_letters:
                wrong_letters.append(letter)

        for letter in name_by_letters:
            if letter not in similar_letters and letter not in wrong_letters:
                other_letters.append(letter)

        if len(wrong_letters) >= 1 or len(other_letters) >= 1:
            similarity_points = len(similar_letters) / (len(wrong_letters) + len(other_letters))

        if (len(similar_letters) > len(wrong_letters) and similarity_points > 0.65) or (len(similar_letters) > len(wrong_letters) and similarity_points <= 0.2):
            possible_names.append(name)

        
    print(possible_names)
        
print('\n'*20)

user_input = input('Enter name: ')

check_in_list(user_input)