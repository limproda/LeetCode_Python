class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        difCandies = len(candyType)/2
        res = set(candyType)
        if len(res) < difCandies:
            return len(res)
        else:
            return int(difCandies)
