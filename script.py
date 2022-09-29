from stack import Stack

print("\nLet's play Towers of Hanoi!!")

# Define the towers
stacks = []
left_stack = Stack('left')
middle_stack = Stack('middle')
right_stack = Stack('right')
stacks.append(left_stack)
stacks.append(middle_stack)
stacks.append(right_stack)

# Set up the size of the game
num_disks = int(input('\nHow many disks do you want to play with?\n'))
while num_disks < 3:
  num_disks = int(input('Enter a number greater than or equal to 3.\n'))
while num_disks > 1000:
  num_disks = int(input('Enter a number less than or equal to 1000.\n'))
        
# Show optimal number of moves
for i in range(num_disks, 0, -1):
  left_stack.push(i)
num_optimal_moves = 2 ** num_disks - 1
print('\n The fastest you can solve this game is in {} moves.'.format(num_optimal_moves))

# Define a function for user to select moves 
def get_input():
  choices = [stack.get_name()[0] for stack in stacks]
  while True:
    for i in range(len(stacks)):
      name = stacks[i].get_name()
      letter = choices[i]
      print('Enter {} for {}'.format(letter, name))
    user_input = input('')
    if user_input in choices:
      for i in range(len(stacks)):
        if user_input == choices[i]:
          return stacks[i]

# Play the game
num_user_moves = 0
while right_stack.get_size() != num_disks:
  print('\n\n\n...Current Stacks...')
  for stack in stacks:
    stack.print_items()
  while True:
    print('\nWhich stack do you want to move from?\n')
    from_stack = get_input()
    print('\nWhich stack to you want to move to?\n')
    to_stack = get_input()
    if from_stack.is_empty():
      print('\n\nInvalid Move. Try Again.')
    elif to_stack.is_empty() or from_stack.peek() < to_stack.peek():
      disk = from_stack.pop()
      to_stack.push(disk)
      num_user_moves += 1
      break 
    else:
      print('\n\nInvalid Move. Try Again.')

# End the game
print('\n\nYou completed the game in {} moves, and the optimal number of moves is {}.'.format(num_user_moves, num_optimal_moves))
if num_user_moves == num_optimal_moves:
  print('Amazing! You played a perfect game :)')
