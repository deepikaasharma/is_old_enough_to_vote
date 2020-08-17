# Fill in the contents of the is_old_enough_to_vote function. This function takes in a number, called age, and returns whether a person of this age old enough to legally vote in the United States. If the person is old enough to vote, the functin should return True. If they are not old enugh to vote in the United States, the function should return False.

# Notes:

#     The legal voting age in the United States is 18

# output = is_old_enough_to_vote(22)
# print(output) # --> True

def is_old_enough_to_vote(age):
  if age>=18:
    return True
  else:
    return False
print(is_old_enough_to_vote(18))