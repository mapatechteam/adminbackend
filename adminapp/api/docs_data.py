from drf_yasg import openapi


get_user_response = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'id': openapi.Schema(type=openapi.TYPE_INTEGER),
            'email': openapi.Schema(type=openapi.TYPE_STRING),
            'is_authenticated': openapi.Schema(type=openapi.TYPE_BOOLEAN),
            'date_joined': openapi.Schema(type=openapi.TYPE_STRING)
        },
    )

get_user_list_response = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'status': openapi.Schema(type=openapi.TYPE_STRING),
            'detail': openapi.Schema(type=openapi.TYPE_STRING),
            'data': openapi.Schema(type=openapi.TYPE_ARRAY, items=get_user_response),
        },
    )

files_make_dump_response = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'status': openapi.Schema(type=openapi.TYPE_STRING),
            'detail': openapi.Schema(type=openapi.TYPE_STRING),
            'status_code': openapi.Schema(type=openapi.TYPE_INTEGER),
        },
    )

filename_param = openapi.Parameter('filename', required=True, in_=openapi.IN_QUERY,
                                   description="Название файла", type=openapi.TYPE_STRING)


string_item = openapi.Schema(type=openapi.TYPE_STRING)

files_preview_response = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'status': openapi.Schema(type=openapi.TYPE_STRING),
            'detail': openapi.Schema(type=openapi.TYPE_STRING),
            'data': openapi.Schema(type=openapi.TYPE_ARRAY, items=string_item),
        },
    )

release_notes_response = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'number': openapi.Schema(type=openapi.TYPE_INTEGER),
            'title': openapi.Schema(type=openapi.TYPE_STRING),
            'file': openapi.Schema(type=openapi.TYPE_STRING),
        },
    )
