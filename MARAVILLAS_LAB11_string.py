WORDS = []
SORT_WORDS = []
for x in range(1, 11):
    USER_INPUT = str(input(f"Enter Word {x}: "))
    WORDS.append(USER_INPUT)

USER_INPUT = int(input("Enter a Number/Length: ")) 

for item in WORDS:
    if len(item) >= USER_INPUT:
        SORT_WORDS.append(item)
print(f"Display Words: {SORT_WORDS}")