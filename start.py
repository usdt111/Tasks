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

#____________________________________________________________________________________


def is_prime(num):
    j = 0
    l = []
    while num >= j:
        j += 1
        if num % j == 0:
            l.append(j)
    if len(l) == 2:
        return True
    else:
        return False

#____________________________________________________________________________________

def break_chocolate(n, m):
    if n == 0 or m == 0:
        return 0
    return n * m - 1

#____________________________________________________________________________________

def get_even_numbers(arr):
    p = []
    for i in arr:
        if i % 2 == 0:
            p.append(i)
    return p


#____________________________________________________________________________________


def solve(s):
    a = 0
    b = 0
    for i in s:
        if i.isupper == True:
            a += 1
        else:
            b += 1
    if a > b:
        return s.upper()
    else:
        return s.lower()

#____________________________________________________________________________________

def calculate(num1, operation, num2): 
    if operation == "+":
        return num1 + num2
    if operation == "-":
        return num1 - num2
    if operation == "*":
        return num1 * num2
    if operation == "/" and num1 != 0 and num2 != 0:
        return num1 / num2
    else:
        return None
        
#____________________________________________________________________________________

def is_prime(num):
    j = 1
    a = []
    while num >= j:
        if num % j == 0:
            a.append(j)
        j += 1
    if len(a) == 2:
        return True
    else:
        return False


#____________________________________________________________________________________

def show_sequence(n):
    p = []
    if 0 > n:
        return f"{n}<0"
    elif n == 0:
        return "0=0"
    a = []
    
    for i in range(n + 1):
        a.append(i)
    for i in range(n + 1):
        if i == n:
            p.append(i)
        else:
            p.append(f"{i}+")
    l = sum(a)
    return f"{''.join(map(str, p))} = {l}"

#____________________________________________________________________________________


def digits(n):
    return len(str(n))

#____________________________________________________________________________________


def remove_url_anchor(url):
    a = []
    for i in url:
        if i == "#":
            break
        else:
            a.append(i)
    return ''.join(map(str, a))