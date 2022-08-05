from src.password_gen_gui import password_gen_main_app

""" main ---> password_gen_gui <-----> password_gen_error <----> password_gen_creation <----> password_gen_api
    
    password_gen_main_app: responsible for displaying input fields on screen and displaying output
    password_gen_error: Checks if user input has any errors, and displays warnings based off of errors
    password_gen_creation: Creates password from words which it gets from gen_api and input received from main_app
    password_gen_api: Talks to API, receives random words based off of user input
    
    """
if __name__ == '__main__':
    user_app = password_gen_main_app.My_Application(password_text_gened="")
