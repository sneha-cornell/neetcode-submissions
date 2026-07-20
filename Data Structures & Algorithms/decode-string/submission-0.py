class Solution:
    def decodeString(self, s: str) -> str:
        #k can be multi digit?
        stack=[] #track both current string and current number 
        curr_string = ""
        curr_number =0

        for c in s: 
            if c.isdigit():
                curr_number = curr_number*10 +int(c)
            elif c=='[':
                stack.append((curr_string,curr_number))
                curr_string=""
                curr_number=0
            elif c==']':
                prev_string, prev_number = stack.pop()
                curr_string=prev_string+curr_string*prev_number
            else: 
                curr_string+=c
        return curr_string 
