import json
import uuid

from rentomatic.domain import room as r
from rentomatic.serializers import room_json_serializer as ser


def test_serialize_domain_rule():
    code = uuid.uuid4()
    room = r.Room(code, size=200, price=10, longitude=-0.09998975,
                  latitude=51.75436293)

    expected_json = """{{"code": "{}", "size": 200, "price": 10, "latitude": 51.75436293, "longitude": -0.09998975}}""".format(code)
    json_room = json.dumps(room, cls=ser.RoomJsonEncoder)
    assert json_room == expected_json
