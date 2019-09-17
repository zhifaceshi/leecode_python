class Solution(object):
    def replaceWords(self, candidates, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        ans = []
        candidates = sorted(candidates)
        for word in sentence.split():
            N = len(ans)
            for can in candidates:
                if word.startswith(can):
                    ans.append(can)
                    break
            if N == len(ans):
                ans.append(word)
        return " ".join(ans)
