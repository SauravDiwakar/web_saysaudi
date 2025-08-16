import matplotlib.pyplot as plt

def collatz(num):
  if (type(num) is not int) or (num < 1):
    print(num)
    raise ValueError("Input can be only positve integer.")

  seq = [num]
  while num != 1:
    if num%2 == 0:
      num //= 2
    else:
      num = (3*num)+1
      
    seq.append(num)

  return len(seq)


def visualize(data):
    x_values = list(data.keys())
    y_values = list(data.values())

    plt.figure(figsize=(15, 5))
    plt.plot(x_values, y_values, marker='o', linestyle='-', color='b')

    plt.xlabel("Number")
    plt.ylabel("Steps")
    plt.title("Number vs Steps")

    plt.grid(True)
    plt.show()

    return True

num_step_map = {}
try:
  for n in range(1, 101):
    list_len = collatz(n)
    num_step_map[n] = list_len

  visualize(num_step_map)

except ValueError as e:
  print(e)

