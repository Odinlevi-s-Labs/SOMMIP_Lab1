import os
import time
from Ls import ls
from Calc import calc


timer = 0
loading = "Loading: [----------]"

while timer < 11:
    os.system('cls')
    print(loading)
    loading = loading.replace("-","=",1)
    time.sleep(1)
    timer += 1
time.sleep(1)
os.system('cls')
print(loading+" Complete!")
print("Instructions you might want to use: ls, calc.\n To exit use 'exit'.")

inp = ""


while True:
    inp = input(">>> ")

    if inp == "exit":
        break

    if inp == "calc":
        calc()
    elif inp == "ls":
        ls()
    else:
        print("Unexpected expression.")
