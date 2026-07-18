class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        w1 = len(word1)
        w2 = len(word2)
        a = 0
        b = 0
        while a < w1 or b < w2:
            if a < w1:
                result.append(word1[a])
            if b < w2:
                result.append(word2[b])
            a +=1
            b +=1
        return "".join(result)
        