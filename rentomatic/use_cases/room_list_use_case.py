# room_list_use_case.py

from rentomatic.response_objects import response_objects as res


class RoomListUseCase:

    def __init__(self, repo):
        self.repo = repo

    def execute(self, request):
        if not request:
            return res.ResponseFailure.build_from_invalid_request_object(
                    request)
        try:
            rooms = self.repo.list(filters=request.filters)
            return res.ResponseSuccess(rooms)
        except Exception as exc:
            return res.ResponseFailure.build_system_error(
                    "{}: {}".format(exc.__class__.__name__, "{}".format(exc)))
