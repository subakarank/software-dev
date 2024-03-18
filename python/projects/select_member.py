import random
import time 
members = [
    'Manick',
    'Karthick',
    'Gowtham',
    'Srinivas',
    'Yuvraj',
    'Suba'
]

def get_member() -> str:
    random_number = random.randint(0, 5)
    return members[random_number]

print("members")
print(members)
print('--------------------------------------------------------------')
print('I am ready to select the member from your list')
is_ready = input('Are you ready? type Y or N \n')

if(is_ready.lower() == 'y'):
    print('scanning now...')
    for member in members:
        print(member, '.......', end="")
    time.sleep(10)
    member = get_member()
    print()
    print("I have chosen the member")
    is_reveal = input("Can I reveal the member now? Type Y or N \n")
    if(is_reveal.lower() == 'y'):
        print(f"selected member is {member}")
    else: 
        print("Good bye!")
        exit()
else: 
    print("Good bye!")
    exit()