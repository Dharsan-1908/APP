vowels = ['a', 'e', 'i', 'o', 'u']
sequence = ["e Development Python APP-Lab-Dharsan-fork Practice"]
sequence = sequence.split(',')


def filterVowel(n, vowels):
    return list(filter(lambda x:  x in vowels, n))


print(filterVowel(sequence, vowels))
