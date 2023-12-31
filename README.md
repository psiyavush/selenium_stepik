# Selenium и Python
**Решение задач по курсу "Автоматизация тестирования с помощью Selenium и Python"**

Сам курс [по ссылке](https://stepik.org/course/575/promo)

Смотрите также Уроки и материалы по курсу "Автоматизация Selenium на Python" [здесь](https://gitlab.com/last-dragon/selenium-on-python)
____
## Список задач по разделам
### Задачи из раздела 1.6 "Поиск элементов с помощью Selenium WebDriver"
* lesson1.6_step4 - поиск элементов с помощью Selenium
* lesson1.6_step5 - поиск элемента по тексту в ссылке
* lesson1.6_step7 - использование метода find_elements
* lesson1.6_step8 - поиск элемента по XPath
* lesson1.6_final - Финальное задание "Уникальность селекторов"

### Задачи из раздала 2. "Полезные методы Selenium"
* lesson2.1_1 - кликаем по checkboxes и radiobuttons (капча для роботов)
* lesson2.1_2 - поиск сокровища с помощью get_attribute
* lesson2.2_1 - работа с выпадающим списком
* lesson2.2_2 - Задание на execute_script
* lesson2.2_3 - загрузка файла
* lesson2.3_1 - принимаем alert
* lesson2.3_2 - переход на новую вкладку
* lesson2.4   - ждем нужный текст на странице

### Задачи из раздала 3. "Тестовые фреймворки"
* lesson3.2 - оформляем тесты в стиле unittest
* lesson3_3_test - оформляем тесты в стиле PyTest
* lesson3.3.2.sh - Фиксируем пакеты в requirements.txt
* pytest.sh - Полезные команды для манипуляции выводом тестов PyTest
* test_fixture - Использование фикстур в PyTest
  * test_fixture1 - Классические фикстуры
  * test_fixture2 - Фикстуры, возвращающие значение
  * test_fixture3 - Финализаторы — закрываем браузер
  * test_fixture4 - Область видимости scope
  * test_fixture5 - Автоиспользование фикстур
  * test_fixture6 - Маркировка тестов
  * pytest.ini - регистрация меток
  
    *Создайте файл pytest.ini в корневой директории вашего тестового проекта и добавьте в файл*
    
    *Текст после знака ":" является поясняющим — его можно не писать.*
  * test_fixture7 - Пропуск тестов
  * test_fixture8 - XFail: помечать тест как ожидаемо падающий
  * conftest.py - конфигурация тестов (Для хранения часто употребимых фикстур и хранения глобальных настроек)
  * test_fixture9 - Параметризация тестов
* lesson3_6_1_test - Задание: логин + параметризация тестов на stepik.org
* parset - Conftest.py и передача параметров в командной строке
  * conftest.py - добавлена логика обработки командной строки по использованию браузера
  * test_parser - запуск теста с параметрами браузеров
  * test_rerun - перезапуск упавших тестов
* stepik3.6 - Запуск автотестов для разных языков интерфейса
  * conftest.py - считывает из командной строки параметр language и browser
  * test_items.py - тест проверяет, что страница товара содержит кнопку добавления в корзину


  **Полный список доступных плагинов Для PyTest** [**здесь**](https://docs.pytest.org/en/latest/reference/plugin_list.html)
