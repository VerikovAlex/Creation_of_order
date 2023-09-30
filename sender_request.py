import configuration
import requests
import data

def create_order(): #Функция для создания нового заказа
    user_response = requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                                  json=data.user_body_for_create_order,
                                  headers=data.headers_for_create_order)
    return user_response.json()["track"]

def get_info_order(track):  #Функция запроса инфы о заказе нового набора
    print(configuration.URL_SERVICE + configuration.GET_INFO_ABOUT_ORDER + str(track))
    return requests.get(configuration.URL_SERVICE + configuration.GET_INFO_ABOUT_ORDER + str(track))

def positive_assert(): #Фнукция проверяющая успешность создания заказа
    track = create_order()
    response_info_order= get_info_order(track)
    print(response_info_order.status_code)
    print (track)
    assert response_info_order.status_code == 200