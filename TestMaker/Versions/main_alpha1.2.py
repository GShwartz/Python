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
        if not float(s):
            raise ValueError

    except ValueError:
        print("[!]Error! Numbers Only.")
        if len(scores) != 0:
            scores.pop()
        get_question_score(s=0)

    return s


def check_sum(s):

    try:
        if (sum(scores) + s) > 100:
            raise ValueError

    except ValueError:
        print(f"[!]Error! {(sum(scores) + s)} > 100")
        print(f"{100 - sum(scores)} left")
        if len(scores) != 0:
            scores.pop()

        return False

    scores.append(s)
    return True


def get_number_of_answers(num=None, minv=None, maxv=None):

    print(f"Number Of Answers: {number_of_answers}")

    print(f"\tMin={minv} | Max={maxv}")

    try:
        num = int(input(f"Number of Answers [{minv}-{maxv}]: "))
        if minv and minv > num:
            print(f"[!]Error! {num} < {minv}")
            raise ValueError

        if maxv and maxv < num:
            print(f"[!]Error! {num} > {maxv}")
            raise ValueError

        return num

    except ValueError:
        print("[!]Input Not Valid")
        get_number_of_answers(num=0, minv=2, maxv=4)

    return int(num)


def get_answers(num_of_answers, answer):

    for ans in range(1, num_of_answers+1):  # Start Index from 1.
        answer = input(f"Answer #{ans}: ")
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

    if 0 < num <= number_of_answers:
        return True

    else:
        return False


def ask_if_sure(ans):   # Returns True

    ask_sure = input("Are you sure? [Y/n]: ")
    if ask_sure.lower() == "n":
        check_right_answer_number(num=number_of_answers)

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
    while score_sum:
        print(f"Question score: {question_score}, Total Score: {sum(scores)}, Valid: {score_sum}")
        num_of_answers = get_number_of_answers(num=0, minv=2, maxv=4)
        multiple_answers = get_answers(num_of_answers, answer="")
        question = questions[-1]
        right_answer_number_var = get_right_answer_number(num=0)
        answers_local.clear()
        is_right = check_right_answer_number(right_answer_number_var)

        if not is_right:
            print(f"Error! Please select 1-{number_of_answers}")
            right_answer_number_var = get_right_answer_number(num=0)

        while is_right:
            print("Summery will replace this line.\n")
            sure = ask_if_sure(ans="")

            while sure:
                if number_of_answers < len(questions):
                    lines = len(questions)
                else:
                    lines = number_of_answers

                answers.append(right_answer_number_var)
                ask_if_continue = ask_continue()
                if not ask_if_continue:
                    finish(lines)

                while ask_if_continue:
                    restart()
                    break
                break
            break
        break


if __name__ == "__main__":

    question_list = []
    scores = []
    scores_local = []
    number_of_answers = 0
    answers = []
    answers_local = []
    right_answer_number = []

    main(question="", question_score=0, num_of_answers=0)
