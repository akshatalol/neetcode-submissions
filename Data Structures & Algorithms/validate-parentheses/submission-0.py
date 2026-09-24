class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        hmap = {")": "(", "]": "[", "}": "{"}
        for i in s:
            if i in hmap: #only checking closing brackets as keys!
                if stack and stack[-1]==hmap[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i) #opening brackets
        return len(stack)==0

