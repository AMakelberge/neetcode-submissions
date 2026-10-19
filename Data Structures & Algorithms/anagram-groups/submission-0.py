class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for s in strs:
            length = len(s)
            counts = [0] * 26

            for i in range(length):
                counts[ord(s[i])-ord('a')] += 1

            res[tuple(counts)].append(s)

        return list(res.values())
    
            