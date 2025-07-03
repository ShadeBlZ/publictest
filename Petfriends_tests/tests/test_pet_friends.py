from api import PetFriends
from settings import valid_email, valid_password


pf = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email,password=valid_password):
    status, result = pf.get_api_key(email,password)
    assert status == 200
    assert 'key' in result

def test_get_all_pets_with_valid_key(filter=''):
    _, auth_key = pf.get_api_key(valid_email,valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 200
    assert len(result['pets']) > 0


def test_add_new_pet_with_valid_data(name='qwe', animal_type='rty', age='33', pet_photo='images/pet_photo.jpg'):
    _, auth_key = pf.get_api_key(valid_email,valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 200
    assert result['name'] == name

def test_succesful_delete_my_pet():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, 'Джон', 'Тривольта', '69', 'images/pet_photo.jpg')
        _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    pet_id = my_pets['pets'][0]['id']
    status, _, = pf.delete_pet(auth_key, pet_id)
    assert status == 200
    assert pet_id not in my_pets.values()

def test_succesful_update_pet_info(name='Бандито', animal_type='Бобрито', age='1'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, 'Джон', 'Тривольта', '69', 'images/pet_photo.jpg')
        _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    pet_id = my_pets['pets'][0]['id']
    status, result = pf.update_pet_info(auth_key, pet_id, name, animal_type, age)
    assert status == 200
    assert name not in my_pets.values()

def test_add_pet_with_no_photo(name='Крокодило', animal_type='Бомбардино', age='2'):
    _, auth_key = pf.get_api_key(valid_email,valid_password)
    status, result = pf.add_pet_simple(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name

def test_successful_update_pet_photo(pet_photo='images/maxresdefault.jpg'):
    _, auth_key = pf.get_api_key(valid_email,valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    if len(my_pets['pets']) == 0:
        pf.add_pet_simple(auth_key, 'Крокодило', 'Бомбардино', '2')
        _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    pet_id = my_pets['pets'][0]['id']
    status, result = pf.set_pet_photo(auth_key, pet_id, pet_photo)
    assert status == 200
    #Не догнал как реализовать проверку установилось ли фото

def test_get_api_key_for_invalid_user(email = 'etozhe@bejim.omg', password = 'qwerty123'):
    status, result = pf.get_api_key(email,password)
    assert status == 403
    assert 'key' not in result
    #Не знаю обязательно ли должны падать негативные тесты, сделал проверку на неполучения ключа

def test_delete_not_my_pet():
    _, auth_key = pf.get_api_key(valid_email,valid_password)
    _, all_pets = pf.get_list_of_pets(auth_key, '')
    pet_id = all_pets['pets'][3]['id']
    status, _, = pf.delete_pet(auth_key, pet_id)
    assert status != 200
    assert pet_id in all_pets.values()
    #Поудалял чужих петов, было весело и смешно

def test_update_pet_info_with_invalid_data(name=123, animal_type='木', age='11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    if len(my_pets['pets']) == 0:
        pf.add_new_pet(auth_key, 'Джон', 'Тривольта', '69', 'images/pet_photo.jpg')
        _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    pet_id = my_pets['pets'][0]['id']
    status, result = pf.update_pet_info(auth_key, pet_id, name, animal_type, age)
    assert status == 400
    assert name in my_pets.values()

def test_add_new_pet_with_invalid_data(name='', animal_type='', age='', pet_photo='images/pet_photo.jpg'):
    _, auth_key = pf.get_api_key(valid_email,valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 400

def test_get_all_pets_with_invalid_key(filter=''):
    auth_key = {
        'key': '1233211234567890'
    }
    status, result = pf.get_list_of_pets(auth_key, filter)
    assert status == 403

def test_add_new_pet_with_invalid_key(name='qwe', animal_type='rty', age='33', pet_photo='images/pet_photo.jpg'):
    auth_key = {
        'key': 'aboba99881337'
    }
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
    assert status == 403

#Надеюсь проверки на прочность тоже считаются
def test_add_10_pets(name='qwe', animal_type='rty', age='33', pet_photo='images/pet_photo.jpg'):
    _, auth_key = pf.get_api_key(valid_email,valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    while True:
        status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)
        _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
        if len(my_pets['pets']) == 10:
            break
    assert status == 200

def test_delete_10_pets():
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
    pet_id = my_pets['pets'][0]['id']
    while True:
        status, _, = pf.delete_pet(auth_key, pet_id)
        pet_id = my_pets['pets'][0]['id']
        _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')
        if len(my_pets['pets']) == 0:
            break
    assert status == 200