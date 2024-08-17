

def data_types_series():
    user_answers = []
    print("""Q-1: Which of the following is an immutable data type in Python?
          a) List
          b) Dictionary
          c) Tuple
          d) Set
          """)
    
    ans = input("Enter your ans (a/b/c/d): ")
    print(f"{ans=}")
    correct_ans = ans.lower() == 'c'
    user_answers.append(correct_ans)

    print("""Q-2: Which of these is a mutable data type?
          a) String
          b) Tuple
          c) List
          d) Integer
          """)
    ans = input("Enter your ans (a/b/c/d): ")
    print(f"{ans=}")
    correct_ans = ans.lower() == 'c'
    user_answers.append(correct_ans)

    print("""Q-3: Which of the following data types is not a sequence in Python?
          a) String
          b) List
          c) Tuple
          d) Set
          """)
    ans = input("Enter your ans (a/b/c/d): ")
    print(f"{ans=}")
    correct_ans = ans.lower() == 'd'
    user_answers.append(correct_ans)

    correct_percent = sum(user_answers) / 3 * 100

    if correct_percent > 50:
        print(f"You are passed with {correct_percent:.2f}% score.")
    else:
        print(f"You are failed and score is {correct_percent:.2f}%. Please try again...")



if __name__ == '__main__':
    data_types_series()