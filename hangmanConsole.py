import random
words = ["Yes","Python","Linux","Windows"]
ans = words[random.randint(0,len(words)-1)].lower()
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
guessState = ["x" for i in ans]
letters = []
win = False
def findSubarr(arr, subarr): #returns index
    for i in range (len(arr)):
        if arr[i] == arr[0]:
            for k in range(len(subarr)):
                while arr[i+k] == subarr[k]:
                    if k == len(subarr[k])-1:
                        return i
                
def printArr(arr):
    s = ""
    for i in arr:
        s += i
    print(s)               
print('Welcome to Hangman!')
while currState <= 7:
    print(hangman_states[currState],flush=True)
    printArr(guessState)
    userinput = input("Enter a letter or phrase to guess")
    if len(userinput) > 1:
        if userinput not in ans:
            print(f"Ha, you tried, but no, the phrase {userinput} is not in the word.")
        else:
            print(f"Oh wow, {userinput} is in the word surprisingly")
            index=findSubarr(ans,userinput)
            x=[ans[i] if i in range(index,index+len(userinput)) else guessState[i] for i in range(0,len(guessState)) ]
            guessState = x
            printArr(guessState)
            
    else:
        if userinput in ans:
            print(f"Yes, the letter {userinput} is in the word.")
            guessState = [ans[x] if ans[x] == userinput else guessState[x] for x in range(len(guessState))]