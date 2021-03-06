import uuid
from rentomatic.domain import room as r


def test_room_model_init():
    code = uuid.uuid4()
    room = r.Room(code, size=200, price=10, longitude=-0.09998975,
                  latitude=51.75436293)
    assert room.code == code
    assert room.size == 200
    assert room.price == 10
    assert room.longitude == -0.09998975
    assert room.latitude == 51.75436293


def test_room_model_from_dict():
    code = uuid.uuid4()
    adict = {
        'code': code, 'size': 200, 'price': 10, 'longitude': -0.09998975,
        'latitude': 51.75436293
    }
    room = r.Room.from_dict(adict)

    assert room.code == code
    assert room.size == 200
    assert room.price == 10
    assert room.longitude == -0.09998975
    assert room.latitude == 51.75436293


def test_room_to_dict():
    adict = {
        'code': uuid.uuid4(), 'size': 200, 'price': 10,
        'longitude': -0.09998975,
        'latitude': 51.75436293
    }
    room = r.Room.from_dict(adict)
    assert adict == room.to_dict()


def test_equality_operator():
    code = uuid.uuid4()
    room1 = r.Room(code, size=200, price=10, longitude=-0.09998975,
                   latitude=51.75436293)

    room2 = r.Room(code, size=200, price=10, longitude=-0.09998975,
                   latitude=51.75436293)
    assert room1 == room2
