import csv
from time import perf_counter
import random
from random import shuffle
from matplotlib import pyplot as plt
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
  d=[0]
  if n >1:
    d.append(b)
    for i in range(n):
      c=a+b
      d.append(c)
      a=b
      b=c
  return d
#no look#


aa = []
for i in range(10):
    aa.append(random.randint(1,9))
def dostuff():
    runtime = perf_counter()
    aa.sort()
    runtime = perf_counter() - runtime
    print(runtime)
    shuffle(aa)

def mian():
    with open("/Users/dmartielli/Documents/Stuff/PyCharm/for_coding_1.csv" , 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(["input", "meh time", "bad time"])
        ok = []
        nokay = []
        for i in range(34):
            exe_time = perf_counter()
            fib_val = fib_bad(i)
            exe_time_bad = perf_counter() - exe_time
            nokay.append(exe_time_bad)
            exe_time = perf_counter()
            fib_val = fib_meh(i)
            exe_time = perf_counter() - exe_time
            ok.append(exe_time)
            csvwriter.writerow([i, exe_time,exe_time_bad])
        plt.plot(nokay)
        plt.plot(ok)
        plt.show()
    dostuff()




if __name__== "__main__":
    mian()


