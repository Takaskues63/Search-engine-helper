names_list = ['Jujutsu Kaisen', 'Mo Dao Zu Shi', 'One Piece', 'Apothecary Diaries']

def check_in_list(user_name_search):

    names_list_separated_by_letters = []

    for name in names_list:

        name_by_letters = []
        
        for letter in name:
            if letter !=' ':
                name_by_letters.append(letter.lower())
            else:
                continue

        names_list_separated_by_letters.append(name_by_letters)    

    print('\n'*20)
    print(f'Searching for: {user_input}')
    print()

    possible_names = []
    names_with_similar_letters = []
    name_id = 0

    for name in names_list_separated_by_letters:
        input_sum = 0
        name_sum = 0
        correct_letter = 0
        similar_letters_in_name = []

        for letter in user_name_search:
            wrong_letter = 0
            input_sum += 1

            for i in name:

                if i not in user_name_search:
                    wrong_letter += 1

            if name.count(letter.lower()) > similar_letters_in_name.count(letter.lower()): 
                similar_letters_in_name.append(letter.lower())
                name_sum += 1
                correct_letter += 1

            else:
                continue
            
        
        names_with_similar_letters.append(similar_letters_in_name)

        if name_sum / input_sum >= 0.65 and correct_letter > wrong_letter:
            possible_names.append(names_list[name_id])
    
        name_id += 1
    
    print(f'Results: {possible_names}')
    print()
    
            
print('\n'*20)
user_input = input('Enter name: ')

check_in_list(user_input)