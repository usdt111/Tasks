def vowel_indices(word):
    "Задача на CodeWars"
    vowels = 'aeiouAEIOU'
    return [index + 1 for index, letter in enumerate(word) if letter in vowels]