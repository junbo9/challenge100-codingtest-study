
N = int(input())
2
​
3
numbers = []
4
​
5
for _ in range(N) : 
6
    numbers.append(int(input()))
7
for i in range(len(numbers)) : 
8
    for j in range(len(numbers)) : 
9
        if numbers[i] < numbers[j] : 
10
            numbers[i], numbers[j] = numbers[j], numbers[i]
11
            
12
for n in numbers : 
13
    print(n)
