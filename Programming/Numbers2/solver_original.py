import nclib
import math

conn = nclib.Netcat(connect="challs.n00bzunit3d.xyz:10258")

def largest_prime_factor(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

while True:
  question = str(conn.recv())
  print(question)
  if "greatest prime factor" in question:
    # Split the question
    question_list = question[:(len(question) - 3)].split()
    num = int(question_list[-1])
    ans = largest_prime_factor(num)
    conn.send_line(str(ans).encode())
  elif "greatest common divisor" in question:
    # Split the question
    question_list = question[:(len(question) - 3)].split()
    num1 = int(question_list[-1])
    num2 = int(question_list[-3])
    ans = math.gcd(num1, num2)
    conn.send_line(str(ans).encode())
  elif "least common multiple" in question:
    # Split the question
    question_list = question[:(len(question) - 3)].split()
    num1 = int(question_list[-1])
    num2 = int(question_list[-3])
    ans = math.lcm(num1, num2)
    conn.send_line(str(ans).encode())
  elif "flag" in question:
    break