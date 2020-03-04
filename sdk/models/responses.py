from .base import Base


class UserResponse(Base):
    def __init__(self, id=None, type=None, attributes=None):

        super(UserResponse, self).__init__()

        self.id = id
        self.type = type
        self.attributes = self.get_or_new_from_json_dict(attributes, AttributesResponse)


class AttributesResponse(Base):
    def __init__(self, name=None, description=None, image_url=None):

        super(AttributesResponse, self).__init__()

        self.name = name
        self.description = description
        self.image_url = image_url
