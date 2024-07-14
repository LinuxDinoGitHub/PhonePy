import random
words = ["Yes","Python","Linux","Windows"]
ans = words[random.randint(0,len(words)-1)]
hangman_states = [
"""
+---+
|   |
|
|
|
|
=========
""",
"""
+---+
|   |
|   O
|
|
|
=========
""",
"""
+---+
|   |
|   O
|   |
|
|
=========
""",
"""
+---+
|   |
|   O
|  /|
|
|
=========
""",
"""
+---+
|   |
|   O
|  /|\
|
|
=========
""",
"""
+---+
|   |
|   O
|  /|\
|  /
|
=========
""",
"""
+---+
|   |
|   O
|  /|\
|  / \
|
=========
"""
]
#I used chatgpt to generate this

currState=0
print('Welcome to Hangman!')
while currState <= 7:
    print(hangman_states[currState],flush=True)
    userinput = input("Enter a letter or phrase to guesd")
    if len(userinput) > 1:
        #do stuff
