import os
from quiz_data import questions, Question

class QuizGame:
  questions: list[Question]
  score: int
  
  def __init__(self) -> None:
    self.questions = questions
    self.score = 0

  def handle_asnwer(self, question: Question, asn: str) -> bool:
    asn = asn.capitalize()  
    if asn == question.correct_answer:
       return True
    return False
  
  def start(self):
    for i in range(len(self.questions)):
      question = questions[i]
      q = input(f"Q.{i + 1}: {question.question}. (True\\False): ")
      correct = self.handle_asnwer(question, q)
      if not correct:
        print("That was wrong!")
      else:
        print("That was correct!")
        self.score += 1
      print(f"The correct answer was: {question.correct_answer}")
      print(f"Your current score is: {self.score}/{i}")

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')
    quiz = QuizGame()
    quiz.start()