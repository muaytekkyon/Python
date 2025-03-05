# Analysis of Algorithms (CSCI 323)
# Winter 2025
# Assignment 11 - "Estimate, Evaluate and Rank Recurrences"
# Brandon Marsh

# Acknowledgements:
# I worked with the class


import inspect
import texttable
import math
import Assignment02 as as2

# [1] Use this function to obtain the content of a function, i.e. the part after the return statement.
def func_body(f):
   body = inspect.getsource(f)  # gets the code
   idx = body.index("return")  # get the part after the word return
   return '"' + body[7 + idx:].strip() + '"'


# [2] Create an empty dictionary to store intermediate results and a helper function ff to efficiently run a function f for input n:

dict_funcs = {}
def ff(f, n):
    func_name = f.__name__
    if func_name not in dict_funcs:
        dict_funcs[func_name] = {}
    dict_func = dict_funcs[func_name]
    if n not in dict_func:
        dict_func[n] = f(f, n)
    return dict_func[n]


# [3] Define a sample function f1, like the one for MergeSort. Try to use the one-line if/else (aka "ternary expression") as it will make it easier to capture the function content in Task 1. Make sure that all quotients are converted to int.
# T(n) =2T(n/2) + n





# [4] Test the function by calling from your main function
def call_and_print(data, func, n):
    data.append([func.__name__, func_body, n, ff(func,n), math.log(ff(func, n), 10)])
    # print(func.__name__, func_body(func), "for n =", n, "is", ff(func, n))


def print_table(title, headers, alignments, data):
    table_obj = texttable.Texttable()
    table_obj.set_cols_align(alignments)
    table_obj.add_rows([headers] + data)
    print(title)
    print(table_obj.draw())
    print()

def main():
    assn = "Assignment11"
    data = []
    funcs = [f1_merge_sort, f2_factorial, f3_fibonacci,f4_karatsuba,f5_stooge,f6_bubble,f7_bigint_dnc,f8_linear,f9_dnc_matrix,f10_strassen]
    for func in funcs:
        for n in [10, 50, 100]:
            call_and_print(data,func, n)

    headers = ["Name", "Function", "n", "F(n)", "log F(n)"]
    alignments = ["l", "l,", "r", "r","r"]
    title = "Evaluation of Functions"
    print_table(title, headers, alignments, data)


    # [5] See all the intermediate values that were also computed by executing:
    for func in dict_funcs:
        print(func, dict_funcs[func])

    # [6] Once this works, create functions f2 thru f10 corresponding to nine more recurrences from the slides or old exams.
def f1_merge_sort(f, n):
    return 0 if n == 1 else 2 * ff(f, int(n/2)) + n
def f2_factorial(f, n):
    return 1 if n == 0 else n * ff(f,n-1)
def f3_fibonacci(f, n):
    return 0 if n == 0 else (1 if n == 1 else ff(f, n-1) + ff(f,n-2))
def f4_karatsuba(f,n):
    return 0 if n == 1 else 3 * ff(f, int(n/2)) + n
def f5_stooge(f,n):
    return 0 if n == 1 else 3 * ff(f, int(2*n/3)) + 1
def f6_bubble(f,n):
    return 0 if n == 1 else ff(f, int(n-1)) + n-1
def f7_bigint_dnc(f,n):
    return 0 if n == 1 else 4 * ff(f, int(n/2)) + n
def f8_linear(f,n):
    return 0 if n == 1 else ff(f, int(n-1)) + 1
def f9_dnc_matrix(f,n):
    return 0 if n == 1 else 8 * ff(f, int(n / 2)) + n ^ 2
def f10_strassen(f,n):
    return 0 if n == 1 else 7 * ff(f, int(n / 2)) + n ^ 2







    # algs = [native_search, brute_force,rabin_karp,knuth_morris_pratt,boyer_moore]
    # trials = 10
    # sizes = [10, 100, 1000, 10000, 100000, 1000000]




if __name__ == "__main__":
    main()