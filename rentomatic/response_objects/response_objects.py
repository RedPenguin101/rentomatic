class ResponseFailure:
    PARAMETERS_ERROR = 'ParametersError'
    RESOURCE_ERROR = 'ResourceError'
    SYSTEM_ERROR = 'SystemError'

    def __init__(self, type, message):
        self.type = type
        self.message = self._format_message(message)

    def _format_message(self, msg):
        if isinstance(msg, Exception):
            return "{}: {}".format(msg.__class__.__name__, "{}".format(msg))
        return msg

    @property
    def value(self):
        return {'type':self.type, 'message':self.message}

    @classmethod
    def build_from_invalid_request_object(cls, request_object):
        message = "\n".join(["{}: {}".format(err['parameter'], err['message'])
            for err in request_object.errors])
        return cls(cls.PARAMETERS_ERROR, message)

    @classmethod
    def build_resource_error(cls, message):
        return cls(cls.RESOURCE_ERROR, message)

    @classmethod
    def build_system_error(cls, message):
        return cls(cls.SYSTEM_ERROR, message)

    @classmethod
    def build_parameters_error(cls, message):
        return cls(cls.PARAMETERS_ERROR, message)

    def __bool__(self):
        return False

class ResponseSuccess:
    SUCCESS = 'Success'
    def __init__(self, value=None):
        self.value = value
        self.type = self.SUCCESS

    def __bool__(self):
        return True
