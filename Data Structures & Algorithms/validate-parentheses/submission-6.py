class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
    
        for character in s:
            if len(stack)==0 and character in ")}]":
                return False
            if character in "({[":
                stack.append(character)

            elif character ==")":
                current_char=stack.pop()
                if current_char!="(":
                    return False
            elif character =="}":
                current_char=stack.pop()
                if current_char!="{":
                    return False
            elif character =="]":
                current_char=stack.pop()
                if current_char!="[":
                    return False
            print(stack)

        if len(stack)==0:
            return True
        else: 
            return False    


        