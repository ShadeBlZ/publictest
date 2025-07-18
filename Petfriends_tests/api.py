import requests
import json
import requests_toolbelt
from requests_toolbelt import MultipartEncoder


class PetFriends:
    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru"

    def get_api_key(self, email: str, password: str) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON с уникальным ключем
            пользователя, найденного по указанным email и паролю"""

        headers = {
            'email': email,
            'password': password
        }
        res = requests.get(self.base_url+'/api/key', headers=headers)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_list_of_pets(self, auth_key: json, filter: str='') -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON со списком
        найденных питомцев, совпадающих с фильтром. На данный момент фильтр иметь либо пустое значение - получить
        список всех питомцев, либо 'my_pets' - получить список собственных питомцев."""

        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url+'/api/pets', headers=headers, params=filter)

        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        return status, result


    def add_new_pet(self, auth_key: json, name: str, animal_type: str,
                    age: str, pet_photo: str) -> json:
        """Метод отправляет (постит) на сервер данные о добавляемом питомце и возвращает статус
                запроса на сервер и результат в формате JSON с данными добавленного питомца"""

        data = MultipartEncoder(
            fields={
                'name': name,
                'animal_type': animal_type,
                'age': age,
                'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            })

        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        res = requests.post(self.base_url + '/api/pets', headers=headers, data=data)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except json.JSONDecodeError:
            result = res.text
        print(result)
        return status, result

    def delete_pet(self, auth_key: json, pet_id: json) -> json:
        """Метод отправляет на сервер запрос на удаление питомца по указанному ID и возвращает
                статус запроса и результат в формате JSON с текстом уведомления о успешном удалении.
                На сегодняшний день тут есть баг - в result приходит пустая строка, но status при этом = 200"""

        headers = {'auth_key': auth_key['key']}
        res = requests.delete(self.base_url + f'/api/pets/{pet_id}', headers=headers)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        print(result)
        return status, result

    def update_pet_info(self, auth_key: json, pet_id: json, name: str, animal_type: str, age: str) -> json:
        """Метод отправляет запрос на сервер о обновлении данных питомца по указанному ID и
                возвращает статус запроса и result в формате JSON с обновлённыи данными питомца"""

        headers = {'auth_key': auth_key['key']}
        data = {
                'name': name,
                'animal_type': animal_type,
                'age': age
            }

        res = requests.put(self.base_url + f'/api/pets/{pet_id}', headers=headers, data=data)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result

    def add_pet_simple(self, auth_key: json, name: str, animal_type: str, age: str) -> json:
        """Метод отправляет на сервер данные о добавляемом питомце ( без фото ) и возвращает статус запроса вместе с
        результатом в формате JSON с данными о добавленом питомце."""

        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }
        res = requests.post(self.base_url+'/api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        print(result)
        return status, result

    def set_pet_photo(self, auth_key: json, pet_id: json, pet_photo: str) -> json:
        """Метод отправляет на сервер и обновляет данные уже имеющегося питомца, а затем возвращает статус запроса
        и обновленные данные о питомце в формате JSON"""

        data = MultipartEncoder(
            {
            'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
        })
        headers = {'auth_key': auth_key['key'], 'Content-Type': data.content_type}
        res = requests.post(self.base_url+f'/api/pets/set_photo/{pet_id}', headers=headers, data=data)
        status = res.status_code
        result = ''
        try:
            result = res.json()
        except:
            result = res.text
        print(result)
        return status, result