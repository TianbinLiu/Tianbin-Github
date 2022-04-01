# menuy.py - function style menu
# Imports typically listed at top
# each import enables us to use logic that has been abstracted to other files and folders
from TT0 import matrix, swap, tree, ship
from TT1 import gamelist, fibonacci
from TT2 import factor, fibonacci_class, advy, prime, palindrome

# Menu list of [Prompts, Actions]
# Two styles are supported to execute abstracted logic
# 1. "filename.py" will be run by exec(open("filename.py").read())
# 2. file.function references will be executed as file.function()
data_menu = [
    ["Matrix", matrix.matrix],
    ["Swap", swap.swap],
    ["Tree", tree.tree],
    ["Ship", ship.ship],
    ["Game List", gamelist.gamelist],
]

math_menu = [
    ["Factors", factor.factors],
    ["GCD", factor.gcd],
    ["LCM", factor.lcm],
    ["Primes", prime.primes],
    ["Fibonacci", fibonacci.fibonacci],
    ["Fibonacci Class", fibonacci_class.fclass],
    ["Palindrome", palindrome.paltest]
]

adventure_menu = [
    ["At the Beach?", advy.beach],
    ["On top of the Mountains?", advy.mountain],
    ["Navigating a lake?", advy.lake]
]


def menu(title, options):
    # header for menu
    # Menu banner
    border = "=" * 25
    banner = f"\n{border}\n{title}\n{border}"
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    except TypeError:
        print(f"Not callable {action}")
    # end validation try

    menu(title, options)  # recursion, start menu over again


# def math_menu
# using sub menu list above:
# sub_menu works similarly to menu()
def _data_menu():
    title = "Data SubMenu"
    menu(title, data_menu)


# def math_menu
# using sub menu list above:
# sub_menu works similarly to menu()
def _math_menu():
    title = "Math SubMenu"
    menu(title, math_menu)


# def adventure menu
# using sub menu list above:
# sub_menu works similarly to menu()
def _adventure_menu():
    title = "Adventure SubMenu"
    menu(title, adventure_menu)


def driver():
    title = "Main Menu"
    menu_list = [["Data (Matrix, Ship, Swap, Tree, Gamelist)", _data_menu],
                 ["Math (Factors, GCD, LCM, Prime, Fibonacci, Fibonacci_Class, Palindrome, )", _math_menu],
                 ["Adventure (Beach, Mountains, Lake)", _adventure_menu]]
    menu(title, menu_list)


if __name__ == "__main__":
    driver()
