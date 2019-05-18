import pytest
import uuid
from unittest import mock

from rentomatic.domain import room as r
from rentomatic.use_cases import room_list_use_case as uc
from rentomatic.request_objects import room_list_request_object as req
from rentomatic.response_objects import response_objects as res

@pytest.fixture
def domain_rooms():
    room_1 = r.Room(uuid.uuid4, size=200, price=10,
                    longitude=-0.09998975, latitude=51.75436293)
    room_2 = r.Room(uuid.uuid4, size=200, price=10,
                    longitude=-0.09998975, latitude=51.75436293)
    room_3 = r.Room(uuid.uuid4, size=200, price=10,
                    longitude=-0.09998975, latitude=51.75436293)
    room_4 = r.Room(uuid.uuid4, size=200, price=10,
                    longitude=-0.09998975, latitude=51.75436293)
    return [room_1, room_2, room_3, room_4]

def test_room_list_without_parameters(domain_rooms):
    '''
    mock the repo so it provides a list method that returns the list of
    models. then initialise the uc and execute it. then check the repo
    method was called without params. then check the result of the
    uc execution is the same as the full list of mock.
    '''
    repo = mock.Mock()
    repo.list.return_value = domain_rooms

    room_list_use_case = uc.RoomListUseCase(repo)
    request = req.RoomListRequestObject()

    response = room_list_use_case.execute(request)

    assert bool(response) is True
    repo.list.assert_called_with(filters=None)
    assert response.value == domain_rooms


def test_room_list_with_filters(domain_rooms):
    repo = mock.Mock()
    repo.list.return_value = domain_rooms

    room_list_use_case = uc.RoomListUseCase(repo)
    qry_filters = {'code__eq':5}
    request_object = req.RoomListRequestObject.from_dict(
            {'filters':qry_filters})

    response_object = room_list_use_case.execute(request_object)

    assert bool(response_object) is True
    repo.list.assert_called_with(filters=qry_filters)
    assert response_object.value == domain_rooms

def test_room_list_handles_generic_error():
    repo = mock.Mock()
    repo.list.side_effect = Exception('just an error message')

    room_list_use_case = uc.RoomListUseCase(repo)
    request_object = req.RoomListRequestObject.from_dict({})

    response_object = room_list_use_case.execute(request_object)

    assert bool(response_object) is False
    assert response_object.value == {
            'type':res.ResponseFailure.SYSTEM_ERROR,
            'message':"Exception: just an error message"
            }


def test_room_list_handles_bad_request():
    repo = mock.Mock()
    room_list_use_case = uc.RoomListUseCase(repo)
    request_object = req.RoomListRequestObject.from_dict({'filters':5})

    response_object = room_list_use_case.execute(request_object)

    assert bool(response_object) is False
    assert response_object.value == {
            'type':res.ResponseFailure.PARAMETERS_ERROR,
            'message':"filters: Is not iterable"
            }
