import numpy as np


def word_count_by_maximum_word_length_and_alphabet_cardinality(maximum_word_length, alphabet_cardinality):
    return np.array([word_count_by_exact_word_length_and_alphabet_cardinality(t, alphabet_cardinality) for t in
                     range(0, maximum_word_length + 1)]).sum()


def word_count_by_exact_word_length_and_alphabet_cardinality(exact_word_length, alphabet_cardinality):
    return pow(alphabet_cardinality, exact_word_length)


def position_in_lexicographical_order(alphabet, word):
    # skipping word correctness check (only contains symbols from alphabet)
    # first calculate how many shorter words exist
    shorter_words_count = word_count_by_maximum_word_length_and_alphabet_cardinality(len(word) - 1, len(alphabet))
    # and then calculate the position in words with same length
    position_in_length = np.array(
        [alphabet.index(word[i]) * pow(len(alphabet), len(word) - i - 1) for i in range(0, len(word))]).sum()
    return int(shorter_words_count + position_in_length)


def word_by_lexicographical_index(alphabet, index):
    i = 0;
    while index - word_count_by_exact_word_length_and_alphabet_cardinality(i, len(alphabet)) >= 0:
        index = index - word_count_by_exact_word_length_and_alphabet_cardinality(i, len(alphabet))
        i += 1
    word = ""
    mod = 0
    while i > 0:
        i -= 1
        mod = index % pow(len(alphabet), i)
        j = (index - mod) / pow(len(alphabet), i)
        word += alphabet[int(j)]
        index = mod
    return word


def main():
    print(
        "An alphabet of cardinality 3 has not more than " + str(
            word_count_by_maximum_word_length_and_alphabet_cardinality(
                5, 3)) + " words of length 5 or shorter!")
    # print(
    #     "An alphabet of cardinality 5 has not more than " + str(
    #         word_count_by_maximum_word_length_and_alphabet_cardinality(
    #             7, 5)) + " words of length 7 or shorter!")
    # print("The word \"1177\" has the lexicographical position " + str(
    #     position_in_lexicographical_order(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'],
    #                                       "1177")) + " over the alphabet {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}")
    # print("The word \"babb\" has the lexicographical position " + str(
    #     position_in_lexicographical_order(['a', 'b'],
    #                                       "babb")) + " over the alphabet {a, b}")
    # print("The word at lexicographical index 26 over alphabet {a, b} is \"" + word_by_lexicographical_index(['a', 'b'],
    #                                                                                                        26) + "\"")
    print("Nr. 1.5a) \"abba\" steht an Stelle " + str(
        position_in_lexicographical_order(['a', 'b', 'c', 'd', 'e'], "abba")) + " im Alphabet {a,b,c,d,e}")
    print("Nr. 1.5b) An Stelle 1000 steht das Wort " + word_by_lexicographical_index(['a', 'b', 'c', 'd', 'e'], 1000))
    print("Nr. 2.1: " + str(
        position_in_lexicographical_order(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k'], "aaaa")))
    print("Nr. 2.2: " + str(word_by_lexicographical_index(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k'], 11110)))


if __name__ == "__main__":
    # execute only if run as a script
    main()
