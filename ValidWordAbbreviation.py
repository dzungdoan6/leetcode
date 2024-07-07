def validWordAbbreviation(word: str, abbr: str) -> bool:
    p1 = 0
    p2 = 0
    while p1 < len(word) and p2 < len(abbr):
        if abbr[p2] == '0':
            return False
        
        if not abbr[p2].isnumeric():
            if word[p1] == abbr[p2]:
                p1 += 1
                p2 += 1
                continue
            else:
                return False
        
        p1_step = 0
        while (p2 < len(abbr) and abbr[p2].isnumeric()):
            p1_step = p1_step*10 + int(abbr[p2])
            p2 += 1
        p1 += p1_step
    if p1 == len(word) and p2 == len(abbr):
        return True
    return False

word = 'internationalization'
abbr = 'i12iz4n'
print(validWordAbbreviation(word=word, abbr=abbr))

word = 'apple'
abbr = 'a2e'
print(validWordAbbreviation(word=word, abbr=abbr))

word = "hi"
abbr = "1"
print(validWordAbbreviation(word=word, abbr=abbr))
