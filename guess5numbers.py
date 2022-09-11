# it's a nice number game

def check_number_of_equal_indexes(secret, guessed):
    calculator = 0
    for i in range(0, 5, 1):
        if secret[i] == guessed[i]:
            calculator += 1
        i += 1
    return calculator

def check_number_of_right_numbers(secret, guessed):
    calculator = 0
    for list_element in secret:
        if list_element in guessed:
            calculator += 1
    return calculator

def check_length_of_input(guessed):
    if len(guessed) == 5:
        return True
    else:
        return False

def check_if_only_numbers(guessed):
    if guessed.isnumeric() == True:
        return True
    else:
        return False

def main():
    from random import sample
    import os
    sequence = [i for i in range(10)]
    subset = sample(sequence, 5)

    print("*"*50)
    print("GUIDANCE")
    print(" ")
    print("Try to guess 5 right numbers using your logical head and reasoning.")
    print(" ")
    print("You get feedback about how many right numbers you guessed correctly on a right place")
    print("and how many numbers were overall correct in your guess.")
    print(" ")
    print(" ")
    print("EXAMPLE ")
    print("Give your guess: 14752  | 2/3")
    print("")
    print("Which means")
    print("Result: right numbers on right places / right numbers overall")
    print(" ")
    print("(when correct answer could be for example 14897)")
    print("")
    print("*"*50)

    guess = False
    print("Give your guess: ")
    while guess is False:
        guessed_numbers = input()
        os.system(" ")
        if check_length_of_input(guessed_numbers) == False or check_if_only_numbers(guessed_numbers) == False:
            print("Incorrect input, try again.")

        if check_length_of_input(guessed_numbers) == True and check_if_only_numbers(guessed_numbers) == True:
            guessed_list = list(map(int, str(guessed_numbers)))
            print(guessed_numbers," |" ,check_number_of_equal_indexes(subset,guessed_list),"/",check_number_of_right_numbers(subset,guessed_list))

            if check_number_of_right_numbers(subset, guessed_list) == 5 and \
                    check_number_of_equal_indexes(subset, guessed_list) == 5:
                guess = True
                print("You won because of your brilliant reasoning.")

main()
