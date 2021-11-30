def find_substring(str, pattern):
    answer = ""
    current = ""
    start, matched = 0, 0

    # Making dictionary for the pattern
    pattern_dict = {}
    for i in pattern:
        if i not in pattern_dict:
            pattern_dict[i] = 0
        pattern_dict[i] += 1

    # Iterates through the string
    for end in range(len(str)):
        char = str[end]
        current += char

        # Checks if we found all the chars of one kind from the pattern
        if char in pattern_dict:
            pattern_dict[char] -= 1
            if pattern_dict[char] >= 0:
                matched += 1

            # If we found all the characters, remember the substring and then shrink it (slide the window)
            while matched == len(pattern):
                if len(current) < len(answer) or len(answer) == 0:
                    answer = current
                current = current[1:]
                if str[start] in pattern_dict:
                    if pattern_dict[str[start]] == 0:
                        matched -= 1
                    pattern_dict[str[start]] += 1
                start += 1

    return answer

String="aa"
Pattern="aa"

print(find_substring(String, Pattern))