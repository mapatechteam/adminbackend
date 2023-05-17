from http import HTTPStatus

import pytest

class Test00Users:
    url_users = 'api/lectonic_admin/api/users/'
    url_user_list = 'api/lectonic_admin/api/users/list/'

    def test_00_users_200(self, client):
        user_id_exists = 1
        # user_id_not_exists = 10
        url = self.url_users + user_id_exists +'/'
        response = client.get(url)

        assert response.status_code == HTTPStatus.OK ,(
            'GET запрос с существующим user_id, отправленный на '
            f'эндпоинт {self.url_users}, должен вернуть ответ со '
            'статусом 200'
        )