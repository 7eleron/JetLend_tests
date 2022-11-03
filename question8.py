# сложность функции в любом случае будет O(n^2)
def test1():
    _lis = [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}]
    result = []
    for x in range(len(_lis)): # цикл по всем элементам листа O(n)
        if _lis[x] not in _lis[x+1:]: # сравнение элемента O(n)
            result.append(_lis[x])
    return result # итог O(n) * O(n) = O(n^2)

def test2():
    _lis = [{"key1": "value1"}, {"k1": "v1", "k2": "v2", "k3": "v3"}, {}, {}, {"key1": "value1"}, {"key1": "value1"}, {"key2": "value2"}]
    result = []
    for x in _lis: # цикл по всем элементам листа O(n)
        if x not in result: # сравнение элемента O(n)
            result.append(x)
    return result # итог O(n) * O(n) = O(n^2)