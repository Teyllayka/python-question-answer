
import msvcrt
import inquirer
import random
import time
import json

with open('questions.json') as f:
    data = json.load(f)


was = []
with open('save.data') as f:
    line = f.readline()
    string_list = line.split()
    was = [int(x) for x in string_list]


num = int(input("how many questions???"))

if len(data) - len(was) < num:
    num = len(data) - len(was)
    print(f'too many questions will be shown only {num}')
elif len(data) - len(was) == 0:
    was = []
    print('you completed all questions, history is reset')



char = ''
flag = False
dns = False




while num > 0:
    ran = random.randint(0, len(data)-1)
    while ran in was:
        ran = random.randint(0, len(data)-1)
    while True:
        title = ""
        for y in data[ran]["title"]:
            title += y + "\n"
        print(data[ran]["category"])
        print(title)
        questions = [
            inquirer.List('answer',
                          #message=title,
                          message = " ",
                          choices=data[ran]['answers'],
                          ),
        ]
        answers = inquirer.prompt(questions)
        answer = ""
        for y in data[ran]["correctAnswer"]:
            answer += y
        if len(answer) != 0:
            if answers['answer'] == answer:
                print("correct!!")
                was.append(ran)
                break
            else:
                print("incorect!!")
        else:
            dns = True
            print("there is no correct answer")
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
    if dns:
        was.append(ran)
        dns = False
    print("\033c", end='')
    num -= 1

with open('save.data', 'w') as f:
    string_array = [str(x) for x in was]
    separator = ' '
    result_string = separator.join(string_array)
    f.write(result_string)
