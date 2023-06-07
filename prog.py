
import msvcrt
import inquirer
import random
import time



was = []
with open('save.data') as f:
    line = f.readline()
    string_list = line.split()
    was = [int(x) for x in string_list]




question = []
with open("input.txt", 'r') as f:
    for line in f.readlines():
        question.append(line.split(' '))

for i in range(len(question)):
    for j in range(len(question[i])):
        question[i][j] = question[i][j].rstrip('\n')


char = ''
num = int(input("how many questions???"))


if len(question) - len(was) == 0:
    was = []
    print('you completed all questions, history is reset')
elif len(question) - len(was) < num:
    num = len(question) - len(was)
    print(f'too many questions will be shown only {num}')



flag = False


while num > 0:
    ran = random.randint(0, len(question)-1)
    while ran in was:
        ran = random.randint(0, len(question)-1)
    while True:
        questions = [
            inquirer.List('answer',
                          message=question[ran][0],
                          choices=question[ran][1:-1],
                          ),
        ]
        answers = inquirer.prompt(questions)
        if answers['answer'] == question[ran][-1]:
            print("correct!!")
            was.append(ran)
            break
        else:
            print("incorect!!")
        while True:
            print("press r to retry, n - next")
            char = msvcrt.getch().decode('utf-8')
            print(char)
            if char == 'n':
                flag = True
                break
            if char == 'r':
                print("\033c", end='')
                break
        if flag:
            flag = False
            break
    if char != "n" or char != "r":
        time.sleep(1)
    print("\033c", end='')
    num -= 1


with open('save.data', 'w') as f:
    string_array = [str(x) for x in was]
    separator = ' '
    result_string = separator.join(string_array)
    f.write(result_string)    
