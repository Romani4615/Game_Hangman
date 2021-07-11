#word trying to guess
secretword = "paypaycutie".lower()
guessed = ""
failurecount = 7

#loop till player fails out
#will break if succeeded
while failurecount > 0:
    #get guess input from player
    guess = input('Enter a letter')
    
    if guess in secretword:
        print('CORRECT!!!')
   #if incorrect, subtract a letter from the failure count     
    else:
        failurecount -= 1
        print(f'incorrect there is no {guess} bitch you now have {failurecount} guesses left')
    #maintain a list of all letters guessed
    guessed = guessed + guess
    wronglettercount = 0
    for letter in secretword:
        if letter in guessed:
            print(f'{letter}', end="")
        else:
            print("_", end="")
            wronglettercount += 1
            
    #if there's no wrong letters, then they win!!!
    if wronglettercount == 0:
        print("you win my dud")
        break
    
else:
    print('sry loser')
