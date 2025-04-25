"""This is the router being tested, it expects a DAO object to be passed in
to its constructor.

The DAO is responsible for fetching data from the database, and the router is
responsible for formatting that data into a response.
"""


class Router:
    def __init__(self, dao):
        self.dao = dao

    def get(self, path):
        if path == "/users":
            users, total = self.dao.get_users()

            # Calculate pagination
            next_page = 2 if total > 10 else None
            previous_page = None

            response_data = {
                "data": users,
                "total": total,
                "nextPage": next_page,
                "previousPage": previous_page
            }

            return Response(200, response_data)
        return Response(404, {"error": "Not found"})


class Response:
    def __init__(self, status_code, data, headers=None):
        self.status_code = status_code
        self.data = data
        self.headers = headers or {"Content-Type": "application/json"}

    def json(self):
        return self.data

    def get_header(self, key):
        return self.headers.get(key)
