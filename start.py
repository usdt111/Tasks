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

#____________________________________________________________________________________

def find_smallest(numbers,to_return):
    a = min(numbers)
    if to_return == "value":
        return a
    if to_return == "index":
        return numbers.index(a)
    
#____________________________________________________________________________________


def is_triangle(a, b, c):
    if a >= b + c or b >= a + c or c >= a + b:
        return False
    else:
        return True