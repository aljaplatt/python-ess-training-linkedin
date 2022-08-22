from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# write for loop to iterate over the question data
# create a question object for each entry in question data
# append each question obj to the question bank
# question_bank = []
# for question in question_data:
#     question_text = question['text']
#     question_answer = question['answer']
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)
question_bank = []
for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank) #? prints a list of 12 question objects
# print(question_bank[0].text) #? prints 'A slug's blood is green.'

quiz = QuizBrain(question_bank )

# if quiz still has ques is true, go to next question else exit loop.
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")