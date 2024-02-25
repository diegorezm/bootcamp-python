from dataclasses import dataclass
import pandas as pd
import string
import random


@dataclass
class Password:
    website: str
    emailOrUsername: str
    password: str


class PassowrdManager:
    def __init__(self) -> None:
        self.password_list: list[Password] = self.get_all_passwords()

    def get_all_passwords(self) -> list[Password]:
        try:
            df = pd.read_csv("./passwords.csv")
            w = df["Website"]
            e = df["Email/Username"]
            p = df["Password"]
            passwords: list[Password] = []
            for website, email, password in zip(w, e, p):
                passwords.append(
                    Password(website=website, emailOrUsername=email, password=password)
                )
            return passwords
        except FileNotFoundError:
            return []

    def save_data(self):
        password_data = [
                {"Website": password.website, "Email/Username": password.emailOrUsername, "Password": password.password}
            for password in self.password_list
        ]
        df = pd.DataFrame(password_data)
        df.to_csv("./passwords.csv", index=False)

    def create_new_entry(self, p: Password):
        self.password_list.append(p)
        self.save_data()

    @staticmethod
    def gen_random_password() -> str:
        alphabet = list(string.ascii_lowercase + string.ascii_uppercase)  
        symbols = ["%", "@", "#", "$", "&", "*","(", ")", "-", "_", "+", "-"]
        possible_numbers = list(range(101))
        new_password = []
        for _ in range(4):
            new_password.append(random.choice(alphabet))
        for _ in range(4):
            new_password.append(random.choice(symbols))
        for _ in range(4):
            new_password.append(random.choice(str(possible_numbers)))
        return ''.join(new_password)
