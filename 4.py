import itertools

def solve_crypt_arithmetic(equation):
    """
    Solve a crypt-arithmetic equation.
    
    :param equation: A string representing the equation to solve, e.g., "SEND + MORE = MONEY"
    :return: A dictionary mapping letters to digits if a solution is found, else None
    """
    words = equation.replace(' ', '').split('=')
    left_side = words[0].split('+')
    right_side = words[1]
    
    unique_chars = set(''.join(left_side + [right_side]))
    if len(unique_chars) > 10:
        return None  # More unique characters than digits
    
    first_letters = set(word[0] for word in left_side + [right_side])
    
    for perm in itertools.permutations(range(10), len(unique_chars)):
        char_to_digit = dict(zip(unique_chars, perm))
        
        if any(char_to_digit[char] == 0 for char in first_letters):
            continue
        
        left_sum = sum(int(''.join(str(char_to_digit[char]) for char in word)) for word in left_side)
        right_value = int(''.join(str(char_to_digit[char]) for char in right_side))
        
        if left_sum == right_value:
            return char_to_digit
    
    return None


equation = "SEND + MORE = MONEY"
solution = solve_crypt_arithmetic(equation)

if solution:
    print(f"Solution for {equation}:")
    for char, digit in solution.items():
        print(f"{char}: {digit}")
else:
    print(f"No solution found for {equation}")
