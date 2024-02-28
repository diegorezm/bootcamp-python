from question_model import Question


class QuizBrain:
    def __init__(self, q_list: list[Question]) -> None:
        self.q_list = q_list
        self.current_question: int = 0

    def next_question(self) -> (Question | None):
        if self.has_next_question():
            self.current_question += 1
            return self.q_list[self.current_question]
        return None

    def check_answer(self, user_answer: bool) -> bool:
        current_q = self.q_list[self.current_question]
        if current_q.correct_answer == user_answer:
            return True
        return False
    
    def has_next_question(self) -> bool:
        if self.current_question < len(self.q_list) - 1:
            return True
        return False
