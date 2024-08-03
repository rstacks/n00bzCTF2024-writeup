ASCII_CODE_FOR_a = 97

og_string = "abcdefghij"
shuffled_string = "edhiafcbgj"

winner_string = ""
for i in range(len(og_string)):
  # Figure out where the OG character ended up
  placement_index = shuffled_string.index(og_string[i])

  # Figure out what letter SHOULD have been there
  correct_letter = chr(placement_index + ASCII_CODE_FOR_a)

  # Add that letter to the winner_string
  winner_string += correct_letter

print(winner_string)
