# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 17:07:00 2022

@author: jaime
"""

import random

  

def digits_and_tries():
    """
    Explanation
    -------------

    This funtion genereates the number of digits in the secret code and the number of tries the player will have to guess the code

    Parameters
    -------
    
    None

    Returns
    -------
    
    code_length : int
        Value of the length of the secret code.
    tries : int
        Value of the amount of tries the player will have to guess the code.

    Precondition
    -----------
    None

    Example
    -------
    In [1]: digits_and_tries()
    How many digits do you want the code to have? 4
    How many tries do you want to have? 10

    Out[1]: (4, 10)
    """
    code_length = int(input('How many digits do you want the code to have? '))
    tries = int(input('How many tries do you want to have? '))
    print()
    return code_length , tries

def codigo_secreto(code_length):
    """
    Explanation
    -------------

    This funtion genereates a secret code of a given length by generating numbers from 0 to 9 using random module and appedning them to a list 

    Parameters
    -------
    
    code_length: int
       Value of the amount of digits in the code
    

    Returns
    -------
    
    code: list

    Precondition
    -----------
    
    import random

    Example
    -------
    In[1]: codigo_secreto(6)
    Out[1]: [4, 8, 1, 2, 8, 7]
    """
    num_digit = 0
    code = []
    while num_digit < code_length:
        digit = random.randint(0, 9)
        code.append(digit)
        num_digit += 1
    print(f'Code in generator is {code}')
    print(f'Len(Code) in generator is {len(code)}')
    ans = str(code)
    return ans

def valida_tanteo(check, code_length):
    """
    Explanation
    -------------

    This funtion validates a guess of a given code by checking if the guess is purely numeric and has matching length.
       
    Parameters
    ---------

    check: string, tuple, or list
       Guess of what the secret code may be.
    code_length: int
       Length of the secret code

    Returns
    -------

    ans: bool
       True if the guess is valid, false otherwise

    Precondition
    -----------

    None 

    Example
    -------

    In[1]: valida_tanteo('1234', 4)
    Out[1]: True

    In[2]: valida_tanteo('12AB', 4)
    Out[2]: False

    In[3]: valida_tanteo('1234', 8)
    Out[3]: False
    
    """
    ans = check.isnumeric() and len(check) == code_length
    return ans

def aciertos_semiaciertos(code, guess):
    """
    Explanation
    -------------

    - This funtion compares a given code and a guess and returns the number of guesses (correct guessed digits in the correct position in the code) 
    and semiguesses (correct guessed digits but in the wrong position in the code)
       
    Parameters
    ---------

    code: string, tuple, or list
       A secret code
    check: string, tuple, or list
       The guess of what the secret code is

    Returns
    -------

    aciertos: int
       The number of correct gueses
    semiaciertos: int,
       The number of halfguesses

    Precondition
    -----------

    The input variables 'code' and 'check' are ment to be a string of numbers of equal length.
    However, the function works regardless of what the inputs are as long as they are a valid type.

    Example
    -------
    In[1]: aciertos_semiaciertos('2426', '2267')
    Out[1]: (1, 2)
    
    In[2]: aciertos_semiaciertos('2426', '2429')
    Out[2]: (3, 0)
    
    In[3]: aciertos_semiaciertos('2426', '2426')
    Out[3]: (4, 0)
            
    """
    print(f'Code in funtion is {code}')
    print(f'Len(code) in function is {len(code)}.')
    aciertos = 0
    semiaciertos = 0
    for i in range(len(code)):
        if guess[i] == code[i]:
            aciertos += 1
        elif code[i] in guess:
            semiaciertos += 1
    return aciertos, semiaciertos



def juega_humano():
    """
    Explanation
    -------------

    - This function is a version of the game Mastermind, however instead of pegs and colors is a secret code of a given length comprised of digits from 0 to 9 which can repeat themselves.
    The structure of the game is as follows:
        - Generate the number of digits of the code and tries.
        - Generate the secret code for the game.
        - Set a flag to false to make sure that game doesn't stop.
        - The user inputs their guess.
        - Checks if the input guess is valid or not.
        - Once every digit in the guess has looped, we change the amount of remaining tries.
        - Checks for a win or lose condition.
       
    Parameters
    ---------

    None

    Returns
    -------

    result: str
       Result of the game, that being a victory or a loss

    Precondition
    -----------

    The 'random' module must be imported before

    Example
    -------

            
    """
   
    print("Hello, welcome to Mastermind! This is a game where I think of a code and you have to guess it. Before we begin, let me ask you a few questions.\n")
    code_length , game_tries = digits_and_tries()   # Generate the number of digits of the code and tries
    print("Great, now that we've set the amount of digits in the code and the amount of tries we can begin.\n")
    
    
    game_code = (codigo_secreto(code_length))    # Generate the secret code for the game
    print(f'Code in game is {game_code}')
    print(f'Len(game_code) in game is {len(game_code)}.')
    
    flag_game_complete = False   # Set a flag to false to make sure that game doesn't stop
    
    while flag_game_complete == False:
        
        guess = (input("What's your guess?: "))    # The user inputs their guess
        
        if valida_tanteo(guess,code_length) == True:   # Checks if the input guess is valid or not
            aciertos , semiaciertos = aciertos_semiaciertos(game_code, guess)
            print(f' Juego: {aciertos}, {semiaciertos}')
            game_tries -= 1   # Once every digit in the guess has looped, we change the amount of remaining tries
            print (f'Guess: {aciertos}   Half-guess: {semiaciertos}   Remaining tries: {game_tries}\n')
            
            if aciertos == 4:   # Checks for a win condition
                flag_game_complete = True
                result = 'YOU WIN. You guessed the correct code!'
            
            elif game_tries == 0:   # Checks for a lose condition. Note: We check for a win condition first because if the user guesses the code on the 10th try it is still a win.
                flag_game_complete = True
                print(f'Correct answer: {game_code}')
                result = 'YOU LOSE. You ran out of tries. Better luck next time!'
        else:
            print (f'Please introduce a purely numeric guess of {code_length} characters')   # Indicates the playes that their input wasn't valid
    return (result)


