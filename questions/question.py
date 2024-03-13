import json

f=open("questions.json")
questions=json.load(f)
score = 0
for idx, q in enumerate(questions["questions"]) :
    #print(q)
    print("Choose correct Answer")
    print(f"{idx + 1}. {q['question']}")
    for i, c in enumerate(q["choices"]) :
        print(f"{i + 1}. {c}")
    ans = int(input("Enter your choice\n")) - 1
    if ans == q["answer"]:
        score = score + 1
    else:
        print("You have enter incorrect answer")
        print(f"Answer for {q['question']} is {q['choices'][q['answer']]}")
print(f"Your score is {score}/{len(questions['questions'])}")
