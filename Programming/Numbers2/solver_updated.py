import nclib
import math

conn = nclib.Netcat(connect="challs.n00bzunit3d.xyz:10258")

# "Borrowed" from the top response on this Stack Overflow post
# https://stackoverflow.com/questions/15347174/python-finding-prime-factors
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
  
  # Split the question into list to get the numbers
  question_list = question[:(len(question) - 3)].split()
  
  if "greatest prime factor" in question:
    num = int(question_list[-1])
    ans = largest_prime_factor(num)
    conn.send_line(str(ans).encode())
  elif "greatest common divisor" in question:
    num1 = int(question_list[-1])
    num2 = int(question_list[-3])
    ans = math.gcd(num1, num2)
    conn.send_line(str(ans).encode())
  elif "least common multiple" in question:
    num1 = int(question_list[-1])
    num2 = int(question_list[-3])
    ans = math.lcm(num1, num2)
    conn.send_line(str(ans).encode())
  elif "flag" in question:
    break