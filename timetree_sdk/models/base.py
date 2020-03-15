import json


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

    def as_json_string(self):
        return json.dumps(self.as_json_dict(), sort_keys=True)

    def as_json_dict(self):
        data = {}
        for key, value in self.__dict__.items():
            if isinstance(value, (list, tuple, set)):
                data[key] = list()
                for item in value:
                    if hasattr(item, 'as_json_dict'):
                        data[key].append(item.as_json_dict())
                    else:
                        data[key].append(item)

            elif hasattr(value, 'as_json_dict'):
                data[key] = value.as_json_dict()
            elif value is not None:
                data[key] = value

        return data
