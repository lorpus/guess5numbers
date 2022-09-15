from random import sample
from os import system, name


msg = " \n" \
      "Try to guess 5 right numbers using your" \
      " \n" \
      "logical head and reasoning." \
      " \n" \
      " \n" \
      "You get feedback about how many right " \
      " \n" \
      "numbers you guessed correctly on " \
      " \n" \
      "the right place and how many numbers " \
      " \n" \
      "were overall correct in your guess." \
      " \n" \
      " \n" \
      "  EXAMPLE \n" \
      " \n" \
      "  Give your first guess: " \
      " \n" \
      "  14752  | 2 / 3" \
      " \n" \
      " \n" \
      " \n" \
      "  2 / 3 is the result of your first" \
      " \n " \
      " guess and it means: " \
      " \n" \
      " \n" \
      "  2 right numbers on right places " \
      " \n " \
      " 3 right numbers overall" \
      " \n" \
      " \n" \
      "  (for this the correct answer " \
      " \n" \
      "   could be 14897) \n" \
      " \n" \
      " \n" \
      " \n" \
      " Press q if you want to give up :(\n" \

def print_intro_box(msg, indent=1, width=None, title=None):
    lines = msg.split('\n')
    space = " " * indent
    if not width:
        width = max(map(len, lines))
    box = f'╔{"═" * (width + indent * 2)}╗\n'  # upper_border
    if title:
        box += f'║{space}{title:<{width}}{space}║\n'  # title
        box += f'║{space}{"-" * (len(title)):<{(width)}}{space}║\n'  # underscore
    box += ''.join([f'║{space}{line:<{width}}{space}║\n' for line in lines])
    box += f'╚{"═" * (width + indent * 2)}╝'  # lower_border
    print(box)

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

# clear might work on linux but right now cannot get it to work on windows
def clear():
   # for windows
   if name == 'nt':
        _ = system('cls')

   # for mac and linux
   else:
        _ = system('clear')


def main():
    print_intro_box(msg=msg, indent=1, title='guess5numbers')
    sequence = [i for i in range(10)]
    subset = sample(sequence, 5)

    new_guess_result = []
    all_guesses_results = []

    guess = False
    print("Give your first guess: ")

    while guess is False:
        guessed_numbers = input()

        # if player quits
        if guessed_numbers == "q" or guessed_numbers == "Q":
            print("Okay, next time you are gonna make it.")
            print("The right number was")
            for list_element in subset:
                print(list_element, end=", ")
                print("\b\b", end=" ")
            quit()

        # in case of weird input
        if check_length_of_input(guessed_numbers) == False or check_if_only_numbers(guessed_numbers) == False:
            print("Weird guess, try again please.")

        # generating results of the guess for the user
        if check_length_of_input(guessed_numbers) == True and check_if_only_numbers(guessed_numbers) == True:

            guessed_list = list(map(int, str(guessed_numbers)))
            result_1 = check_number_of_equal_indexes(subset, guessed_list)
            result_2 = check_number_of_right_numbers(subset, guessed_list)


            new_guess_result.append(guessed_numbers)
            new_guess_result.append(result_1)
            new_guess_result.append(result_2)
            all_guesses_results.append(new_guess_result)

            i = 0
            for element in all_guesses_results:
                print(element[i], "   │" ,element[i+1], "/", element[i+2])
                i += 3

            if check_number_of_right_numbers(subset, guessed_list) == 5 and \
                    check_number_of_equal_indexes(subset, guessed_list) == 5:
                guess = True
                print("You won because of your brilliant reasoning.")
                how_many_guesses = len(all_guesses_results)
                print("       And you guessed only", how_many_guesses, "times, goood job!!")
        #clear()

main()
