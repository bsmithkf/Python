def wordSearch(word,letter):
    sum = 0
    for i in range(len(word)):
        if word[i] == letter:
            sum +=1
    return sum

print(wordSearch('The quick brown fox jumped over the lazy dogs','z'))
