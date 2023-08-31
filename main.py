path_to_file = r"Dane_2305\slowa.txt"


# path_to_file = r"Dane_2305\przyklad.txt"


WAKACJE_WORD = "wakacje"


def sanitize_input():
    with open(path_to_file, "r") as f:
        return [item.replace("\n", "") for item in f.readlines()]


def ex_4_1(sanitized_input):
    results = [item for item in sanitized_input if list(item).count("w") == list(item).count("k")]
    for result in results:
        print(result)


def ex_4_2(sanitized_input):
    letters = set(WAKACJE_WORD)
    results = []
    for word in sanitized_input:
        results.append(
            min({letter: list(word).count(letter) if letter != "a" else list(word).count(letter) // 2 for letter in
                 letters}.items(), key=lambda x: x[1])[1])
    print(results)


def ex_4_3(sanitized_input):
    for word in sanitized_input:
        idx = 0
        wakacje = ""
        #can be done better? to reconsider
        for letter in word:
            if letter == WAKACJE_WORD[idx]:
                wakacje += letter
                idx = (idx + 1) % 7
        print(len(word) - len(wakacje[:7 * (len(wakacje) // 7)]))


if __name__ == '__main__':
    abc = sanitize_input()
    ex_4_1(abc)
    ex_4_2(abc)
    ex_4_3(abc)
