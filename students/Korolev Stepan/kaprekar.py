import matplotlib.pyplot as plt


def kaprekar(value: int, k: int = 4, r: int = 10):
    assert type(value) == int and type(k) == int and type(r) == int, \
        "Error: 0x00, value is not an int"

    if k < 2 or r < 2 \
            or not len(str(value)) == k: return -1  # задачи при k<2 или r<2 не имеют смысла

    assert k > 1, \
        "Error: 0x01"  # если как-то условие не прошло!?!?!

    assert r > 1, \
        "Error: 0x02"  # то же самое
    digits = []  # список цифр
    for i in range(len(str(value))):
        digits.append(str(value % r))
        value //= r
    digits.sort(key=lambda i: -int(i))  # максимальное число
    digits_max = int(''.join(digits))
    digits.sort(key=lambda i: int(i))
    digits_min = int(''.join(digits))  # минимальное число
    return digits_max - digits_min  # их разность


def kaprekarIm(x: list, k: int = 4, r: int = 10):
    assert type(x) == list and len(x) > 0, \
        "Error 0x04"
    return [kaprekar(i, k, r) for i in x]  # возвращает список образов


def _kaprekargraph(x: list, k: int = 4, r: int = 10):
    assert type(x) == list and len(x) > 0, \
        "Error 0x04"
    graph = {}  # словарь вида {образ: [список прообразов]}
    for i in set(kaprekarIm(x, k, r)):  # проходим по ключам
        _array = []  # список прообразов
        for j in x:  # проходим по прообразу
            if kaprekar(j, k, r) == i:  # если образ равен ключу
                _array.append(j)  # добавляем в список прообраз
        graph[i] = _array  # ключ: [все прообразы]
    return graph


def createlinks(a: dict):
    _tmp = []  # массив для очистки массива
    for i in a:  # проходим все ключи
        for j in a[i]:  # проходим все значения ключа a[i]
            if j in a and not j == i:  # если значение это ключ
                for x in a[j]:  # то для всех значений этого ключа a[j]
                    a[i].append(x)  # объединяем значения в граф
                    a[i] = list(set(a[i]))  # удаляем одинаковые элементы
                a[j] = [j]  # избегаем зацикливания
                _tmp.append(j)
    for i in _tmp:
        if i in a: a.pop(i)  # удаляем ненужное
    return a


def investigation(data: list, depth: int, k: int = 4, r: int = 10):
    assert type(data) == list and len(data) > 0 and type(depth) == int and depth > 0, \
        "Error 0x03"
    Im = kaprekarIm(data, k, r)  # образы
    _Im = set(Im)  # множество образов
    step = 0  # текущий проход
    graph = _kaprekargraph(data, k, r)  # граф функции на данном проходе
    _ = plt.plot(data, Im, '.')
    plt.show()
    for i in range(depth):
        data, Im = list(set(Im)), kaprekarIm(list(set(Im)), k, r)  # сверхпозиция
        _ = plt.plot(data, Im, '.')
        plt.show()
        step += 1
        _graph = graph.copy()
        graph = _kaprekargraph(data, k, r)  # граф функции на данном проходе
        if len(set(Im)) == len(set(_Im)) or _graph.keys() == graph.keys():
            break  # выходим, если образ равен прообразу
        _Im = set(Im)  # образ становится прообразом (суперпозиция)
        _Im.add(0)
    if -1 in _Im:
        _Im.remove(-1)  # избавляемся от элементов проверки
    if -1 in graph:
        graph.pop(-1)  # избавляемся от элементов проверки
    return step, _Im, graph


def investigationgraph(graph: dict, depth):
    _graph = graph.copy()  # создаём копию!!! графа
    step = 0  # номер прохода
    for i in range(depth):
        step += 1
        graph = createlinks(graph)  # создаём связи
        if len(graph.keys()) == len(_graph.keys()):  # условие выхода
            break
        _graph = graph.copy()  # снова создаём копию
    return step, graph


depth = 20  # глубина поиска
k = 6  # количество цифр
r = 10  # система счисления (работает только r=10)
data = []  # прообраз
for i in range(10 ** (k - 1), 10 ** k + 1):  # все возможные элементы для такого количества цифр
    data.append(i)

# пример работы createlinks(_1)
# _1 = {1089: [1001, 1010], 9612: [1089]}  # до
# _2 = {9612: [1001, 1010, 1089]}  # после

_tmp = investigation(data, depth, k, r)
print(_tmp[0])
print(_tmp[1])
print(investigationgraph(_tmp[2], 10))
