
import msvcrt
import inquirer
import random
import time

question = []
with open("input.txt", 'r') as f:
    for line in f.readlines():
        question.append(line.split(' '))

for i in range(len(question)):
    for j in range(len(question[i])):
        question[i][j] = question[i][j].rstrip('\n')

was = []

char = ''
num = int(input("how many questions???"))

flag = False


while len(was) < num:
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
    was.append(ran)
