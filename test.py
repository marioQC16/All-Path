import requests
import sys

# Store input numbers
num1 = sys.argv[1]
num2 = sys.argv[2]

# Add two numbers
sum = float(num1) + float(num2)

# Display the sum
print('The shortest path from',num1, 'to', num2, 'is',sum)