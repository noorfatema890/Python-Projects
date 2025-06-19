def valid(s):
    '''This function Checks if the input string 's' contains valid and properly nested parentheses'''
    try:
        tracker = []
        brackets = {')': '(', '}': '{', ']': '['}

        if not (1 <= len(s) <= 10**4):
            print("ⓘ Invalid Input length")
            return False
        
        allowed_chars = set("()[]{}")
        for char in s:
            if char not in allowed_chars:
                print("ⓘ Input should consist parentheses only")
                return False
        
        for char in s:
            print()
            print('Checking char = ', char)
            if char in brackets:
                if len(tracker) == 0:
                    print('\n------------------------------\n➤➤ String is not valid')
                    return False
                if tracker[-1] != brackets[char]:
                    print('\n------------------------------\n➤➤ String is not valid')
                    return False
                print('»»ᅳᅳᅳᅳ► Character matched')
                tracker.pop()
                print(f"tracker after pop: {tracker}")
            else:
                tracker.append(char)
                print('»»ᅳᅳᅳᅳ► adding to tracker')
                print(f"Tracker : {tracker}")
        
        if len(tracker) == 0:
            print('\n------------------------------')
            print('\n➤➤ String is valid')
            return True
        else:
            print('\n------------------------------')
            print('\n➤➤ String is not valid')
            return False
    
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")
        return False

inp_str = input('➤➤ Enter string: ')
print(valid(inp_str))
