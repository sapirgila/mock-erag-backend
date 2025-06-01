class UserService:
    def __init__(self):
        self.users = {}

    def create_user(self, user_id, user_data):
        self.users[user_id] = user_data
        return {"message": "User created successfully", "user_id": user_id}

    def get_user(self, user_id):
        if user_id in self.users:
            return {"user_id": user_id, "user_data": self.users[user_id]}
        else:
            return {"error": "User not found"}, 404