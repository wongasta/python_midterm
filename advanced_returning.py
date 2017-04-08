vowels = ['a', 'e', 'i', 'o', 'u']

def count_vowels(word):
    total = 0
    total_count = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0
    }
    for letter in word:
        if letter in vowels:
            total_count[letter] += 1
            total += 1
    return {
        'total_vowel': total,
        'total_count': total_count
    }

result = count_vowels('michael')
print('Total Vowels: ' + str(result['total_vowel']))
print('Breakdown: ' + str(result['total_count']))