def vowel_indices(word):
    "Задача на CodeWars"
    vowels = 'aeiouAEIOU'
    return [index + 1 for index, letter in enumerate(word) if letter in vowels]
#_________________________________________________________________________________


def make_upper_case(s):
    return s.upper()


#____________________________________________________________________________________



def power_of_two(x):
    if x == 0:
        return False
    if x & (x - 1) == 0:
        return True
    else:
        return False