import random


LETTER_SCORES = {
    "А": 1,
    "Б": 3,
    "В": 1,
    "Г": 3,
    "Д": 2,
    "Е": 1,
    "Ё": 3,
    "Ж": 5,
    "З": 5,
    "И": 1,
    "Й": 4,
    "К": 2,
    "Л": 2,
    "М": 2,
    "Н": 1,
    "О": 1,
    "П": 2,
    "Р": 1,
    "С": 1,
    "Т": 1,
    "У": 2,
    "Ф": 10,
    "Х": 5,
    "Ц": 5,
    "Ч": 5,
    "Ш": 8,
    "Щ": 10,
    "Ъ": 10,
    "Ы": 4,
    "Ь": 3,
    "Э": 8,
    "Ю": 8,
    "Я": 3,
}


def get_random_letter():
    all_keys = list(LETTER_SCORES.keys())
    random_letter = random.choice(all_keys)
    return random_letter


def get_word_with_letter(random_letter):
    while True:
        word = input(f"Введите слово на букву {random_letter}: ").upper()
        if word[0] == random_letter:
            return word
        else:
            print("ТЫ подумал перед тем как отвечать???")


def calculate_score(word):
    all_scores = []
    for letter in word:
        scores = LETTER_SCORES.get(letter.upper(), 0)
        all_scores.append(scores)
    sum_scores = sum(all_scores)
    return sum_scores


def main():
    random_letter = get_random_letter()
    print(f"Ваша случайная буква {random_letter}")
    print("Ход игрока один")
    first_player = get_word_with_letter(random_letter)
    print("Ход игрока два")
    second_player = get_word_with_letter(random_letter)
    first_player_score = calculate_score(first_player)
    print(first_player_score)
    second_player_score = calculate_score(second_player)
    print(f"Игрок 1 ввёл слово {first_player} и получил {first_player_score} очков")
    print(f"Игрок 2 ввёл слово {second_player} и получил {second_player_score} очков")
    if first_player_score > second_player_score:
        print("Игрок 1 победил!")
    elif second_player_score > first_player_score:
        print("Игрок 2 победил!")
    else:
        print("Ничья!")


if __name__ == '__main__':
    main()
