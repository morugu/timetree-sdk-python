class Base(object):

    def __init__(self, **kwargs):
        pass

    @classmethod
    def new_from_json_dict(cls, d: dict):
        return cls(**d)

    @staticmethod
    def get_or_new_from_json_dict(data, cls):
        if isinstance(data, cls):
            return data
        elif isinstance(data, dict):
            return cls.new_from_json_dict(data)
        return None
