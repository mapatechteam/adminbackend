import re

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .data import data_users


@api_view(['GET', 'DELETE'])
def user(request, user_id):
    if request.method == 'GET':
        data = data_users.get(user_id)
        return Response(data, status=status.HTTP_200_OK)
    if request.method == 'DELETE':
        return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def user_list(request):
    users_list_response = {
        'status': 'success',
        'detail': 'Список всех пользователей',
        'data': [x for x in data_users.values()]
    }
    return Response(users_list_response, status=status.HTTP_200_OK)


@api_view(['GET'])
def files_make_dump(request):
    regex = r'^[A-Za-z0-9]{1,10}\.[A-Za-z]{1,4}$'
    print(request.data)
    filename = request.data.get('filename')
    print(filename)

    if not re.match(regex, filename):
        return Response(
            {'status': 'error',
             'detail': 'Текст ошибки',
             'status_code': status.HTTP_400_BAD_REQUEST},
            status=status.HTTP_400_BAD_REQUEST
        )

    return Response(
        {'status': 'success',
         'detail': 'Запрос успешно обработан',
         'status_code': status.HTTP_200_OK},
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
def files_preview(request):
    filename = request.data.get('filename')
    return Response(
        {"status": "success",
         "detail": "Превью файла",
         "data": [f"Превью файла {filename}"]},
        status=status.HTTP_200_OK
    )


@api_view(['GET'])
def files_save(request):
    filename = request.data.get('filename')
    regex = r'^[A-Za-z0-9]{1,10}\.[A-Za-z]{1,4}$'
    if not re.match(regex, filename):
        return Response(
            {'status': 'error',
             'detail': 'Текст ошибки',
             'status_code': status.HTTP_404_NOT_FOUND},
            status=status.HTTP_404_NOT_FOUND
        )

    return Response(filename, content_type='application/octet-stream',
                    status=status.HTTP_200_OK
                    )


@api_view(['DELETE'])
def files_delete(request):
    regex = r'^[A-Za-z0-9]{1,10}\.[A-Za-z]{1,4}$'
    filename = request.data.get('filename')

    if not re.match(regex, filename):
        return Response(
            {'status': 'error',
             'detail': 'Текст ошибки',
             'status_code': status.HTTP_400_BAD_REQUEST},
            status=status.HTTP_400_BAD_REQUEST
        )

    return Response(
        {'status': 'deleted',
         'detail': 'Объект успешно удален',
         'status_code': status.HTTP_200_OK},
        status=status.HTTP_200_OK
    )


@api_view(['GET', 'POST', 'DELETE'])
def release_notes(request):
    if request.method == 'GET':
        return Response(
            {"number": 0,
             "title": "title",
             "file": "file"},
            status=status.HTTP_200_OK
        )

    if request.method == 'POST':
        return Response(status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def release_notes_show(request):
    return Response(status=status.HTTP_200_OK)
