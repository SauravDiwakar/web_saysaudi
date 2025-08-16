import random 

def calculation(num):
  total = 0
  while num > 0:
    num, digit = divmod(num, 10)
    total += digit ** 2

  return total

def isHappy(n):
  container = set()
  while n != 1:
    if n in container:
      return False
    container.add(n)
    n = calculation(n) 

  return True


if __name__ == '__main__':
  number = random.randint(1, 1000001)
  if isHappy(number):
    print(f"{number} is Happy.")
  else:
    print(f"{number} is not Happy.")