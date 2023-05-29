# lectonic_adminapp
OpenAPI документация: adminapp/schema.yaml
## Запуск сервиса
1. Клонировать репозиторий:
```
git clone https://github.com/MikhailBogachev/TEST_DRF_friend_service.git
```
2. Gерейти в него в командной строке:
```
cd adminapp/
```
### Запуск с помощью docker
3. Выполнить последовательно две команды:
```
docker build -t django_drf .
```

```
docker run -d -p 8080:8000 --name django_drf_app django_drf
```
Документация: 
```
http://localhost:8080/api/lectonic_admin/api/swagger/
```
Запросы к API делать по адресу:
```
http://localhost:8080/api/lectonic_admin/api/
```
