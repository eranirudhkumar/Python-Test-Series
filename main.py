
test_list = """
Select the test topic:
1 Data Types
2 Control Flow
3 Functions
4 Exit
"""


def load_test():
    while True:
        print(test_list)
        test_choice = input()
        print("User choice:", test_choice)

        if test_choice == '1':
            print("Data Types Test has been started: total time is 5 mins")
        
        elif test_choice == '4':
            print("You logged out successfully.")
            break

        else:
            print("Incorrect choice, pls try again...")


if __name__ == '__main__':
    load_test()