class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left<= right:
            k = (left + right)//2

            no_of_hours=0
            for p in piles:
                if p%k==0:
                    curr_hours = p//k
                else:
                    curr_hours=(p//k) +1
                no_of_hours+= curr_hours
            
            if no_of_hours<= h:
                answer=k
                right = k-1
            else:
                left =k+1
        return answer



        