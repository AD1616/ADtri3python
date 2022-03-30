from math import sqrt

class Prime:
  def isPrime(self, n):
    if (n <= 1):
      return "No"
      #0 and 1 are not prime bumers
      
    for i in range(2, int(sqrt(n))+1):
      if (n % i == 0):
        return "No"
        # Finds in the range, sees if there is any divisible number
    return "Yes"
    # Returns yes if it can't find a divisibile  number

def test_prime():
  n = int(input("Enter a number for Prime Function: "))
  prime = Prime()
  print("Is it prime?", prime.isPrime(n))
  # Puts in these numbers to run the function