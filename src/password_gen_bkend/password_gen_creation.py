import math
from src.password_gen_bkend import password_gen_api


class Pass_Generator:

    def __init__(self, password_length, password_symbol):

        self.user_password_length = int(password_length)
        self.user_password_symbol = password_symbol

        self.API_words = []
        self.user_password_gened = ""
        self.my_API = password_gen_api.Word_API(math.floor(self.user_password_length / 3))

    def contact_api(self):
        self.API_words = self.my_API.generate_words(2)

    def password_creator(self):

        for word in self.API_words:

            self.user_password_gened += word
            self.user_password_gened += self.user_password_symbol

            if self.user_password_gened.count(self.user_password_symbol) == 2:
                self.API_words.clear()
                self.API_words += self.my_API.generate_words(self.user_password_length - len(self.user_password_gened))
                self.user_password_gened += self.API_words[0]
                break

        return self.user_password_gened
