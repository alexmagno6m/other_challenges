# importante sobre el funcionamiento basico de los test unitarios
# corresponde al dia 28 del challenge 20 days of code, hackerrank.
# day 27 ubit test

#esta es la funcion a probar, dada un arreglo entrega el indice del elemento de menor valor
#si la lista esta vacia devuelve error
def minimum_index(seq):
    if len(seq) == 0:
        raise ValueError("Cannot get the minimum value index from an empty sequence")
    min_idx = 0
    for i in range(1, len(seq)):
        if seq[i] < seq[min_idx]:
            min_idx = i

    return min_idx

#en esta clase se prueba la efectividad si la lista esta vacia
class TestDataEmptyArray(object):

    @staticmethod
    def get_array():
        return []
# esta clase prueba el indice del elemento de menor valor
class TestDataUniqueValues(object):

    @staticmethod
    def get_array():
        return [3,1,2]

    @staticmethod
    def get_expected_result():
        return 1

# esta clase prueba el indice mas pequeño de dos elementos con el menor
#valor duplicados
class TestDataExactlyTwoDifferentMinimums(object):

    @staticmethod
    def get_array():
        return [3,1,1]

    @staticmethod
    def get_expected_result():
        return 1


# este es el desarrollo de cada una de las pruebas
def TestWithEmptyArray():
    try:
        seq = TestDataEmptyArray.get_array()
        result = minimum_index(seq)
    except ValueError as e:
        pass
    else:
        assert False


def TestWithUniqueValues():
    seq = TestDataUniqueValues.get_array()
    assert len(seq) >= 2
    assert len(list(set(seq))) == len(seq)

    expected_result = TestDataUniqueValues.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result


def TestiWithExactyTwoDifferentMinimums():
    seq = TestDataExactlyTwoDifferentMinimums.get_array()
    assert len(seq) >= 2
    tmp = sorted(seq)
    assert tmp[0] == tmp[1] and (len(tmp) == 2 or tmp[1] < tmp[2])

    expected_result = TestDataExactlyTwoDifferentMinimums.get_expected_result()
    result = minimum_index(seq)
    assert result == expected_result

TestWithEmptyArray()
TestWithUniqueValues()
TestiWithExactyTwoDifferentMinimums()
print("OK")