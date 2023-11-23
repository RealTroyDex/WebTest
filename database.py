class UserDB:
    def __init__(self):
        self.users = []

    def add_user(self, email, password, activation_code):
        user = {'email': email, 'password': password, 'activation_code': activation_code, 'activated': False}
        self.users.append(user)

    def get_user_by_email(self, email):
        for user in self.users:
            if user['email'] == email:
                return user
        return None

    def activate_user(self, email, activation_code):
        user = self.get_user_by_email(email)
        if user and user['activation_code'] == activation_code:
            user['activated'] = True
            return True
        return False
