import nclib

# Initial boundaries for guess
min_num = 0
max_num = pow(10, 100)

# Open connection to provided interface
conn = nclib.Netcat(connect="24.199.110.35:41199")

while True:
  # Determine guess and send
  guess = (max_num + min_num) // 2
  conn.send_line(str(guess).encode())

  # Determine boundaries for next guess
  feedback = str(conn.recv())
  print(feedback)
  if "small" in feedback:
    min_num = guess
  elif "large" in feedback:
    max_num = guess
  else:
    break

conn.close()
