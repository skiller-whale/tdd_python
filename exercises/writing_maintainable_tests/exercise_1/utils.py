# Sample test user data
users_for_tests = [
    {"id": 1, "name": "User 1", "email": "user1@example.com"},
    {"id": 2, "name": "User 2", "email": "user2@example.com"},
    {"id": 3, "name": "User 3", "email": "user3@example.com"},
    {"id": 4, "name": "User 4", "email": "user4@example.com"},
    {"id": 5, "name": "User 5", "email": "user5@example.com"},
    {"id": 6, "name": "User 6", "email": "user6@example.com"},
    {"id": 7, "name": "User 7", "email": "user7@example.com"},
    {"id": 8, "name": "User 8", "email": "user8@example.com"},
    {"id": 9, "name": "User 9", "email": "user9@example.com"},
    {"id": 10, "name": "User 10", "email": "user10@example.com"},
    {"id": 11, "name": "User 11", "email": "user11@example.com"},
    {"id": 12, "name": "User 12", "email": "user12@example.com"},
    {"id": 13, "name": "User 13", "email": "user13@example.com"},
    {"id": 14, "name": "User 14", "email": "user14@example.com"},
    {"id": 15, "name": "User 15", "email": "user15@example.com"},
    {"id": 16, "name": "User 16", "email": "user16@example.com"},
    {"id": 17, "name": "User 17", "email": "user17@example.com"},
    {"id": 18, "name": "User 18", "email": "user18@example.com"},
    {"id": 19, "name": "User 19", "email": "user19@example.com"},
    {"id": 20, "name": "User 20", "email": "user20@example.com"},
    # Pretend there are more users here...
]


class MockDao:
    def __init__(self):
        self.users = []

    def set_users(self, users):
        self.users = users

    def get_users(self, page=1, limit=10):
        start = (page - 1) * limit
        end = start + limit
        return self.users[start:end], len(self.users)
