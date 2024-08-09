def are_parentheses_balanced(s):
    # Initialize an empty stack to keep track of opening brackets
    stack = []

    # Define strings containing all opening and closing brackets
    opening = "({["
    closing = ")}]"

    # Create a dictionary mapping each closing bracket to its corresponding opening bracket
    pairs = {")": "(", "}": "{", "]": "["}

    # Iterate through each character in the input string
    for char in s:
        # If the character is an opening bracket
        if char in opening:
            # Add it to the stack
            stack.append(char)
        # If the character is a closing bracket
        elif char in closing:
            # Check if the stack is empty OR
            # the last opening bracket doesn't match the current closing bracket
            if not stack or stack[-1] != pairs[char]:
                # If either condition is true, the brackets are not balanced
                return False
            # If the brackets match, remove the last opening bracket from the stack
            stack.pop()

    # After processing all characters, check if the stack is empty
    # If it's empty (length 0), all brackets were balanced, so return True
    # Otherwise, there are unmatched opening brackets, so return False
    return len(stack) == 0


# Example usage
print(are_parentheses_balanced("({[]})"))  # Should print: True
print(are_parentheses_balanced("([)]"))  # Should print: False
print(are_parentheses_balanced("(("))  # Should print: False
print(are_parentheses_balanced(""))  # Should print: True
