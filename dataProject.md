{% include navigation.html %}

{% include navig.html %}

# Data Structures Project

### Replit embed below. May need to change the run function in .replit.

{% include replit.html %}

* <a href="https://ad1616.github.io/ADtri3python/week0">Week 0</a>
* <a href="https://ad1616.github.io/ADtri3python/week1">Week 1</a>

# Week 2

## Snippets

### Organization Screenshots

![image](https://user-images.githubusercontent.com/64157584/160328272-edb68876-9e89-4bbe-9b07-f11c1a0a77ff.png)

![image](https://user-images.githubusercontent.com/64157584/160328319-b1b7a6ef-b527-4e42-9cc2-81073350e923.png)

![image](https://user-images.githubusercontent.com/64157584/160328365-0a8a2d0f-1c5b-4ff2-91a5-061565428893.png)


### Factorial Function with Classes


```python
class Factorial:
  def __init__(self):
      # Intially have 1 since in factorial you multiply by 1 at the end
      self.facNum = 1
  def __call__(self, n):
    if n < self.facNum:
      return self.facNum
    else:
      # At first, it is n * self(n-1)
      # Then, self(n-1) calls the function again, and it will have value (n-1) * self(n-2)
      # This keeps going until the n-1 argument in self is less than 1, which will then then return 1 for self(0)
      # The result is n * (n-1) * (n-2) * (n-3) ... * 1 which is factorial
      facAnswer = n * self(n-1) 
    return facAnswer

def tester():
  # Create instance of factorial object
  fac_of = Factorial() 
  try: 
    x = int(input("What is the number you want to take factorial of? "))
    print(fac_of(x)) 
  except:
    print("Enter an integer")
```


### My own math function: Prime Factors. OOP code


```python
import math

class PrimeFactor:
    def __init__(self):
      # Object of prime factor class will initially have empty list for prime factors and factors
      self.factors = []
      self.prime = []
    def __call__(self, n):
      # Iterate through all possible factors, and add the successful candidates to the list
      for i in range (1, int(math.floor(n/2) + 1)):
        if (n % i == 0):
          self.factors.append(i)
      # Iterate through the factors and check if each one is prime
      for factor in self.factors:
        # Count used for prime testing, set to 0
        count = 0
        for i in range(2, (factor // 2 + 1)):
            if (factor % i == 0):
                # If it does have factors, count is increased by 1
                count = count + 1
                break
        #If count ever changed from 0, then the factor was not a prime number
        #If it didn't, and the number isn't one, then we add it to the prime factors list
        if (count == 0 and factor != 1):
          self.prime.append(factor)
      # If there were no prime factors, meaning the number itself is prime, then we only have none in the list
      if (len(self.prime) == 0):
        self.prime.append("none")
      return self.prime


def tester():
  factors12 = PrimeFactor() 
  print("12's prime factors: " + str(factors12(12))) # Should output 2 and 3
  factors5 = PrimeFactor()
  print("5's prime factors: " + str(factors5(5))) # Should output none
```


### Prime Factors in Imperative form


```python
import math

def primeFactors(num):
  # Empty lists that will store factors and prime factors
  factors = []
  primeFactors = []
  # This loop generates all factors of the number
  for i in range (1, int(math.floor(num/2) + 1)):
    if (num % i == 0):
      factors.append(i)
  # From the determined factors, this code will check which are prime
  # First loop iterates through all the factors
  for factor in factors:
    # Count used for prime testing, set to 0
    count = 0
    # This loop is used to check if the factor itself has any factors
    for i in range(2, (factor // 2 + 1)):
        if (factor % i == 0):
            # If it does have factors, count is increased by 1
            count = count + 1
            break
    #If count ever changed from 0, then the factor was not a prime number
    #If it didn't, and the number isn't one, then we add it to the prime factors list
    if (count == 0 and factor != 1):
      primeFactors.append(factor)
  # If there were no prime factors, meaning the number itself is prime, then we only have none in the list
  if (len(primeFactors) == 0):
    primeFactors.append("none")
  return primeFactors


def tester():
  print("12's prime factors: " + str(primeFactors(12))) # Should output 2 and 3
  print("5's prime factors: " + str(primeFactors(5))) # Should output none
```


### Palindrome Code


```python
import re
import math

class Palindrome: 
  def __init__(self):
    # Intializing result to true; will change if it is not palindrome
    self.result = True
  # object attribute "thing" is what is being tested by the class
  def __call__(self, thing):
    # Again setting self.result to true so that it resets after each call
    self.result = True
    # Converting to string for indexing purposes
    thing = str(thing)
    # Saving original to be displayed later
    original = "\"" + thing + "\""
    # Manipulating thing so that there are no special characters or uppercase letters
    thing = re.sub('\W+','', thing)
    thing = thing.lower()
    # Iterating through the characters checking if the first one matches the last one
    for i in range(0, math.floor(len(thing)/2)):
      if thing[i] != thing[-(i+1)]:
        # If the corresponding characters don't match, then result is set to false
        self.result = False
        break
    # If the loop never set result to false, then it is palindrome
    if self.result == True:
      return (str(original) + " is a palindrome")
      
    if self.result == False:
      return (str(original) + " is not a palindrome")

def tester():
  test = Palindrome() # Instantiating an object of palindrome class
  print(test("A man, a plan, a canal -- Panama!")) # Is palindrome
  print(test("1! heh#heh    !1")) # Is palindrome
  print(test("hello")) # Is not palindrome
  print(test(12321)) # Is palindrome
  print(test(12221)) # Is palindrome
  print(test(12314)) # Is not palindrome
```


## Github Links


[Factorial Issue](https://github.com/AD1616/ADtri3python/issues/10)

[Own Math Function Issue](https://github.com/AD1616/ADtri3python/issues/11)

[Palindrome Issue](https://github.com/AD1616/ADtri3python/issues/12)


## Replit links

[Updated Menu](https://replit.com/@AD1616/ADtri3python#pythonStuff/menu.py)
