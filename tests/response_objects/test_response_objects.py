import pytest

from rentomatic.response_objects import response_objects as res
from rentomatic.request_objects import room_list_request_object as req


@pytest.fixture
def response_value():
    return {'key': ['value1', 'value2']}


@pytest.fixture
def response_type():
    return 'ResponseError'


@pytest.fixture
def response_message():
    return 'This is a response message'


def test_response_success_true():
    assert bool(res.ResponseSuccess()) is True


def test_response_success_has_type_and_value(response_value):
    '''instantiate response from value and check whether the type is success
    and the value of the response object is the same as the value passed in'''
    response = res.ResponseSuccess(response_value)

    '''type of response object is used as the indicator of success or failure
    represented as a string'''
    assert response.type == res.ResponseSuccess.SUCCESS
    assert response.value == response_value


def test_response_failure_is_false(response_type, response_message):
    assert bool(res.ResponseFailure(response_type, response_message)) is False


def test_response_failure_has_type_and_message(
        response_type, response_message):
    response = res.ResponseFailure(response_type, response_message)

    assert response.type == response_type
    assert response.message == response_message


def test_response_failure_contains_value(response_type, response_message):
    response = res.ResponseFailure(response_type, response_message)

    assert response.value == {'type': response_type,
                              'message': response_message}


def test_response_failure_initialisation_with_exception():
    response = res.ResponseFailure(response_type,
                                   Exception('Just an error message'))

    assert bool(response) is False
    assert response.type == response_type
    assert response.message == 'Exception: Just an error message'


def test_response_failure_from_empty_invalid_requst_object():
    response = res.ResponseFailure.build_from_invalid_request_object(
            req.InvalidRequestObject())

    assert bool(response) is False
    assert response.type == res.ResponseFailure.PARAMETERS_ERROR


def test_response_failure_from_invalid_request_object_with_errors():
    request_object = req.InvalidRequestObject()
    request_object.add_error('path', 'Is mandatory')
    request_object.add_error('path', "can't be blank")

    response = res.ResponseFailure.build_from_invalid_request_object(
            request_object)
    assert bool(response) is False
    assert response.type == res.ResponseFailure.PARAMETERS_ERROR
    assert response.message == "path: Is mandatory\npath: can't be blank"


def test_response_failure_build_resource_error():
    '''if a response can't be returned because resources aren't available,
    a suitable response failure should be returned'''

    response = res.ResponseFailure.build_resource_error('test message')

    assert bool(response) is False
    assert response.type == res.ResponseFailure.RESOURCE_ERROR
    assert response.message == 'test message'


def test_response_failure_build_system_error():
    '''if a response can't be returned because of a system error,
    a suitable response failure should be returned'''

    response = res.ResponseFailure.build_system_error('test message')

    assert bool(response) is False
    assert response.type == res.ResponseFailure.SYSTEM_ERROR
    assert response.message == 'test message'


def test_response_failure_build_parameters_error():
    '''if a response can't be returned because of a paramters error,
    a suitable response failure should be returned'''

    response = res.ResponseFailure.build_parameters_error('test message')

    assert bool(response) is False
    assert response.type == res.ResponseFailure.PARAMETERS_ERROR
    assert response.message == 'test message'
