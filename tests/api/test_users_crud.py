"""API tests for reqres.in users endpoint - CRUD operations.

Run: pytest tests/api/test_users_crud.py -v
"""
import allure
import requests

HEADERS = {"x-api-key": "reqres-free-v1"}  # reqres.in free public key


@allure.feature("Users API")
class TestUsersCrud:

    @allure.title("GET /users returns paginated user list")
    def test_get_users_list(self, api_base_url):
        response = requests.get(f"{api_base_url}/users", params={"page": 1}, headers=HEADERS)
        assert response.status_code == 200
        body = response.json()
        assert body["page"] == 1
        assert len(body["data"]) > 0
        # Schema check on the first user record
        user = body["data"][0]
        for field in ("id", "email", "first_name", "last_name"):
            assert field in user

    @allure.title("GET /users/{id} returns a single user")
    def test_get_single_user(self, api_base_url):
        response = requests.get(f"{api_base_url}/users/2", headers=HEADERS)
        assert response.status_code == 200
        assert response.json()["data"]["id"] == 2

    @allure.title("GET /users/{id} with non-existent id returns 404")
    def test_get_user_not_found(self, api_base_url):
        response = requests.get(f"{api_base_url}/users/9999", headers=HEADERS)
        assert response.status_code == 404

    @allure.title("POST /users creates a user and returns id")
    def test_create_user(self, api_base_url):
        payload = {"name": "Julia", "job": "QA Engineer"}
        response = requests.post(f"{api_base_url}/users", json=payload, headers=HEADERS)
        assert response.status_code == 201
        body = response.json()
        assert body["name"] == payload["name"]
        assert "id" in body and "createdAt" in body

    @allure.title("PUT /users/{id} updates a user")
    def test_update_user(self, api_base_url):
        payload = {"name": "Julia", "job": "Senior QA Engineer"}
        response = requests.put(f"{api_base_url}/users/2", json=payload, headers=HEADERS)
        assert response.status_code == 200
        assert response.json()["job"] == payload["job"]

    @allure.title("DELETE /users/{id} returns 204 No Content")
    def test_delete_user(self, api_base_url):
        response = requests.delete(f"{api_base_url}/users/2", headers=HEADERS)
        assert response.status_code == 204
