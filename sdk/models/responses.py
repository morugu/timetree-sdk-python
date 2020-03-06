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


class EventResponse(Base):
    def __init__(self, id=None, type=None, attributes=None, relationships=None):

        super(EventResponse, self).__init__()

        self.id = id
        self.type = type
        self.attributes = self.get_or_new_from_json_dict(attributes, EventAttributes)
        self.relationships = self.get_or_new_from_json_dict(relationships, EventRelationshipsResponse)


class EventAttributes(Base):
    def __init__(self, category=None, title=None, all_day=None, start_at=None, start_timezone=None, end_at=None, end_timezone=None, recurrence=None, recurring_uuid=None, description=None, location=None, url=None, updated_at=None, created_at=None):

        super(EventAttributes, self).__init__()

        self.category = category
        self.title = title
        self.all_day = all_day
        self.start_at = start_at
        self.start_timezone = start_timezone
        self.end_at = end_at
        self.end_timezone = end_timezone
        self.recurrence = recurrence
        self.recurring_uuid = recurring_uuid
        self.description = description
        self.location = location
        self.url = url
        self.updated_at = updated_at
        self.created_at = created_at


class EventRelationshipsResponse(Base):
    def __init__(self, creator=None, label=None, attendees=None):

        super(EventRelationshipsResponse, self).__init__()

        self.creator = self.get_or_new_from_json_dict(creator['data'], EventRelationshipsCreatorResponse)
        self.label = self.get_or_new_from_json_dict(label['data'], EventRelationshipsLabelResponse)
        self.attendees = [self.get_or_new_from_json_dict(it, EventRelationshipsAttendeesResponse) for it in attendees['data']]


class EventRelationshipsCreatorResponse(Base):
    def __init__(self, id=None, type=None):

        super(EventRelationshipsCreatorResponse, self).__init__()

        self.id = id
        self.type = type


class EventRelationshipsLabelResponse(Base):
    def __init__(self, id=None, type=None):

        super(EventRelationshipsLabelResponse, self).__init__()

        self.id = id
        self.type = type


class EventRelationshipsAttendeesResponse(Base):
    def __init__(self, id=None, type=None):

        super(EventRelationshipsAttendeesResponse, self).__init__()

        self.id = id
        self.type = type
