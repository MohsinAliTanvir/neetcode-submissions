class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for t in tokens:
            
            if t not in "+-*/":
                stack.append(t)
            else:
                val2=int(stack.pop())
                val1=int(stack.pop())
                # print(val1)
                # print(val2)
                if t=="*":
                    ans=val1*val2
                    stack.append(ans)
                if t=="+":
                    ans=val1+val2
                    stack.append(ans)
                if t=="-":
                    ans=val1-val2
                    stack.append(ans)
                if t=="/":
                    ans=val1/val2
                    stack.append(ans)
            # print(stack)
        return int(stack[0])

        