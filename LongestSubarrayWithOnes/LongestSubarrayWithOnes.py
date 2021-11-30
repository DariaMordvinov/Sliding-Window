def length_of_longest_substring(arr, k):
    # Creates an array of size 2: index 0 for storing zeros, index 1 for storing ones
    counters = [0, 0]

    start, longest = 0, 0

    # Iterating through array
    for end in range(len(arr)):
        # Counts every zero or every one we encounter
        counters[arr[end]] += 1

        # Checks if we already have more zeroes than we can replace
        if counters[0] > k:
            # Slides the window by one
            counters[arr[start]] -= 1
            start += 1

        # Remembers the longest subarray
        longest = max(longest, end - start + 1)

    return longest


Array = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
k = 2
print(length_of_longest_substring(Array, k))