from dataclasses import dataclass

@dataclass
class Question:
  category: str
  type: str
  difficulty: str
  question: str
  correct_answer: bool
  incorrect_answers: list[bool]
