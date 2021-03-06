# rest/room.py

import json

from flask import Blueprint, Response, request

from rentomatic.repository import postgresrepo as pr
from rentomatic.use_cases import room_list_use_case as uc
from rentomatic.serializers import room_json_serializer as ser
from rentomatic.request_objects import room_list_request_object as req
from rentomatic.response_objects import response_objects as res

blueprint = Blueprint('room', __name__)

STATUS_CODES = {
        res.ResponseSuccess.SUCCESS: 200,
        res.ResponseFailure.RESOURCE_ERROR: 404,
        res.ResponseFailure.PARAMETERS_ERROR: 400,
        res.ResponseFailure.SYSTEM_ERROR: 500
        }

connection_data = {
        'dbname': 'rentomaticdb',
        'user': 'postgres',
        'password': 'rentomaticdb',
        'host': 'localhost'
        }


@blueprint.route('/rooms', methods=['GET'])
def room():
    query_string = {'filters': {}}

    for arg, values in request.args.items():
        if arg.startswith('filter_'):
            query_string['filters'][arg.replace('filter_', '')] = values

    request_object = req.RoomListRequestObject.from_dict(query_string)

    repo = pr.PostgresRepo(connection_data)
    use_case = uc.RoomListUseCase(repo)

    response_object = use_case.execute(request_object)

    return Response(json.dumps(response_object.value, cls=ser.RoomJsonEncoder),
                    mimetype='application/json',
                    status=STATUS_CODES[response_object.type])
