path_to_file = r"Dane_2305\slowa.txt"


path_to_file = r"Dane_2305\przyklad.txt"


def sanitize_input():
    with open(path_to_file, "r") as f:
        return [item.replace("\n", "") for item in f.readlines()]


def ex_4_1(sanitized_input):
    results = [item for item in sanitized_input if list(item).count("w") == list(item).count("k")]
    for result in results:
        print(result)


def ex_4_2(sanitized_input):
    letters = ("a", "c", "e", "k", "j", "w")
    results = []
    sanitized_input = sanitized_input[38:39]
    for word in sanitized_input:
        counter = {letter: list(word).count(letter) for letter in letters}
        minimum_letter = min(counter.items(), key=lambda x: x[1])
        result = minimum_letter[1]//2 if minimum_letter[0]=='a' else minimum_letter[1]
        results.append(result)
    a =1

if __name__ == '__main__':
    abc = sanitize_input()
    # ex_4_1(abc)
    ex_4_2(abc)
