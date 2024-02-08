# Student Number : 22031444
VOWELS = "aeiou"


def get_shifted_vowel(vowel, vowel_count):
    """
     DEFINITION  : This function takes as input a string s that contains some numbers 
                   and calculates the sum of all the digits in the string, ignoring any symbols that are not digits.

      INPUT :
         Get Shifted Vowel character depending upon the number of times vowel repeated in the word
         :param vowel: vowel character
         :param vowel_count: Count of vowel character repeated in the word
         :return: vowel character shifted depending upon the vowel_count

        WORKING : 
              1. Get the index of the vowel character in VOWELS
              2. Get the right shifted index of the vowel depending on the vowel repeated count.
              3. Return the shifted vowel of same case.
     OUTPUT(s) :
        shifted_vowel_string : string variable that stores new string with shifted vowels.

     EXAMPLE USAGE :
        consider string, s1 = 'eeUUi'
        new_updated_string = shift_vowel(s)

    """
    # Get the index of the vowel character in VOWELS
    index = VOWELS.index(vowel.lower())

    # Get the right shifted index of the vowel depending on the vowel repeated count
    n = (index + vowel_count + 1) % 5

    # Get the shifted vowel character
    shifted_vowel = VOWELS[n]

    # Return the shifted vowel of same case
    return shifted_vowel.upper() if vowel.isupper() else shifted_vowel


def get_shifted_vowel_word(word):
    """
    DEFINITION  : This function takes as input a string s that contains some numbers 
                  and calculates the sum of all the digits in the string, ignoring any symbols that are not digits

    INPUT  :
                Get word with shifted vowels depending upon the number of times vowel repeated in the word
                param word: Word in which vowels needs to be shifted
                return: Word in which vowels are shifted.

   WORKING :
                1.Iterate over each character of the word
                2.Check if the character is an vowel
                3.If character is an vowel and repeated n times get the shifted vowel
                 
   OUTPUT(word) : 
                return sum of the digits   

   EXAMPLE USAGE :
                consider string, word = '183Wales'
                 sum = sum_of_digits(word)              
    """
    shifted_vowel_string = ""
    # Iterate over each character of the word
    for character in word:
        # Check if the character is an vowel
        if character.lower() in VOWELS:
            # If character is an vowel and repeated n times get the shifted vowel
            shifted_vowel_string += get_shifted_vowel(character, word.lower().count(character.lower()))
        else:
            shifted_vowel_string += character
    return shifted_vowel_string


def shift_vowel(string):
    """
    Get word with shifted vowel.
    :param string: string in which vowels needs to be shifted 
    :return: Word in which vowels are shifted.
    """
    return " ".join(get_shifted_vowel_word(word) for word in string.split())


def separate_digits_and_non_digits_from_tuple(tuple_data):
    """
    Separate digits and non digits from the given
    :param tuple_data: Tuple of strings
    :return: lists of digits and non digits
    """
    digits = []
    non_digits = []
    for string in tuple_data:
        for character in list(string):
            # Check if character is numeric and append to digits list
            if character.isnumeric():
                digits.append(int(character))
            # If condition fails, append to non digits list
            else:
                non_digits.append(character)
    return digits, non_digits


def sum_of_digits(string):
    """
    Get sum of integer digits in the given string.
    :param string: String with/without integer digits in it
    :return: sum of integer digits
    """
    digits, non_digits = separate_digits_and_non_digits_from_tuple(string)
    if digits:
        print("The sum of digits operation performs {}","+".join([str(i) for i in digits]))
        print("The extracted non-digits are:  {}".format(non_digits))
    if not digits and non_digits:
        print("The sum of digits operation could not detect a digit!")
        print("The returned input letters are:  {}".format(non_digits))
    if not digits and not non_digits:
        print("Empty string entered!")

    return sum(digits)
