#Famous FizzBuzz Coding challenge
for i in range(1, 101):
  if i % 15 == 0:
    #multiple of 3 and 5, FizzBuzz
    print("FizzBuzz")
  elif i % 5 == 0:
    #Multiple of 5, not 3, Buzz
    print("Buzz")
  elif i % 3 == 0:
    #Multiple of 3, not 5, Fizz
    print("Fizz")
  else:
    #None of the above, print the number i
    print(i)