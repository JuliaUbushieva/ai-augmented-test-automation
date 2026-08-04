"""API tests for jsonplaceholder.typicode.com posts endpoint - CRUD operations.

Run: pytest tests/api/test_users_crud.py -v
"""
import allure
import requests


@allure.feature("Posts API")
class TestPostsCrud:

    @allure.title("GET /posts returns a list of posts")
    def test_get_posts_list(self, api_base_url):
        response = requests.get(f"{api_base_url}/posts")
        assert response.status_code == 200
        body = response.json()
        assert len(body) > 0
        # Schema check on the first record
        for field in ("userId", "id", "title", "body"):
            assert field in body[0]

    @allure.title("GET /posts/{id} returns a single post")
    def test_get_single_post(self, api_base_url):
        response = requests.get(f"{api_base_url}/posts/1")
        assert response.status_code == 200
        assert response.json()["id"] == 1

    @allure.title("GET /posts/{id} with non-existent id returns 404")
    def test_get_post_not_found(self, api_base_url):
        response = requests.get(f"{api_base_url}/posts/99999")
        assert response.status_code == 404

    @allure.title("POST /posts creates a post and returns id")
    def test_create_post(self, api_base_url):
        payload = {"title": "QA note", "body": "Created by automated test", "userId": 1}
        response = requests.post(f"{api_base_url}/posts", json=payload)
        assert response.status_code == 201
        body = response.json()
        assert body["title"] == payload["title"]
        assert "id" in body

    @allure.title("PUT /posts/{id} updates a post")
    def test_update_post(self, api_base_url):
        payload = {"id": 1, "title": "Updated title", "body": "Updated body", "userId": 1}
        response = requests.put(f"{api_base_url}/posts/1", json=payload)
        assert response.status_code == 200
        assert response.json()["title"] == payload["title"]

    @allure.title("DELETE /posts/{id} returns 200")
    def test_delete_post(self, api_base_url):
        response = requests.delete(f"{api_base_url}/posts/1")
        assert response.status_code == 200