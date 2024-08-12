
class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        o_b = {"(","{","["}
        c_b = {")","}","]"}

        for char in s:
            if char in o_b:
                stack.append(char)
            elif char in c_b:
                if not stack:
                    return False

                top_element = stack.pop()

                if (char == ")" and top_element != "(") or \
                   (char == "}" and top_element != "{") or \
                   (char == "]" and top_element != "["):
                    return False
        return not stack

    




