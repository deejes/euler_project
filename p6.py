"""The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum"""

sum_square = 0
for x in range(1,101):
    print (x)
    sum_square += (x **2)

square_sum = 0

for x in range(1,101):
    square_sum += x

print (sum_square - (square_sum ** 2))
