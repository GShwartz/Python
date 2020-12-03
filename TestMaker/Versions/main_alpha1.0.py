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

    return s


def check_sum(s):

    scores_local.clear()

    try:
        if sum(scores) + s > 100:
            print("Score sum is higher than 100")
            print(f"{100 - sum(scores)} left")
            score = 0
            if len(scores) != 0:
                scores.pop()
            return False

    except ValueError:
        print("Use Numbers.")

    scores_local.append(s)
    scores.append(s)

    return True


def get_number_of_answers(n_o_a):

    try:
        n_o_a = int(input("Number of answers (Max 4)? "))

    except ValueError:
        print("Please select [2-4]")

    number_of_answers.append(n_o_a)

    return n_o_a


def big_small(n_o_a):

    if n_o_a < 2 or n_o_a > 4:
        print("Please select [2-4]")
        answers.clear()
        answers_local.clear()
        big_small(n_o_a=number_of_answers[0])
        return False

    elif 2 > number_of_answers[0] > 4:
        print("Error! Please select [2-4]")
        return False

    else:
        return True


def get_answers(num_of_answers, answer):

    for ans in range(number_of_answers[0]):
        answer = input(f"Answer #{ans+1}: ")    # Start indexing from 1
        if len(answer) == 0:
            print("Error! No Input!")
            get_answers(num_of_answers, answer="")

        answers_local_dictionary[ans+1] = answer
        answers_local.append(answer)
        answers.append(answer)
        answers_dict[ans+1] = answer

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
    answers_local_dictionary.clear()
    answers_dict.clear()
    number_of_answers.clear()
    right_answer_number.clear()
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
    score_sum = check_sum(question_score)   # Returns True/False
    num_of_answers = get_number_of_answers(n_o_a=0)
    is_bigger = big_small(num_of_answers)   # Returns True/False

    if not is_bigger:
        print(f"Question score: {question_score}, Valid: {score_sum}")
        if sum(scores) != 0:
            scores.pop()
            question_score = get_question_score(s=0)

    while is_bigger:

        question = questions[-1]
        multiple_answers = get_answers(num_of_answers, answer="")
        right_answer_number_var = get_right_answer_number(num=0)
        answers_local.clear()
        is_right = check_right_answer_number(right_answer_number_var)

        if not is_right:
            print(f"Error! Please select [1={number_of_answers[0]}")
            right_answer_number_var = get_right_answer_number(num=0)

        while is_right:
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
        break


if __name__ == "__main__":

    question_list = []
    scores = []
    scores_local = []
    number_of_answers = []
    answers = []
    answers_local = []
    answers_local_dictionary = {}
    right_answer_number = []

    answers_dict = {}

    main(question="", question_score=0, num_of_answers=0)
