from app.io.input import input_from_file, input_from_file_pandas

def test_input_from_file1():
    test = '../../data/test_input_from_file_1.txt'
    expected = 'testing input from file 1'
    actual = input_from_file(test)
    assert actual == expected

def test_input_from_file2():
    test = '../../data/test_input_from_file_2.txt'
    expected = 'i love minions and dogs'
    actual = input_from_file(test)
    assert actual == expected

def test_input_from_file3():
    test = '../../data/test_input_from_file_3.txt'
    expected = 'testing input from file 3'
    actual = input_from_file(test)
    assert actual == expected

def test_input_from_file_pandas1():
    test = '../../data/test_input_from_file_pandas1.csv'
    expected = ['name', 'age', 'kevin', '10']
    actual = input_from_file_pandas(test).to_string().split()
    assert actual == expected

def test_input_from_file_pandas2():
    test = '../../data/test_input_from_file_pandas2.csv'
    expected = ['name', 'age', 'BOOOOB', '7']
    actual = input_from_file_pandas(test).to_string().split()
    assert actual == expected

def test_input_from_file_pandas3():
    test = '../../data/test_input_from_file_pandas3.csv'
    expected = ['0', '2222', 'idk']
    actual = input_from_file_pandas(test).to_string().split()
    assert actual == expected
