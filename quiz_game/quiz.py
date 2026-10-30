def start_quiz(questions):
    score = 0

    for question in questions:
        print("\n" + question["question"])

        for i, option in enumerate(question["options"], 1):
            print(f"{i}. {option}")

        answer = int(input("Apna answer choose karo: "))

        if answer == question["answer"]:
            print("✅ Correct!")
            score += 1
        else:
            print("❌ Wrong!")

    return score