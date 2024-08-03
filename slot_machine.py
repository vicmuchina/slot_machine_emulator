import random


MAX_NUMBER_OF_LINES = 3
MIN_BET = 1
MAX_BET = 1000

ROWS = 3
COLUMNS = 3

symbols = {
    "A" : 2,
    "B" : 4,
    "C" : 6,
    "D" : 8
}

symbol_values = {
    "A" : 6,
    "B" : 5,
    "C" : 4,
    "D" : 3

}
def spin():
    pass

def deposit():
    while True:
        amount = input("How much would you like to deposit? ")
        if amount.isdigit():         
            amount = int(amount)
            if amount > 0:
                print(f"Your balance is {amount}")
                break
            else:
                print("You must deposit a positive amount")

        else:
            print("Input a number")

    return amount

def get_number_of_lines():
    while True:
        lines = input(f"Please enter the number of lines you would like to play (1-{MAX_NUMBER_OF_LINES}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_NUMBER_OF_LINES :
                break
            else:
                print(f"The number of lines should be between 1 and {MAX_NUMBER_OF_LINES} ")
        else:
            print("Input a number")

    return lines

def get_bet():
    while True:
        amount = input("How much would you like to bet on each line? ")
        if amount.isdigit():         
            amount = int(amount)
            if  MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"You must bet a positive amount between {MIN_BET} and {MAX_BET} kenya shillings")

        else:
            print("Input a number")

    return amount

def get_slotmachine_spin(rows, columns, symbols):

    all_symbols = []

    for symbol,symbol_value in symbols.items():
        all_symbols += symbol * symbol_value

    cols = []
    for _ in range (columns):
        col = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            symbol = random.choice(current_symbols)
            current_symbols.remove(symbol)
            col.append(symbol)
        cols.append(col)    

    return cols

def print_slotmachine_reels(cols):

    for row in range(len(cols[0])):
        for i,col in enumerate(cols):
            if i != len(cols) - 1:
                print(col[row],end="|")
            else:
                print(col[row],end="")
        print()        
    
def check_winning_lines(columns,lines,bet,symbol_values):
    winnings = 0
    winning_lines = []
    for row in range(lines):
        symbol_to_check = columns[0][row]
        for col in columns:
            symbol_being_checked = col[row]
            if symbol_to_check != symbol_being_checked:
                break
        else:
            winnings += symbol_values[symbol_being_checked] * bet
            winning_lines.append(row + 1)
               
    return winnings,winning_lines

def spin(balance):
    lines = get_number_of_lines()
   
    while True:
        bet = get_bet()
        total_bet = lines * bet

        if  total_bet <= balance:
            break
        else:
            print(f"You do not have enough balance to make this bet,your balance is {balance} kenya shillings")

    print(f"you are betting {bet}ksh on  {lines} lines,Total bet is {total_bet} kenya shillings")

    random_columns = get_slotmachine_spin(ROWS, COLUMNS, symbols)

    print(random_columns)
    print_slotmachine_reels(random_columns)
    winnings, winning_lines = check_winning_lines(random_columns,lines,bet,symbol_values)

    print(f"You have won {winnings} ksh")
    print(f"you have won on lines", *winning_lines)

    return winnings - total_bet

def main():
    balance = deposit()

    while True:
        print(f"Your current balance is {balance}")
        answer = input("Press enter or any key to spin or q to quit ")

        if answer == "q":
            quit()
        else:

            balance += spin(balance)

main()