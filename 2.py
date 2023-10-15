# string = input()
string = 'In the hole in the ground there lived a hobbit'

for i in range(len(string)):
    if i % 2 ==0:
        print(string[i], end='')
