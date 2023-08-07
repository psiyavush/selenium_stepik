** Полезные команды для манипуляции выводом тестов PyTest **
# можно вместо py.test писать pytest
py.test test_sample.py --collect-only # собирает информацию тестового набора

py.test test_sample.py -v # выводит вербозные сообщения

py.test test_sample.py -s # позволяет увидеть текст, который выводится командой print()

py.test -q test_sample.py # опустить вывод имени файла

python -m pytest -q test_sample.py # вызов pytest через python

py.test --markers # показать доступные маркеры

# Для того чтобы создать маркер многократного использования.
/*
# содержимое pytest.ini
[pytest].
маркеры =
    webtest: пометить тест как webtest.
*/

py.test -k "TestClass, а не test_one" # запускать только тесты с именами, которые соответствуют "строковому выражению"

py.test test_server.py::TestClass::test_method # cnly run tests that match the node ID

py.test -x # останавливаться после первой неудачи

py.test --maxfail=2 # останавливаться после двух неудач

py.test --showlocals # показывать локальные переменные в трассировках
py.test -l # (сокращение)

py.test --tb=long # информативное форматирование трассировки по умолчанию
py.test --tb=native # форматирование стандартной библиотеки Python
py.test --tb=short # более короткий формат возвратов к трассировке
py.test --tb=line # только одна строка для каждого сбоя
py.test --tb=no # отсутствие вывода трассировки

py.test -x --pdb # при первом сбое сброс в PDB, затем завершение сеанса тестирования

py.test --durations=10 # список 10 самых медленных длительностей теста.

py.test --maxfail=2 -rf # выход после двух сбоев, сообщение о сбое.

py.test -n 4 # посылать тесты на несколько процессоров

py.test -m slowest # запускать тесты с декоратором @pytest.mark.slowest или slowest = pytest.mark.slowest; @slowest

py.test --traceconfig # выяснить, какие плагины py.test активны в вашем окружении.

py.test --instafail # если установлен pytest-instafail, показывать ошибки и сбои мгновенно, а не ждать окончания набора тестов.

# Тестирование с использованием параметризации
/*
    import pytest


    @pytest.mark.parametrize(
        ('n', 'expected'), [
            (1, 2),
            (2, 3),
            (3, 4),
            (4, 5),
            pytest.mark.xfail((1, 0)),
            pytest.mark.xfail(reason="some bug")((1, 0)),
            pytest.mark.skipif('sys.version_info >= (3,0)')((10, 11)),
        ]
    )
    def test_increment(n, expected):
        assert n + 1 == expected
*/