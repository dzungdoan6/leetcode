from typing import List
def build_hashmap(word):
    map = {}
    for i in range(len(word)):
        if word[i] in map:
            map[word[i]] += 1
        else:
            map[word[i]] = 1
    return map

def get_common(map, word):
    common = []
    for i in range(len(word)):
        if word[i] in map:
            common.append(word[i])
            map[word[i]] -= 1
            if map[word[i]] == 0:
                del map[word[i]]
    return common

def commonChars(words: List[str]) -> List[str]:
    map = build_hashmap(words[0])
    for i in range(1, len(words)):
        word = words[i]
        common_chars = get_common(map, word)
        map = build_hashmap(common_chars)
    return common_chars

words = ["bella","label","roller"]
print(commonChars(words))

words = ["cool","lock","cook"]
print(commonChars(words))