# Numbers 2

## Description

Let's see if you can do more than just counting... (Part 1 was in n00bzCTF 2023:
https://github.com/n00bzUnit3d/n00bzCTF2023-OfficalWriteups/tree/master/Misc/Numbers). There are no
attachments. Note: There are only 3 different types of questions.

<code>nc challs.n00bzunit3d.xyz 10258</code>

## Solution

- I started by manually connecting to the <code>nc</code> interface to get an understanding
of the task. In order to get the flag, we need to solve 100 math problems. These problems ask
for the greatest prime factor, the greatest common divisor, or the least common multiple of a given
number(s). We only have a few seconds to answer each question, so using a script seems to be the
intended solution.

- I solved this challenge less than 5 minutes before the CTF ended (!), so my solve script was not
as polished as I usually try to make them. You can view the script I actually used to retrieve the
flag [here](solver_original.py), or you can view a lightly modified script [here](solver_updated.py).
The modified script works the same way as the original script, but it's just been cleaned up
and simplified for easier reading.

- I used [nclib](https://nclib.readthedocs.io/en/latest/) to connect to the <code>nc</code>
interface. My script would read a problem from the interface, then search for keywords to match
it to one of the 3 question types mentioned above. Then, the number(s) would be extracted, and the
operation would be performed.

- I used Python's built-in <code>math</code> module to solve the greatest common divisor and
least common multiple problems (using <code>math.gcd()</code> and <code>math.lcm()</code>
respectively). For the greatest prime factor problems, I found a function on Stack Overflow that
did exactly that, so I "borrowed" (stole) it and used it in my script. Here is the thread that I
got this function from (check the top response):
https://stackoverflow.com/questions/15347174/python-finding-prime-factors

- Once the script was written, all I had to do was let it run in order to get the flag.

## Flag

n00bz{numb3r5_4r3_fun_7f3d4a_5b7b05832c22}
