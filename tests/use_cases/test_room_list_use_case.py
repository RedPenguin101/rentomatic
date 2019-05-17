import pytest
import uuid
from unittest import mock

from rentomatic.domain import room as r
from rentomatic.use_cases import room_list_use_case as uc

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
    result = room_list_use_case.execute()

    repo.list.assert_called_with()
    assert result == domain_rooms
