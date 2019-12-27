import time

link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_basket_button(browser):
    browser.get(link)
    # для проверки по критерию 2 снять значок # ниже
    # time.sleep(30)
    button = len(browser.find_elements_by_css_selector("#add_to_basket_form button"))
    assert button > 0, "Кнопка 'Добавить в корзину' не найдена"
    
# запросы для запуска (по умолчанию установлен русский язык и браузер Хром):
# запрос из задания: pytest --language=es test_items.py
# запрос для французского языка и браузера Мозилла: pytest --browser_name=firefox --language=fr test_items.py
