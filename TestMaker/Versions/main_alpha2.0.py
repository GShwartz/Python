def get_questions(question):
    while True:

        try:
            question = str(input("Enter your question: "))
            if len(question) == 0:
                raise ValueError

            elif question[0] == ' ':
                raise ValueError

            break

        except ValueError:
            print(f"[!]Error! '{question}' is Invalid.")

    question_list.append(question)
    return question


def get_question_score(qs):
    while True:
        try:
            qs = int(input("Enter Question Score: "))
            if not float(qs):
                raise ValueError

            elif qs + (sum(scores)) > 100:
                print(f"{qs + sum(scores)} > 100")
                raise ValueError
            break

        except ValueError:
            scores_local.clear()
            print(f"[!]Error! Invalid Input. Try Again.")

    scores_local.append(qs)
    scores.append(qs)
    return True


def get_number_of_answers(num=None, minv=None, maxv=None):
    print(f"\tMin={minv} | Max={maxv}")
    while True:
        try:
            num = int(input(f"Number of Answers [{minv}-{maxv}]: "))
            if minv and minv > num:
                print(f"[!]Error! {num} < {minv}")
                raise ValueError

            if maxv and maxv < num:
                print(f"[!]Error! {num} > {maxv}")
                raise ValueError

            answers_local.append(num)
            answers_local.pop(0)
            break

        except ValueError:
            print("[!]Input Not Valid")

    return num


def get_answers(num_of_answers, answer):

    try:
        for ans in range(1, num_of_answers+1):  # Start Index from 1.
            answer = input(f"Answer #{ans}: ")
            if len(answer) == 0:
                raise ValueError

            if answer[0] == ' ':
                raise ValueError

            answers_local.append(answer)

    except ValueError:
        print("Error! No Input!")
        get_answers(num_of_answers, answer="")

    number_of_answers[0] = num_of_answers
    return answer


def get_right_answer_number(num, is_right=False):
    while True:
        try:
            num = int(input("[?]Right Answer #: "))
            if not float(num):
                raise ValueError

            if 0 < num <= number_of_answers[0]:
                is_right = True
                break
            else:
                raise ValueError

        except ValueError:
            print("[!]Error! Invalid Input.")

    right_answer_number[0] = num
    return is_right


def ask_if_sure(ans):
    while True:
        ask_sure = input("Are you sure? [Y/n]: ")
        if ask_sure.lower() == "n":
            get_right_answer_number(num=len(answers_local))

        elif ask_sure.lower() == "y":
            break

        else:
            print("Error! Please type [Y/n]")
            ask_if_sure(ans="")

    answers.append(right_answer_number[0])
    return True


def ask_continue():
    while True:

        a_continue = input("Do you wish to add more questions? [Y/n]: ")
        if a_continue.lower() == "y":
            break

        elif a_continue.lower() == "n":
            return False

        else:
            print("Error! Please choose [Y/n]")

    return True


def restart():

    answers_local.clear()
    right_answer_number[0] = 0
    scores_local.clear()
    main(question="", question_score=0, num_of_answers=0)


def finish():
    print("\n\n==============RESULTS==============\n")
    print("#\t Question\t Answer\t\t Score")
    number_of_questions = len(question_list)
    for num in range(number_of_questions):
        print(f"{num+1}\t {question_list[num]}\t\t\t {answers[num]}\t\t\t {scores[num]}")


def main(question, question_score, num_of_answers):

    question = get_questions(question)
    question = question_list[-1]
    is_big = get_question_score(question_score)
    while is_big:
        num_of_answers = get_number_of_answers(num=0, minv=2, maxv=4)
        multiple_answers = get_answers(num_of_answers, answer="")
        is_right = get_right_answer_number(num=0)
        print("\n****     Summery     ****")
        print(f"Number Of Questions: {len(question_list)}")
        print(f"Question: {question_list[-1]}\nAnswers: {answers_local}\nRight Answer: {right_answer_number[0]}")
        print(f"Question score: {scores_local} | Total Score: {sum(scores)}"
              f" | Valid: {is_big} | Left: {100 - sum(scores)}")
        while is_right:
            sure = ask_if_sure(ans="")
            while sure:
                ask_if_continue = ask_continue()
                if not ask_if_continue:
                    finish()

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
    right_answer_number = [0]

    main(question="", question_score=0, num_of_answers=0)
