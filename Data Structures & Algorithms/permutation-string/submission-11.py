class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left=0
        out=False
        
        for i in range(len(s1),len(s2)+1):
            #s1=set(s1)
            current_str=s2[left:i]
            #current_str=set(current_str)
            # count=0
            # print("Current", current_str)
            # for letter in s1:
            #     if letter in current_str:
            #         count+=1
            #         print("Count", count)
                
            
            # if count==len(s1):
            #     return True
            sorted_text1 = sorted(s1)
            sorted_text2=sorted(current_str)
            if sorted_text1== sorted_text2:
                return True
            left+=1
        return False

    