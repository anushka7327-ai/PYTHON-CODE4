def get_answer():
    while True:
        try:
            answer = int(input("Apna answer choose karo (1-4): "))

            if 1 <= answer <= 4:
                return answer

            print("Please 1 se 4 ke beech number enter karo.")

        except ValueError:
            print("Please sirf number enter karo.")
