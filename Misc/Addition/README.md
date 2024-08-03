# Addition

## Description

My little brother is learning math, can you show him how to do some addition problems?

<code>nc 24.199.110.35 42189</code>

## Attachments

[server.py](attachments/server.py)

## Solution

- The attachment is the source code that runs when we connect to the provided <code>nc</code>
interface. We are given a number of basic addition problems to solve. The number of problems that we
have to solve is determined by us, as when we initially connect to the interface, we are prompted to
input the number of questions we wish to solve.

- After solving all of the addition problems, the flag is read by the program. However, only the first
<code>n</code> characters of the flag are revealed, where <code>n</code> is the number of questions
we chose to answer. Obviously, if we want to see the whole flag, we would need to answer a large
number of questions. However, after solving each problem, the script is instructed to wait 2^i
seconds before proceeding to the next problem, where <code>i</code> is the number of questions
answered so far. The wait time quickly becomes ridiculous as it literally exponentially increases.

- It didn't seem like the intended solution was to actually spend forever solving addition
problems. If we look again at the end of the source code, this is the line that specifically prints
the flag fragment, where <code>questions</code> is an integer representing the number of questions
we chose to answer:
```
print(flag[:questions])
```
- In Python, we can index through iterables using **negative numbers**, which start from the end
of the iterable. So, I provided -1 as the number of questions I wished to solve. This entirely skipped
the addition problems and immediately revealed the entire flag, as -1 corresponds to the last index
of the flag.

## Flag

n00bz{m4th_15nt_4ll_4b0ut_3qu4t10n5}
