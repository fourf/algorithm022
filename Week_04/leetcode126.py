class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []
        word_dict = defaultdict(list)
        for word in word_set:
            for i in range(len(word)):
                word_dict[word[:i] + '*' + word[i+1:]].append(word)
        layer = {beginWord: [[beginWord]]}
        while layer:
            if endWord in layer:
                return layer[endWord]
            new_layer = defaultdict(list)
            for word in layer:
                for i in range(len(word)):
                    for new_word in word_dict[word[:i] + '*' + word[i+1:]]:
                        if new_word in word_set:
                            new_layer[new_word] += [j + [new_word] for j in layer[word]]
            word_set -= set(new_layer.keys())
            layer = new_layer
        return []