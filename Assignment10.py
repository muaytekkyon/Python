# Analysis of Algorithms (CSCI 323)
# Winter 2025
# Assignment 10 - "String Search Algorithms"
# Brandon Marsh

# Acknowledgements:
# I worked with the class


import Assignment02 as as2
from time import time
from random import randint,choices
import texttable

# [1] Define functions that implement these sub-string search algorithms:
# Native Search that wraps the built-in string-search capability of your programming language
# Brute Force - see https://www.geeksforgeeks.org/naive-algorithm-for-pattern-searching/
# Rabin-Karp - see https://www.geeksforgeeks.org/rabin-karp-algorithm-for-pattern-searching
# Rabin-Karp Randomized - (use multiple hash functions with random moduli)
# Knuth-Morris-Pratt - see https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching
# Boyer-Moore - see https://www.geeksforgeeks.org/boyer-moore-algorithm-for-pattern-searching


def random_string(size, alphabet):
    return ''.join(choices(alphabet, k= size))

def native_search(text, m, pattern, n, verbose=False):
    try:
        return text.index(pattern)
    except ValueError:
        return -1


def brute_force(text, m, pattern, n, verbose=False):
    for i in range(m - n + 1):
        j = 0
        while j < n and text[i + j] == pattern[j]:
            j += 1
        if j == n:
            return i
    return -1


def rabin_karp(txt,N,pat,M,verbose=False):
    d =256
    q=101
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0
    t = 0
    h = 1
    for i in range(M - 1):
        h = (h * d) % q
    for i in range(M):
        p = (d * p + ord(pat[i])) % q
        t = (d * t + ord(txt[i])) % q
    for i in range(N - M + 1):
        if p == t:
            for j in range(M):
                if txt[i + j] != pat[j]:
                    break
                else:
                    j += 1
            if j == M:
                print("Pattern found at index " + str(i))
        if i < N - M:
            t = (d * (t - ord(txt[i]) * h) + ord(txt[i + M])) % q
            if t < 0:
                t = t + q
    return -1


def constructLps(pat, lps):
    len_ = 0
    m = len(pat)
    lps[0] = 0
    i = 1
    while i < m:
        if pat[i] == pat[len_]:
            len_ += 1
            lps[i] = len_
            i += 1
        else:
            if len_ != 0:
                len_ = lps[len_ - 1]
            else:
                lps[i] = 0
                i += 1


def knuth_morris_pratt(txt,n,pat,m,verbose=False):
    lps = [0] * m
    constructLps(pat, lps)
    i = 0
    j = 0
    while i < n:
        if txt[i] == pat[j]:
            i += 1
            j += 1
            if j == m:
                return i - j
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


def badCharHeuristic(string, size):
    NO_OF_CHARS = 256
    badChar = [-1] * NO_OF_CHARS
    for i in range(size):
        badChar[ord(string[i])] = i
    return badChar


def boyer_moore(txt,n, pat,m,verbose=False):
    badChar = badCharHeuristic(pat, m)
    s = 0
    while (s <= n - m):
        j = m - 1
        while j >= 0 and pat[j] == txt[s + j]:
            j -= 1
        if j < 0:
            return s
            s += (m - badChar[ord(txt[s + m])] if s + m < n else 1)
        else:
            s += max(1, j - badChar[ord(txt[s + j])])


def run_algs(algs, sizes, trials):
    dict_algs = {}
    data = []
    for alg in algs:
        dict_algs[alg.__name__] = {}
    for size in sizes:
        for alg in algs:
            dict_algs[alg.__name__][size] = 0
        for trial in range(1, trials + 1):
            n = 10
            m = size
            text = random_string(size, alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ")
            idx = randint(0, size - n)
            pattern = text[idx:idx + n]
            for alg in algs:
                start_time = time()
                idx_found = alg(text,m,pattern,n, False)
                end_time = time()
                net_time = end_time - start_time
                dict_algs[alg.__name__][size] += 1000 * net_time
                data.append([alg.__name__, m, n, pattern, idx_found, net_time])
    return dict_algs, data


def print_table(title, headers, alignments, data):
    table_obj = texttable.Texttable()
    table_obj.set_cols_align(alignments)
    table_obj.add_rows([headers] + data)
    print(title)
    print(table_obj.draw())
    print()

def main():
    assn = "Assignment10"
    headers = ["Algorithm", "Len text", "Len pattern", "pattern","idx_found", "time"]
    alignments = ["l","r,","r","l","r","r"]
    title = "String Search Results"
    algs = [native_search, brute_force,rabin_karp,knuth_morris_pratt,boyer_moore]
    trials = 10
    sizes = [10, 100, 1000, 10000, 100000, 1000000]
    dict_algs, data = run_algs(algs, sizes, trials)
    as2.print_times(dict_algs, f"{assn}.txt")
    as2.plot_times(dict_algs, sizes, trials, algs, f"{assn}.png")
    print_table(title, headers, alignments, data)


if __name__ == "__main__":
    main()