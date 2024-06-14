#Project Euler Problems 
#Problem 1 

#define max and sum
max_numbers = 1000 
total_sum = 0

#create loop through numbers 
for x in range(1, max_numbers):
    if x % 3 == 0 or x % 5 == 0: 
        total_sum += x 

print(total_sum)

#Problem 2 

#define parameters 
x = 0 
a = 1 
fib = []

while x < 4000000: 
    fib.append(x)
    x, a = a, x + a
    print(fib)
    


    
