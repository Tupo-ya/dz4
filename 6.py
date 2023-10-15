
# ! Тут вроде как надо текст выводить без скобок. А в примере написан текст В скобках

string = 'When he saw Sally (a girl he used to go to school with) in the shop, he could not believe his eyes. She was fantastic (as always)!'

new_string = ''
while True:
    skobka_x = string.find('(')
    if skobka_x == -1:
        break
    new_string += string[0:skobka_x]
    string = string[skobka_x:]
    string = string[string.find(')')+2:]

print(new_string)