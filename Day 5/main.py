from random_word_generator import pick_random_word

def change_current_state(random_word, current_word_state, char):
    modified_word = ""
    for i, j in zip(random_word, current_word_state):
        if j == "_":
            if i == char:
                modified_word += char
            else:
                modified_word += j
        else:
            modified_word += j
    return modified_word


def check_char(random_word, char, current_word_state, attempt_remaining):
    if char in random_word:
        current_word_state = change_current_state(random_word, current_word_state, char)
    else:
        attempt_remaining -= 1
    return current_word_state, attempt_remaining

def print_current_word_state(current_word_state, attempt_remaining):
    print("Current Word State:", end=" ")
    for i in current_word_state:
        print(i, end=" ")
    print("\tAttempts Remaining:", attempt_remaining)

def is_win(current_word_state, random_word):
    if current_word_state == random_word:
        return True
    return False

def main():
    random_word = pick_random_word()
    current_word_state = ""
    attempt_remaining = 5
    for i in random_word:
        if i in ['a', 'e', 'i', 'o', 'u']:
            current_word_state += i
        else:
            current_word_state += '_'

    flag = False
    while attempt_remaining > 0:
        print_current_word_state(current_word_state, attempt_remaining)
        char = input("Guess the character: ")
        current_word_state, attempt_remaining = check_char(random_word, char, current_word_state, attempt_remaining)
        if is_win(current_word_state, random_word):
            flag = True
            print("WINNER WINNER CHICHKEN DINNER!!!")
            break

    if not flag:
        print("You lost :)")
        print("random word was:", random_word)

if __name__ == "__main__":
    main()