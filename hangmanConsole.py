from random_word import RandomWords
win=0
lose=0
while True:
    r = RandomWords()
    ans = r.get_random_word()
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
    guessState = ["X" for i in ans]
    letters = []
    def line():
        print("-"*30)
    def findSubarr(arr, subarr): #returns index
        for i in range (len(arr)):
            if arr[i] == arr[0]:
                for k in range(len(subarr)):
                    while arr[i+k] == subarr[k]:
                        if k == len(subarr[k])-1:
                            return i
    def enter():
        input("Press Enter to continue... ")
    def printArr(arr):
        s = ""
        for i in arr:
            s += i
        print(s)
    print(10*"\n")               
    print('Welcome to Hangman!')
    line()
    while currState <= 6:
        print(hangman_states[currState],flush=True)
        print("Word:")
        printArr(guessState)
        print("Letters guessed: ",letters)
        userinput = input(">>Enter a letter or phrase to guess: ")
        if userinput in letters:
            print("You have already guessed this letter/phrase.")
            enter()
            continue
        if len(userinput) > 1:
            if userinput not in ans:
                print(f"Ha, you tried, but no, the phrase {userinput} is not in the word.")
                currState+=1
                enter()
            else:
                print(f"Oh wow, {userinput} is in the word surprisingly")
                index=findSubarr(ans,userinput)
                x=[ans[i] if i in range(index,index+len(userinput)) else guessState[i] for i in range(0,len(guessState)) ]
                guessState = x
                printArr(guessState)
                enter()
        else:
            if userinput in ans:
                print(f"Yes, the letter {userinput} is in the word.")
                guessState = [ans[x] if ans[x] == userinput else guessState[x] for x in range(len(guessState))]
                enter()
            else:
                 print("Unfortunately, that is not in the word...")
                 currState+=1
                 enter()
        letters.append(userinput)
        guessString=''
        line()
        for x in guessState:
            guessString += x
        if guessString == ans:
            print("YOU WIN! The word was ",ans)
            win+=1
        elif currState >= 7:
            print("You lost...")
            print("The word was ",ans)
            lose+=1
        print(f"Times won: {win}   Times lost: {lose}")
        if input("Do you want to play again? (y/n)") != "y":
            print("Thanks for playing!")
            exit()