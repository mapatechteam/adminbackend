import json
from http import HTTPStatus
from rest_framework.test import APIClient, APITestCase


class TestClass(APITestCase):
    client = APIClient()
    base_url = 'http://127.0.0.1:8000/api/lectonic_admin/api/'
    user_id_exists = str(1)
    correct_filename = 'test.txt'
    incorrect_filename = 'test.123'

    def test_get_users(self):
        url = self.base_url + f'users/{self.user_id_exists}/'
        response = self.client.get(url)

        assert response.status_code == HTTPStatus.OK, (
            'GET запрос с user_id, отправленный на '
            f'эндпоинт {url}, должен вернуть ответ со '
            'статусом 200'
        )


    def test_delete_users(self):
        url = self.base_url + f'users/{self.user_id_exists}/'
        response = self.client.delete(url)

        assert response.status_code == HTTPStatus.OK, (
            'DELETE запрос с user_id, отправленный на '
            f'эндпоинт {url}, должен вернуть ответ со '
            'статусом 200'
        )


    def test_get_users_list(self):
        url = self.base_url + 'users/list/'
        response = self.client.get(url)

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

        assert response.data.get('status') == 'success', (
            'GET запрос, отправленный на '
            f'эндпоинт {url}, должен вернуть json, '
            'содержащий ключ "status" со значением "success"'
        )

        assert response.data.get('detail') == 'Список всех пользователей', (
            'GET запрос, отправленный на '
            f'эндпоинт {url}, должен вернуть json, '
            'содержащий ключ "detail" со значением "Список всех пользователей"'
        )


    def test_files_make_dump(self):
        url = self.base_url + 'files/make_dump/'


        response = self.client.generic(
            method='GET', path=url, data=json.dumps({'filename': self.correct_filename}),
            content_type='application/json')
        
        assert response.status_code == HTTPStatus.OK, (
            'GET запрос с корректным filename, отправленный на '
            f'эндпоинт {url}, должен вернуть ответ cо '
            'статусом 200'
        )

        assert list(response.data.keys()) == ['status', 'detail', 'status_code'], (
            'GET запрос с корректным filename, отправленный на '
            f'эндпоинт {url}, должен вернуть json c '
            'полями status, detail, status_code'
        )

        assert response.data.get('status') == 'success', (
            'GET запрос c корректным filename, отправленный на '
            f'эндпоинт {url}, должен вернуть json, '
            'содержащий ключ "status" со значением "success"'
        )

        assert response.data.get('detail') == 'Запрос успешно обработан', (
            'GET запрос c корректным filename, отправленный на '
            f'эндпоинт {url}, должен вернуть json, '
            'содержащий ключ "detail" со значением "Запрос успешно обработан"'
        )

        assert response.data.get('status_code') == HTTPStatus.OK, (
            'GET запрос c корректным filename, отправленный на '
            f'эндпоинт {url}, должен вернуть json, '
            'содержащий ключ "status_code" со значением "200"'
        )

        response = self.client.generic(
            method='GET', path=url, data=json.dumps({'filename': self.incorrect_filename}),
            content_type='application/json')
        
        assert response.status_code == HTTPStatus.BAD_REQUEST, (
            'GET запрос с НЕкорректным filename, отправленный на '
            f'эндпоинт {url}, должен вернуть ответ cо '
            'статусом 400'
        )

        assert list(response.data.keys()) == ['status', 'detail', 'status_code'], (
            'GET запрос с НЕкорректным filename, отправленный на '
            f'эндпоинт {url}, должен вернуть json c '
            'полями status, detail, status_code'
        )

        assert response.data.get('status') == 'error', (
            'GET запрос с НЕкорректным filename, отправленный на '
            f'эндпоинт {url}, должен вернуть json, '
            'содержащий ключ "status" со значением "error"'
        )

        assert response.data.get('detail') == 'Текст ошибки', (
            'GET запрос с НЕкорректным filename, отправленный на '
            f'эндпоинт {url}, должен вернуть json, '
            'содержащий ключ "detail" со значением "Текст ошибки"'
        )

        assert response.data.get('status_code') == HTTPStatus.BAD_REQUEST, (
            'GET запрос с НЕкорректным filename, отправленный на '
            f'эндпоинт {url}, должен вернуть json, '
            'содержащий ключ "status_code" со значением "400"'
        )

    def test_files_preview(self):
        url = self.base_url + 'files/preview/'
        response = self.client.get(url, data={'filename': 'test.txt'})

        assert response.status_code == HTTPStatus.OK, (
            'GET запрос с filename, отправленный на '
            f'эндпоинт {url}, должен вернуть ответ cо '
            'статусом 200'
        )

        assert list(response.data.keys()) == ['status', 'detail', 'data'], (
            'GET запрос, отправленный на '
            f'эндпоинт {url}, должен вернуть json c '
            'полями status, detail, data'
        )

        assert response.data.get('status') == 'success', (
            'GET запрос, отправленный на '
            f'эндпоинт {url}, должен вернуть json, '
            'содержащий ключ "status" со значением "success"'
        )

        assert response.data.get('detail') == 'Превью файла', (
            'GET запрос, отправленный на '
            f'эндпоинт {url}, должен вернуть json, '
            'содержащий ключ "detail" со значением "Превью файла"'
        )

        assert isinstance(response.data.get('data'), list), (
            'GET запрос, отправленный на '
            f'эндпоинт {url}, должен вернуть json, '
            'содержащий ключ "data" со значением типа list'
        )
    
    def test_files_save(self):
        url = self.base_url + 'files/save/'

        response = self.client.generic(
            method='GET', path=url, data=json.dumps({'filename': self.correct_filename}),
            content_type='application/json'
        )

        assert response.status_code == HTTPStatus.OK, (
            'GET запрос с корректным filename, отправленный на '
            f'эндпоинт {url}, должен вернуть ответ cо '
            'статусом 200'
        )

        assert response.__getitem__('content-type') == 'application/octet-stream', (
            'GET запрос с корректным filename, отправленный на '
            f'эндпоинт {url}, должен вернуть ответ в '
            'application/octet-stream формате'
        )

        response = self.client.generic(
            method='GET', path=url, data=json.dumps({'filename': self.incorrect_filename}),
            content_type='application/json')
        
        assert response.status_code == HTTPStatus.NOT_FOUND, (
            'GET запрос с НЕкорректным filename, отправленный на '
            f'эндпоинт {url}, должен вернуть ответ cо '
            'статусом 404'
        )

        assert list(response.data.keys()) == ['status', 'detail', 'status_code'], (
            'GET запрос с НЕкорректным filename, отправленный на '
            f'эндпоинт {url}, должен вернуть json c '
            'полями status, detail, status_code'
        )

        assert response.data.get('status') == 'error', (
            'GET запрос с НЕкорректным filename, отправленный на '
            f'эндпоинт {url}, должен вернуть json, '
            'содержащий ключ "status" со значением "error"'
        )

        assert response.data.get('detail') == 'Текст ошибки', (
            'GET запрос с НЕкорректным filename, отправленный на '
            f'эндпоинт {url}, должен вернуть json, '
            'содержащий ключ "detail" со значением "Текст ошибки"'
        )

        assert response.data.get('status_code') == HTTPStatus.NOT_FOUND, (
            'GET запрос с НЕкорректным filename, отправленный на '
            f'эндпоинт {url}, должен вернуть json, '
            'содержащий ключ "status_code" со значением "404"'
        )
    
    def test_files_delete(self):
        url = self.base_url + 'files/delete/'
        response = self.client.generic(
            method='DELETE', path=url, data=json.dumps({'filename': self.correct_filename}),
            content_type='application/json'
        )

        assert response.status_code == HTTPStatus.OK, (
            'DELETE запрос с корректным filename, отправленный на '
            f'эндпоинт {url}, должен вернуть ответ cо '
            'статусом 200'
        )

        assert list(response.data.keys()) == ['status', 'detail', 'status_code'], (
            'DELETE запрос с корректным filename, отправленный на '
            f'эндпоинт {url}, должен вернуть json c '
            'полями status, detail, status_code'
        )

        assert response.data.get('status') == 'deleted', (
            'GET запрос с корректным filename, отправленный на '
            f'эндпоинт {url}, должен вернуть json, '
            'содержащий ключ "status" со значением "deleted"'
        )

        assert response.data.get('detail') == 'Объект успешно удален', (
            'GET запрос с корректным filename, отправленный на '
            f'эндпоинт {url}, должен вернуть json, '
            'содержащий ключ "detail" со значением "Объект успешно удален"'
        )

        assert response.data.get('status_code') == HTTPStatus.OK, (
            'GET запрос с корректным filename, отправленный на '
            f'эндпоинт {url}, должен вернуть json, '
            'содержащий ключ "status_code" со значением "200"'
        )

        response = self.client.generic(
            method='DELETE', path=url, data=json.dumps({'filename': self.incorrect_filename}),
            content_type='application/json')
        
        assert response.status_code == HTTPStatus.BAD_REQUEST, (
            'GET запрос с НЕкорректным filename, отправленный на '
            f'эндпоинт {url}, должен вернуть ответ cо '
            'статусом 400'
        )

        assert list(response.data.keys()) == ['status', 'detail', 'status_code'], (
            'GET запрос с НЕкорректным filename, отправленный на '
            f'эндпоинт {url}, должен вернуть json c '
            'полями status, detail, status_code'
        )

        assert response.data.get('status') == 'error', (
            'GET запрос с НЕкорректным filename, отправленный на '
            f'эндпоинт {url}, должен вернуть json, '
            'содержащий ключ "status" со значением "error"'
        )

        assert response.data.get('detail') == 'Текст ошибки', (
            'GET запрос с НЕкорректным filename, отправленный на '
            f'эндпоинт {url}, должен вернуть json, '
            'содержащий ключ "detail" со значением "Текст ошибки"'
        )

        assert response.data.get('status_code') == HTTPStatus.BAD_REQUEST, (
            'GET запрос с НЕкорректным filename, отправленный на '
            f'эндпоинт {url}, должен вернуть json, '
            'содержащий ключ "status_code" со значением "400"'
        )

    def test_get_release_notes(self):
        url = self.base_url + 'release_notes/'

        response = self.client.get(url)

        assert response.status_code == HTTPStatus.OK, (
            'GET запрос, отправленный на '
            f'эндпоинт {url}, должен вернуть ответ cо '
            'статусом 200'
        )

        assert list(response.data.keys()) == ['number', 'title', 'file'], (
            'GET запрос с корректным filename, отправленный на '
            f'эндпоинт {url}, должен вернуть json c '
            'полями number, title, file'
        )

        assert response.data.get('number') == 0, (
            'GET запрос, отправленный на '
            f'эндпоинт {url}, должен вернуть json, '
            'содержащий ключ "number" со значением "0"'
        )

        assert response.data.get('title') == 'title', (
            'GET запрос, отправленный на '
            f'эндпоинт {url}, должен вернуть json, '
            'содержащий ключ "title" со значением "title"'
        )

        assert response.data.get('file') == 'file', (
            'GET запрос, отправленный на '
            f'эндпоинт {url}, должен вернуть json, '
            'содержащий ключ "file" со значением "file"'
        )
    
    def test_post_release_notes(self):
        url = self.base_url + 'release_notes/'

        response = self.client.post(url)

        assert response.status_code == HTTPStatus.OK, (
            'POST запрос, отправленный на '
            f'эндпоинт {url}, должен вернуть ответ cо '
            'статусом 200'
        )

    
    def test_delete_release_notes(self):
        url = self.base_url + 'release_notes/'

        response = self.client.delete(url)

        assert response.status_code == HTTPStatus.OK, (
            'DELETE запрос, отправленный на '
            f'эндпоинт {url}, должен вернуть ответ cо '
            'статусом 200'
        )
    
    def test_release_show(self):
        url = self.base_url + 'release_notes/show'

        response = self.client.get(url)

        assert response.status_code == HTTPStatus.OK, (
            'GET запрос, отправленный на '
            f'эндпоинт {url}, должен вернуть ответ cо '
            'статусом 200'
        )