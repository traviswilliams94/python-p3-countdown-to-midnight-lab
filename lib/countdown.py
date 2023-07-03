from time import sleep

def countdown(i):
    while i:
        print(f'{i} SECOND(S)!')
        i -= 1
    print("HAPPY NEW YEAR!")

def countdown_with_sleep(i):
    while i:
        print(f'{i} SECOND(S)!')
        i -= 1
        sleep(1)
    print("HAPPY NEW YEAR!")