def is_palindrome(value: str) -> bool:
    """
    This function determines if a word or phrase is a palindrome

    :param value: A string
    :return: A boolean
    """
    # clean the spaces and other symbols
    # isalnum alphanmeric
    clean_value = ''.join(char.lower() for char in value if char.isalnum())

    reverse = clean_value[::-1]
    return reverse == clean_value

    #pass  # remove pass statement and implement me
