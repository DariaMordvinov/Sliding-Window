def find_string_anagrams(str, pattern):
    result_indexes = []

    # Makes dictionary for the pattern
    pattern_hash = {}
    for i in pattern:
        if i not in pattern_hash:
            pattern_hash[i] = 0
        pattern_hash[i] += 1

    anagram = {}
    start = 0

    # Iterates through the giving string
    for end in range(len(str)):

        # Checks if the character is in the pattern
        if str[end] in pattern_hash:
            if str[end] not in anagram:
                anagram[str[end]] = 0
            anagram[str[end]] += 1

            # Slide the window if we already have more characters then required
            while anagram[str[end]] > pattern_hash[str[end]]:
                anagram[str[start]] -= 1
                if anagram[str[start]] == 0:
                    del anagram[str[start]]
                start += 1

            # Check if we found the anagram
            if anagram == pattern_hash:
                result_indexes.append(start)
                anagram[str[start]] -= 1
                if anagram[str[start]] == 0:
                    del anagram[str[start]]
                start += 1

        # Change the starting position if we encountered character not from the pattern
        else:
            anagram = {}
            start = end + 1

    return result_indexes


String = "cbaebabacd"
Pattern = "abc"
print(find_string_anagrams(String, Pattern))