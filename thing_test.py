import pytest
import thing

@pytest.fixture()
def data():
    return 123

def test_exposure_simple_function(data):
    assert thing.simple_function(data) == "You have called simple_function 123!"

def test_mock(data, mocker):
    mocker.patch('thing.simple_function')
    thing.simple_function.return_value = "You have mocked simple_function"
    assert thing.simple_function(data) == "You have mocked simple_function"