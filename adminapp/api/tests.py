from rest_framework.test import APIClient, APITestCase
from http import HTTPStatus
client = APIClient()


base_url = 'http://127.0.0.1:8000/api/lectonic_admin/api/'


class UsersTest(APITestCase):
    user_id_exists = '1'

    def test_get_users(self):
        url = base_url + f'users/{self.user_id_exists}/'
        response = client.get(url)

        assert response.status_code == HTTPStatus.OK, (
            'GET запрос с user_id, отправленный на '
            f'эндпоинт {url}, должен вернуть ответ со '
            'статусом 200'
        )

    def test_delete_users(self):
        url = base_url + f'users/{self.user_id_exists}/'
        response = client.delete(url)

        assert response.status_code == HTTPStatus.OK, (
            'DELETE запрос с user_id, отправленный на '
            f'эндпоинт {url}, должен вернуть ответ со '
            'статусом 200'
        )

    def test_get_users_list(self):
        url = base_url + 'users/list/'
        response = client.get(url)

        assert response.status_code == HTTPStatus.OK, (
            'GET запрос, отправленный на '
            f'эндпоинт {url}, должен вернуть ответ со '
            'статусом 200'
        )

        assert list(response.data.keys()) == ['status', 'detail', 'data'], (
            'GET запрос, отправленный на '
            f'эндпоинт {url}, должен вернуть json c '
            'полями status, detail, data'
        )

class FilesTest(APITestCase):
    # def test_files_make_dump(self):
    #     url = base_url + 'files/make_dump/'
    #     correct_filename = 'test.txt'
    #     incorrect_filename = 'test.123'

    #     response = client.get(url, data={'filename': correct_filename})
    #     assert response.status_code == HTTPStatus.OK, (
    #         'GET запрос с корректным filename, отправленный на '
    #         f'эндпоинт {url}, должен вернуть ответ cо '
    #         'статусом 200'
    #     )

    #     assert response.data.keys() == ['status', 'detail', 'status_code'], (
    #         'GET запрос с корректным filename, отправленный на '
    #         f'эндпоинт {url}, должен вернуть json c '
    #         'полями status, detail, status_code'
    #     )

        # response = client.get(url, data={'filename': incorrect_filename})
        # assert response.status_code == HTTPStatus.BAD_REQUEST, (
        #     'GET запрос с НЕкорректным filename, отправленный на '
        #     f'эндпоинт {url}, должен вернуть ответ cо '
        #     'статусом 400'
        # )
