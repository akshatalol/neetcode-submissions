class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap={}
        for i in strs:
            x="".join(sorted(i))
            if x not in hmap:
                hmap[x]=[]
            hmap[x].append(i)
        return list(hmap.values())