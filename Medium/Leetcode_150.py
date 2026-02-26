class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        s = []

        for t in tokens:
            # find numbers
            if t not in ('-', '+', '*', '/'):
                #push numbers to the stack s
                s.append(int(t))

            else: # it's an operator
                a = s.pop()
                b = s.pop()

                if t == '-':
                    s.append(b - a)

                elif t == '+':
                    s.append(b+a)

                elif t == '*':
                    s.append(b*a)

                else:
                    s.append(int(float(b)/ a))
                
        return s[0]