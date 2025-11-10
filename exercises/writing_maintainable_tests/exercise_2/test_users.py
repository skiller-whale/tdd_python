from router import Router
from utils import users_for_tests, MockDao


def test_get_0_users_ok():
    test_users = []  # empty array of users
    mock_dao = MockDao()
    mock_dao.set_users(test_users)
    router = Router(mock_dao)

    response = router.get("/users")

    assert response.status_code == 200  # OK
    assert response.get_header("Content-Type") == "application/json"

    payload = response.json()
    assert payload == {
        "data": test_users,
        "total": 0,
        "nextPage": None,
        "previousPage": None
    }


def test_get_10_users_ok():
    test_users = users_for_tests[:10]  # array of 10 users
    mock_dao = MockDao()
    mock_dao.set_users(test_users)
    router = Router(mock_dao)

    response = router.get("/users")

    assert response.status_code == 200  # OK
    assert response.get_header("Content-Type") == "application/json"

    payload = response.json()
    assert payload == {
        "data": test_users,
        "total": 10,
        "nextPage": None,
        "previousPage": None
    }


def test_get_20_users_ok():
    test_users = users_for_tests[:20]  # array of 20 users
    mock_dao = MockDao()
    mock_dao.set_users(test_users)
    router = Router(mock_dao)

    response = router.get("/users")

    assert response.status_code == 200  # OK
    assert response.get_header("Content-Type") == "application/json"

    payload = response.json()
    assert payload == {
        "data": test_users[:10],
        "total": 20,
        "nextPage": 2,
        "previousPage": None
    }
