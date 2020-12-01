def get_question(q):
    """
    Get question from user.
    """

    q = input(f"Question #{len(questions) + 1}: ")
    questions.append(q)

    return q


def get_score():
    """
    Get question's score from user and validate int.
    """
    global score

    try:
        score = int(input("Enter Question Score: "))

    except ValueError:
        print("[!]Error! Use numbers.")
        get_score()

    return score


def check_score_sum():
    global score

    try:
        if sum(scores, score) > 100:
            print("Score sum is higher than 100")
            print(score, scores)
            score = 0
            scores.pop()
            return False

    except ValueError:
        print("Use Numbers.")

    scores.append(score)

    return True


def num_answers_is_int():
    """
    Get number of answers to the question from the user.
    Validate number of answers is INT.
    """

    num_of_answers = 0

    try:
        num_of_answers = int(input("Number of answers (Max 4)? "))

    except ValueError:
        print("Please select [2-4]")

    return num_of_answers


def big_small(num_of_ans):
    """
    Validate user input is bigger than 2 and smaller or equal to 4 (Max number of answers).
    """
    try:

        if num_of_ans < 2 or num_of_ans > 4:
            print("Please select [2-4]")
            question_answers_global.clear()
            answers_local.clear()
            big_small(num_of_ans=0)

    except num_of_ans < 2 or num_of_ans > 4:
        print("Error! Please select [2-4]")

    return num_of_ans


def get_answers(num_of_ans, answer):
    """
    Validate user input is not empty.
    Returns number of answers to the question.
    """

    dict_answers_local.clear()
    number_of_answers.clear()
    # answers_local.append("")   # Filling index 0

    for ans in range(num_of_ans):
        answer = input(f"Answer #{ans+1}: ")    # Question's number begins with 1 instead of 0.
        if len(answer) == 0:
            print("No empty answers_num.")
            number_of_answers.clear()
            answers_local.clear()
            get_answers(num_of_ans)

        number_of_answers.append(num_of_ans)
        dict_answers_local[ans+1] = answer
        answers_local.append(answer)

    print("\n===================")
    print(f"Question: {questions[-1]}")
    print(f"Number Of Answers: {number_of_answers[0]}")
    print(f"Answers: {dict_answers_local}")
    print(f"Score: {score}")
    print("===================")

    return num_of_ans, answer


def right_answer_is_int(r_a):

    try:
        r_a = int(input("Type The Right Answer #: "))

    except ValueError:
        print("Value Error!")

    return r_a


def get_right_answer_num(r_a, lines):

    print(f"Your choice: {r_a}")

    if 0 < r_a <= number_of_answers[0]:
        sure = input("Are you sure? [Y/n]: ")
        if sure.lower() == "n":
            dict_answers_local.clear()
            get_right_answer_num(r_a, lines)

        elif sure.lower() == "y":
            if number_of_answers[0] < len(questions):
                lines = len(questions)
            dict_answers_local[1] = answers_local[0]

        else:
            print("Please Select [Y/n]")
            dict_answers_local.clear()
            get_right_answer_num(r_a, lines)

    else:
        print(f"Please select 1-{number_of_answers[0]}")
        get_right_answer_num(r_a, lines)

    return r_a


def finish(num_of_ans, right_answer_number, question, score, lines):

    ask_continue = input("Do you wish to add more questions? [Y/n]: ")
    if ask_continue.lower() == "y":
        dict_answers_local.clear()
        number_of_answers.clear()
        main(num_of_ans=0, right_answer_number=0, question="", score=0)

    elif ask_continue.lower() == "n":
        print(lines)
        print("\n\n==============RESULTS==============\n")
        print("#\t Question\t Answer\t\t Score")
        for i, a in zip(range(lines), dict_answers_global.values()):
            print(f"{i + 1}\t {questions[i]}\t\t {a}\t\t {scores[i]}")

    else:
        print("Please select [Y/n]")
        finish(num_of_ans, right_answer_number, question, score, lines)


def main(num_of_ans, right_answer_number, question, score):

    score = get_score()
    score_sum = check_score_sum()
    if not score_sum:
        print(score, score_sum)
        if sum(scores) != 0:
            scores.pop()

        score = get_score()
        score_sum = check_score_sum(score)

    if score_sum:
        question = get_question(q="")
        num_of_ans = num_answers_is_int()
        is_bigger = big_small(num_of_ans)
        answers = get_answers(is_bigger, answer="")

        while is_bigger:
            right_answer_number = right_answer_is_int(answer)
            while right_answer_number:
                r_a_n = get_right_answer_num(right_answer_number, lines=0)
                dict_answers_global[r_a_n] = list(dict_answers_local.values())[right_answer]
                print("\n========================")
                print(f"Questions: {questions}")
                print(f"Right Answers: {dict_answers_global}")
                print(f"Total Score: {sum(scores)}")
                print("========================\n")
                finish(num_of_ans, r_a_n, question, score, lines=len(questions))
                break
            break


if __name__ == "__main__":

    questions = []
    scores = []
    answers_local = []
    question_right_answers = {}
    question_answers_global = []
    number_of_answers = []
    dict_answers_local = {}
    dict_answers_global = {}
    answer = ""
    right_answer = 0
    num_of_lines = 0
    main(num_of_ans=0, right_answer_number=0, question="", score=0)
