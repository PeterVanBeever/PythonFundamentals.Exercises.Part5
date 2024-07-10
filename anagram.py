def is_anagram(first_string: str, second_string: str) -> bool:
    """
    Given two strings, this functions determines if they are an anagram of one another.
    """
    #pass  # remove pass statement and implement me

    #sort strings in order of char
    #compare the two strings if match

    word1 = sorted(first_string)
    word2 = sorted(second_string)
    return word1 == word2