import string
from trie import Trie
from typing import List


def clean_text(data: str) -> List[str]:
    translator = str.maketrans("", "", string.punctuation + "\n")

    cleaned_data = data.translate(translator).lower().split(" ")

    return cleaned_data


def main():
    text_data_file = "word_match_testcase.txt"
    text_data = []
    trie = Trie()

    with open(text_data_file, "r") as data:
        temp_text = data.read().split("\n")
        text_data.extend(clean_text(" ".join(temp_text)))

    for text in text_data:
        trie.insert(text)

    while True:
        user_input = input("Enter the word you want to search: ")

        if user_input == "see you in hell":
            print("Bye!! Come again later..")
            break

        found_flag, word_count = trie.search(user_input.lower())
        res = "Found" if found_flag else "Not Found"

        print(f"{res} -> {word_count}")


if __name__ == "__main__":
    main()
