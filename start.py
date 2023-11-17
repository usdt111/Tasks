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


#____________________________________________________________________________________


def find_outlier(integers):
    j = 0
    k = 0
    g = []
    f = []
    for i in integers:
        if i % 2 == 0:
            j += 1
            g.append(i)
        else:
            k += 1
            f.append(i)
    if j > k:
        return int(''.join(map(str, f)))
    elif k > j:
        return int(''.join(map(str, g)))

#____________________________________________________________________________________

def array_diff(a, b):
    for i in b:
        if i in a:
            while i in a:
                a.remove(i)
    return a

#____________________________________________________________________________________

def array_diff(a, b):
    for i in b:
            while i in a:
                a.remove(i)
    return a