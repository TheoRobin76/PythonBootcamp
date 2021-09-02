from OOP_quiz_game import Question, question_data, QuizBrain

question_bank = []
for i in question_data:
    text = i['text']
    answer = i['answer']
    new_question = Question(text, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

quiz.end_game()
