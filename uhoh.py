import csv
from time import perf_counter


def fact(n):
    if n>1:
        return fact(n-1) + fact(n-2)
    else:
        return 1
def fib_bad(n):
  if n > 1:
    return fib_bad(n-1) + fib_bad(n-2)
  else:
    return 1

#no look#
def fib_meh(n):
  a = 0
  b = 1
  print(a)
  if n >1:
    print(b)
    for i in range(n):
      c=a+b
      print(c)
      a=b
      b=c
#no look#

def mian():
    with open("/Users/dmartielli/Documents/PyCharm/for_coding_1.csv" , 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["input", "meh time", "bad time"])
        for i in range(34):
            exe_time = perf_counter()
            fib_val = fib_bad(i)
            exe_time_bad = perf_counter() - exe_time
            exe_time = perf_counter()
            fib_val = fib_meh(i)
            exe_time = perf_counter() - exe_time
            csvwriter.writerow([i, exe_time,exe_time_bad])



if __name__== "__main__":
    mian()

