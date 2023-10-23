# Program to display the Fibonacci sequence up to n-th term

def generate_fibonacci(nterms):
   # first two terms
   n1, n2 = 0, 1
   count = 0
   fibonacci_sequence = []

   # check if the number of terms is valid
   if nterms <= 0:
       return "Please enter a positive integer"
   elif nterms == 1:
       return [n1]
   else:
       while count < nterms:
           fibonacci_sequence.append(n1)
           nth = n1 + n2
           # update values
           n1 = n2
           n2 = nth
           count += 1
       return fibonacci_sequence

# Get the number of terms from the user
nterms = int(input("How many terms? "))
result = generate_fibonacci(nterms)
print("Fibonacci sequence:")

if isinstance(result, str):
   print(result)
else:
   print(result)

