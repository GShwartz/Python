def get_questions(question):
    try:
        question = str(input("Enter your question: "))
        if len(question) == 0:
            raise ValueError

        elif question[0] == ' ':
            raise ValueError

    except ValueError:
        print(f"[!]Error! '{question}' is Invalid.")
        get_questions(question='')

    return question


def get_question_score(qs):
    while True:

        try:
            qs = int(input("Enter Question Score: "))
            if not float(qs):
                raise ValueError

            if qs + (sum(scores)) > 100:
                print(f"{qs+sum(scores)} > 100")
                raise ValueError

            break

        except ValueError:
            print("[!]Error! Numbers Only.")

    scores_local.append(qs)
    return True


def get_number_of_answers(num=None, minv=None, maxv=None):
    print(f"Debug | Number Of Answers: {number_of_answers}")

    print(f"\tMin={minv} | Max={maxv}")

    try:
        num = int(input(f"Number of Answers [{minv}-{maxv}]: "))
        if minv and minv > num:
            print(f"[!]Error! {num} < {minv}")
            raise ValueError

        if maxv and maxv < num:
            print(f"[!]Error! {num} > {maxv}")
            raise ValueError

        answers.append(num)
        return num

    except ValueError:
        print("[!]Input Not Valid")
        get_number_of_answers(num=0, minv=2, maxv=4)

        return num


def get_answers(num_of_answers, answer):

    try:
        for ans in range(1, num_of_answers+1):  # Start Index from 1.
            answer = input(f"Answer #{ans}: ")
            if len(answer) == 0:
                raise ValueError

            answers_local.append(answer)

    except ValueError:
        print("Error! No Input!")
        answers_local.clear()
        get_answers(num_of_answers, answer="")

    return answer


def get_right_answer_number(num, noa):
    print(f"Debug: num={num} | noa={noa}")

    while True:
        try:
            num = int(input("Type the Right Answer Number: "))
            if 0 < num < noa:
                answers.append(num)
                break

            else:
                raise ValueError

        except ValueError:
            print(f"Error! {num} Invalid. Try Again.")

    return True


def ask_if_sure(ans):   # Returns True

    ask_sure = input("Are you sure? [Y/n]: ")
    if ask_sure.lower() == "n":
        get_right_answer_number(num=0, noa=number_of_answers[0])

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

    question = get_questions(question)
    question_list.append(question)
    is_big = get_question_score(question_score)
    while is_big:
        print(f"Question score: {scores_local}, Total Score: {sum(scores)}, Valid: {is_big}")
        num_of_answers = get_number_of_answers(num=0, minv=2, maxv=4)
        multiple_answers = get_answers(num_of_answers, answer="")
        question = question_list[-1]
        right_answer_number_var = get_right_answer_number(num=0, noa=num_of_answers)
        is_right = get_right_answer_number(num_of_answers, right_answer_number_var)
        while is_right:
            print("Summery will replace this line.\n")
            sure = ask_if_sure(ans="")

            while sure:
                if number_of_answers < len(question_list):
                    lines = len(question_list)
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
    scores_local = []
    scores = []
    number_of_answers = [0]
    answers_local = []
    answers = []
    right_answer_number = []

    main(question="", question_score=0, num_of_answers=0)
