import re


class QuizBrain:
    def __init__(self, questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0
    
    def still_has_questions(self):
        # if self.question_number < len(self.questions_list):
        #     return True
        # else: 
        #     return False 
        return self.question_number < len(self.questions_list)

    def next_question(self):
        curr_question = self.questions_list[self.question_number]
        # question number increased each time the user is shown next question 
        # starts , then jumps immdediately to 1
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {curr_question.text} (True/False?)")
        self.check_answer(user_answer, curr_question.answer)
    
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print('You got it right!')
        else:
            print('Incorrect.')
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
