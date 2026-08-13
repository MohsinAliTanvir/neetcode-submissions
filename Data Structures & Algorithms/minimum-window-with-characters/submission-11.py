from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # best_string=""
        # len_best_string=1000000000000000
        # left=0
        # counter2=Counter(t)
        # print("t",counter2)
        # for i in range(len(t),len(s)+1):
        #     curr=s[left:i]

        #     counter1=Counter(curr)
        
         
        #     if not(counter2-counter1):
              
        #         if len_best_string >len(curr):
        #             best_string=curr
        #             len_best_string=len(curr)
        #         if len_best_string==len(t):
        #             return best_string
        #         while not(counter2-counter1):
        #             left+=1
        #             curr=s[left:i]
        #             counter1=Counter(curr)
            
        #             if not(counter2-counter1):
                       
        #                 if len_best_string >len(curr):
        #                     best_string=curr
        #                     len_best_string=len(curr)
        #                 if len_best_string==len(t):
        #                     return best_string

        # return best_string

        from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        counter2 = Counter(t)
        counter1 = Counter()

        left = 0

        have = 0
        required = len(counter2)

        best_left = 0
        best_length = float("inf")

        for i in range(len(s)):

            # Add right character
            counter1[s[i]] += 1

            # Did we just satisfy this character's requirement?
            if s[i] in counter2 and counter1[s[i]] == counter2[s[i]]:
                have += 1

            # Window contains everything from t
            while have == required:

                curr_len = i - left + 1

                if curr_len < best_length:
                    best_length = curr_len
                    best_left = left

                # Remove left character
                counter1[s[left]] -= 1

                # Did removing it make us miss something?
                if (
                    s[left] in counter2
                    and counter1[s[left]] < counter2[s[left]]
                ):
                    have -= 1

                left += 1

        if best_length == float("inf"):
            return ""

        return s[best_left:best_left + best_length]



        