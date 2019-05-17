import json
from unittest import mock

from rentomatic.domain.room import Room

room_dict = {
    'code': '3251a5bd-86be-428d-8ae9-6e51a8048c33',
    'size': 200,
    'price': 10,
    'longitude': -0.09998975,
    'latitude': 51.75436293
}
room = Room.from_dict(room_dict)
rooms = [room]

@mock.patch('rentomatic.use_cases.room_list_use_case.RoomListUseCase')
def test_get(mock_use_case, client):
    mock_use_case().execute.return_value = rooms
    # note we  are not RUNNNING the use case itself, just mocking it

    http_response = client.get('/rooms')
    # this is the key part: we get the API endpoint which sends an
    # HTTP GET request and collects the servers response.

    assert json.loads(http_response.data.decode('UTF-8')) == [room_dict]
    #check it's a JSON, and in the format were expected
    mock_use_case().execute.assert_called_with()
    # check executre is called with no parameters
    assert http_response.status_code == 200
    # check reponse is 200 'OK'
    assert http_response.mimetype == 'application/json'
    # check the reports is JSON
