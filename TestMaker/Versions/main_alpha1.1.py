def get_questions():

    question = input("Enter your question: ")
    if len(question) == 0:
        print("No Empty Questions.")
        get_questions()

    question_list.append(question)

    return question


def get_question_score(s):

    try:
        s = int(input("Enter Question Score: "))

    except ValueError:
        print("[!]Error! Use numbers.")
        return 0

    return s


def check_sum(s):

    try:
        if sum(scores) + s > 100:
            print("Score sum is higher than 100")
            print(f"{100 - sum(scores)} left")
            score = 0
            if len(scores) != 0:
                scores.pop()
            return False

    except ValueError:
        scores_local.clear()
        print("Use Numbers.")
        return False

    scores_local.append(s)
    scores.append(s)

    return True


def get_number_of_answers(num=None, minv=None, maxv=None):

    print(f"minv={minv}\t maxv={maxv}")
    print(number_of_answers)

    try:
        num = int(input(f"Number of Answers [{minv}-{maxv}]: "))
        if minv and minv > num:
            print(f"{num} < {minv}")
            number_of_answers.clear()
            raise ValueError

        if maxv and maxv < num:
            print(f"{num} > {maxv}")
            number_of_answers.clear()
            raise ValueError

        number_of_answers.append(num)

        return num

    except ValueError:
        print("Input Not Valid")
        number_of_answers.clear()
        get_number_of_answers(num=0, minv=2, maxv=4)

    if len(number_of_answers) != 0:
        number_of_answers.clear()
        number_of_answers.append(num)

    return num


def big_small(n_o_a):

    number_of_answers.clear()

    if n_o_a < 2 or n_o_a > 4:
        number_of_answers.clear()
        return False

    else:

        number_of_answers.append(n_o_a)

        return True


def get_answers(num_of_answers, answer):

    for ans in range(number_of_answers[0]):
        answer = input(f"Answer #{ans+1}: ")    # Start indexing from 1
        if len(answer) == 0:
            print("Error! No Input!")
            get_answers(num_of_answers, answer="")

        answers_local.append(answer)
        answers.append(answer)

    return answer


def get_right_answer_number(num):

    try:
        num = int(input("Type the Right Answer Number: "))

    except ValueError:
        print("Error! Please type numbers only.")

    return num


def check_right_answer_number(num):

    if 0 < num <= number_of_answers[0]:
        return True

    else:
        return False


def ask_if_sure(ans):   # Returns True

    ask_sure = input("Are you sure? [Y/n]: ")
    if ask_sure.lower() == "n":
        number_of_answers.clear()
        check_right_answer_number(num=number_of_answers[0])

    elif ask_sure.lower() == "y":
        return True

    else:
        print("Error! Please type [Y/n]")
        ask_if_sure(ans="")


def ask_continue():

    a_continue = input("Do you wish to add more questions? [Y/n]: ")
    if a_continue.lower() == "y":
        return True

    elif a_continue.lower() == "n":
        return False

    else:
        print("Error! Please choose [Y/N]")
        ask_continue()


def restart():

    answers_local.clear()
    number_of_answers.clear()
    right_answer_number.clear()
    scores_local.clear()
    main(question="", question_score=0, num_of_answers=0)


def finish(lines):
    question_list_dup = []
    answers_dup = []
    scores_dup = []

    print("\n\n==============RESULTS==============\n")
    print("#\t Question\t Answer\t\t Score")
    number_of_questions = len(question_list)
    for num in range(number_of_questions):
        print(f"{num+1}\t {question_list[num]}\t\t {answers[num]}\t {scores[num]}")


def main(question, question_score, num_of_answers):

    questions = get_questions()
    question_score = get_question_score(s=0)
    if question_score == 0:
        scores.pop()
        scores_local.pop()
        question_score = get_question_score(s=0)

    score_sum = check_sum(question_score)   # Returns True/False
    num_of_answers = get_number_of_answers(num=0, minv=2, maxv=4)
    print("FIN")
    print(num_of_answers)
    print(f"Question score: {question_score}, Total Score: {sum(scores)}, Valid: {score_sum}")

    question_score = 0
    question = questions[-1]
    multiple_answers = get_answers(num_of_answers, answer="")
    right_answer_number_var = get_right_answer_number(num=0)
    answers_local.clear()
    is_right = check_right_answer_number(right_answer_number_var)

    if not is_right:
        print(f"Error! Please select [1={number_of_answers[0]}")
        right_answer_number_var = get_right_answer_number(num=0)

    while is_right:
        print("Summery will replace this line.\n")
        sure = ask_if_sure(ans="")

        while sure:
            if number_of_answers[0] < len(questions):
                lines = len(questions)
            else:
                lines = number_of_answers[0]

            answers.append(right_answer_number_var)
            ask_if_continue = ask_continue()
            if not ask_if_continue:
                finish(lines)

            while ask_if_continue:
                restart()
                break
            break
        break


if __name__ == "__main__":

    question_list = []
    scores = []
    scores_local = []
    number_of_answers = [0]
    answers = []
    answers_local = []
    right_answer_number = []

    main(question="", question_score=0, num_of_answers=0)
