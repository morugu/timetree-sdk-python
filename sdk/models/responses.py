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


class CalendarResponse(Base):
    def __init__(self, id=None, type=None, attributes=None, relationships=None, members=None):

        super(CalendarResponse, self).__init__()

        self.id = id
        self.type = type
        self.attributes = self.get_or_new_from_json_dict(attributes, CalendarAttributesResponse)


class CalendarAttributesResponse(Base):
    def __init__(self, name=None, created_at=None, description=None, image_url=None, color=None, order=None):

        super(CalendarAttributesResponse, self).__init__()

        self.name = name
        self.created_at = created_at
        self.description = description
        self.image_url = image_url
        self.color = color
        self.order = order


class RelationshipsResponse(Base):
    def __init__(self, labels, members):

        super(RelationshipsResponse, self).__init__()

        self.labels = [self.get_or_new_from_json_dict(it, LabelResponse) for it in labels]
        self.members = [self.get_or_new_from_json_dict(it, MemberResponse) for it in members]


class LabelResponse(Base):
    def __init__(self, id=None, type=None, attributes=None):

        super(LabelResponse, self).__init__()

        self.id = id
        self.type = type
        self.attributes = attributes


class LabelAttributesResponse(Base):

    def __init__(self, name=None, color=None):

        super(LabelAttributesResponse, self).__init__()

        self.name = name
        self.color = color


class MemberResponse(Base):
    def __init__(self, id=None, type=None, attributes=None):

        super(MemberResponse, self).__init__()

        self.id = id
        self.type = type
        self.attributes = self.get_or_new_from_json_dict(attributes, MemberAttributeResponse)


class MemberAttributeResponse(Base):
    def __init__(self, name=None, description=None, image_url=None):

        super(MemberAttributeResponse, self).__init__()

        self.name = name
        self.description = description
        self.image_url = image_url
