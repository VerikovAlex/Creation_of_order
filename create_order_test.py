import sender_request

# Вериков Александр, 8-я когорта — Финальный проект. Инженер по тестированию плюс

# Тест 1. Создание заказа и запрос информации о нем
# Проверка, что в ответ на запрос инфы о ранее созданном заказе возвращается ответ 201
def test_create_order_and_get_info_success_response():
    sender_request.positive_assert()