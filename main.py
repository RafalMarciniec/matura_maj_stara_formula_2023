path_to_file = r"Dane_2305\slowa.txt"


# path_to_file = r"Dane_2305\przyklad.txt"


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
    for word in sanitized_input:
        results.append(
            min({letter: list(word).count(letter) if letter != "a" else list(word).count(letter) // 2 for letter in
                 letters}.items(), key=lambda x: x[1])[1])
    print(results)


def ex_4_3(sanitized_input):
    word_to_find = "wakacje"
    for word in sanitized_input:
        idx = 0
        wak = ""
        for letter in word:
            if letter == word_to_find[idx]:
                wak += letter
                idx = (idx + 1) % 7
        print(len(word) - len(wak[:7 * (len(wak) // 7)]))


if __name__ == '__main__':
    abc = sanitize_input()
    # ex_4_1(abc)
    # ex_4_2(abc)
    ex_4_3(abc)
