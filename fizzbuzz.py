fizzbuzz = 0
count = True

while fizzbuzz <= 100:
  if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
    print "Fizz Buzz"
    fizzbuzz += 1
  elif fizzbuzz % 3 == 0:
    print "Fizz"
    fizzbuzz += 1
  elif fizzbuzz % 5 == 0:
    print "Buzz"
    fizzbuzz += 1
  else:
    print fizzbuzz
    fizzbuzz += 1
    

    

    