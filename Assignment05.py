# Analysis of Algorithms (CSCI 323)
# Winter 2025
# Assignment 5 - Evaluating and Ranking Functions
# Brandon Marsh

# Acknowledgements:
# I worked with the class

import inspect
from math import log, factorial
import pandas as pd
import matplotlib.pyplot as plt



#[1] Define a function func_body() that obtains the content of a function, i.e. the part after the return statement.

def func_body(f):
   body = inspect.getsource(f)
   idx = body.index("return")
   return body[7 + idx:].strip()


def clean(s):
    return s.replace("**", "^").replace("*","").replace("fact(n)","n!").strip()

#[2] Define function f0 as the Identity Function, i.e. f(n) = n. Let f1 thru f10 be these functions from Rosen, Ch. 3, Slide 50. Add additional functions f11 etc. for experimental purposes.


def fact(n):
    return factorial(n)

def f0(n):
    return n


def f1(n):
    return 1.5**n


def f2(n):
    return 8*n**3+17*n**2+111


def f3(n):
    return log(n)**2


def f4(n):
    return 2**n


def f5(n):
    return log(log (n))


def f6(n):
    return n**2*log(n)**3


def f7(n):
    return 2**n*(n**2 + 1)

def f8(n):
    return n**3+n*log(n)**2


def f9(n):
    return 10000


def f10(n):
    return fact(n)


def f11(n):
    return n**2.7


def f12(n):
    return n**1.6


def f13(n):
    return n**2.81


#[3] Define a function evaluate_functions to evaluate a list of functions for a list of inputs. Because the range of inputs and outputs varies so greatly, you may be better off - for the purposes of the table and graph - by taking the log of the input and log of the output. See https://en.wikipedia.org/wiki/Log%E2%80%93log_plot


def func_desc(f):
    return f.__name__ + " "+clean(func_body(f))


def eval_functions(functions, sizes):
   dict_functions = {}
   for func in functions:
       dict_functions[func_desc(func)] = {}
   for size in sizes:
       for func in functions:
           dict_functions[func_desc(func)][size] = round(log(func(size),10),4)
   return dict_functions

#[4] Define a function print_values()  to print the dictionary as a table, with an option to sort the values in increasing order.

def print_values(dict_functions,filename,do_sort):
   pd.set_option("display.max_rows", 500)
   pd.set_option("display.max_columns", 500)
   pd.set_option("display.width", 1000)
   df = pd.DataFrame.from_dict(dict_functions).T
   if do_sort:
        df =df.sort_values(by=df.columns[2])
   print(df)
   with open(filename, "w") as f:
       f.write(df.to_string())


#[5] Define a function plot_values() to plot the dictionary as a bar-graph.

def plot_values(dict_functions, sizes, functions, xlabel, ylabel, file_name):
   func_num = 0
   plt.xticks([j for j in range(len(sizes))], [str(size) for size in sizes])
   for func in functions:
       func_num += 1
       d = dict_functions[func_desc(func)]
       x_axis = [j + 0.05 * func_num for j in range(len(sizes))]
       y_axis = [d[i] for i in sizes]
       plt.bar(x_axis, y_axis, width=0.05, alpha=0.75, label=func_desc(func))
   plt.legend()
   plt.title("Evaluation of Functions")
   plt.xlabel(xlabel)
   plt.ylabel(ylabel)
   plt.savefig(file_name)
   plt.show()




def main():
    assn = "Assignment05"
    sizes = [10,100,1000]
    functions = [f0,f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f11,f12,f13]
    dict_functions = eval_functions(functions, sizes)
    print_values(dict_functions, assn + ".txt", do_sort=False)
    plot_values(dict_functions, sizes, functions,xlabel="n",ylabel="f(n)", file_name=f"{assn}.png")
    print_values(dict_functions, assn + ".txt", do_sort=True)




if __name__ == "__main__":
    main()
