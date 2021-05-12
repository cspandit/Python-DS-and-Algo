# Problem is to find count of all the anagrams in a string


from collections import defaultdict


def count_anagrams(string, pattern, n):
    window_size = len(pattern)
    start = 0
    end = 0
    no_of_anagrams = 0
    d = defaultdict(int)
    for i in pattern:
        d[i] += 1

    count = len(d)
    while end < n:
        # doing calculation
        if string[end] in d:
            d[string[end]] -= 1
            if d[string[end]] == 0:
                count -= 1
        if end - start + 1 < window_size:
            end += 1

        elif end - start + 1 == window_size:
            # calculate answer
            if count == 0:
                no_of_anagrams += 1

            # slide_window
            if string[start] in d:
                d[string[start]] += 1
                if d[string[start]] == 1:
                    count += 1
            start += 1
            end += 1

    return no_of_anagrams


s = "geeksforgeekeegs"
pattern = "geek"
n = len(s)
print(count_anagrams(s, pattern, n))
