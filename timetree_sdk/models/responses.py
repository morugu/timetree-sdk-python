from .base import Base


class UserResponse(Base):
    def __init__(self, data=None):

        super(UserResponse, self).__init__()

        self.data = self.get_or_new_from_json_dict(data, UserDataResponse)


class UserDataResponse(Base):
    def __init__(self, id=None, type=None, attributes=None):

        super(UserDataResponse, self).__init__()

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
    def __init__(self, data=None, included=None):

        super(CalendarResponse, self).__init__()

        if isinstance(data, list):
            self.data = [self.get_or_new_from_json_dict(it, CalendarDataResponse) for it in data]
        else:
            self.data = self.get_or_new_from_json_dict(data, CalendarDataResponse)
        if included is not None:
            self.included = [self.get_or_new_from_json_dict(it, CalendarIncludedResponse) for it in included]


class CalendarDataResponse(Base):
    def __init__(self, id=None, type=None, attributes=None, relationships=None, members=None, included=None):

        super(CalendarDataResponse, self).__init__()

        self.id = id
        self.type = type
        self.attributes = self.get_or_new_from_json_dict(attributes, CalendarAttributesResponse)
        self.relationships = self.get_or_new_from_json_dict(relationships, RelationshipsResponse)


class CalendarIncludedResponse(Base):
    def __init__(self, id=None, type=None, attributes=None):

        super(CalendarIncludedResponse, self).__init__()

        self.id = id
        self.type = type
        if type == 'label':
            self.attendees = self.get_or_new_from_json_dict(attributes, LabelAttributesResponse)
        if type == 'user':
            self.attendees = self.get_or_new_from_json_dict(attributes, MemberAttributesResponse)


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
    def __init__(self, data=None):

        super(LabelResponse, self).__init__()
        self.data = [self.get_or_new_from_json_dict(it, LabelDataResponse) for it in data]


class LabelDataResponse(Base):
    def __init__(self, id=None, type=None, attributes=None):

        super(LabelDataResponse, self).__init__()

        self.id = id
        self.type = type
        self.attributes = self.get_or_new_from_json_dict(attributes, LabelAttributesResponse)


class LabelAttributesResponse(Base):

    def __init__(self, name=None, color=None):

        super(LabelAttributesResponse, self).__init__()

        self.name = name
        self.color = color


class MemberResponse(Base):
    def __init__(self, data=None):

        super(MemberResponse, self).__init__()

        self.data = [self.get_or_new_from_json_dict(it, MemberDataResponse) for it in data]


class MemberDataResponse(Base):
    def __init__(self, id=None, type=None, attributes=None):

        super(MemberDataResponse, self).__init__()

        self.id = id
        self.type = type
        self.attributes = self.get_or_new_from_json_dict(attributes, MemberAttributesResponse)


class MemberAttributesResponse(Base):
    def __init__(self, name=None, description=None, image_url=None):

        super(MemberAttributesResponse, self).__init__()

        self.name = name
        self.description = description
        self.image_url = image_url


class EventResponse(Base):
    def __init__(self, data=None):

        super(EventResponse, self).__init__()

        if isinstance(data, list):
            self.data = [self.get_or_new_from_json_dict(it, EventDataResponse) for it in data]
        else:
            self.data = self.get_or_new_from_json_dict(data, EventDataResponse)


class EventDataResponse(Base):
    def __init__(self, id=None, type=None, attributes=None, relationships=None):

        super(EventDataResponse, self).__init__()

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

        self.creator = self.get_or_new_from_json_dict(creator, EventRelationshipsCreatorResponse)
        self.label = self.get_or_new_from_json_dict(label, EventRelationshipsLabelResponse)
        self.attendees = self.get_or_new_from_json_dict(attendees, EventRelationshipsAttendeesResponse)


class EventRelationshipsCreatorResponse(Base):
    def __init__(self, data=None):

        super(EventRelationshipsCreatorResponse, self).__init__()

        self.data = self.get_or_new_from_json_dict(data, EventRelationshipsCreatorDataResponse)


class EventRelationshipsCreatorDataResponse(Base):
    def __init__(self, id=None, type=None):

        super(EventRelationshipsCreatorDataResponse, self).__init__()

        self.id = id
        self.type = type


class EventRelationshipsLabelResponse(Base):
    def __init__(self, data=None):

        super(EventRelationshipsLabelResponse, self).__init__()

        self.data = self.get_or_new_from_json_dict(data, EventRelationshipsLabelDataResponse)


class EventRelationshipsLabelDataResponse(Base):
    def __init__(self, id=None, type=None):

        super(EventRelationshipsLabelDataResponse, self).__init__()

        self.id = id
        self.type = type


class EventRelationshipsAttendeesResponse(Base):
    def __init__(self, data=None):

        super(EventRelationshipsAttendeesResponse, self).__init__()

        self.data = [self.get_or_new_from_json_dict(it, EventRelationshipsAttendeesDataResponse) for it in data]


class EventRelationshipsAttendeesDataResponse(Base):
    def __init__(self, id=None, type=None):

        super(EventRelationshipsAttendeesDataResponse, self).__init__()

        self.id = id
        self.type = type


class EventCommentResponse(Base):
    def __init__(self, data=None):

        super(EventCommentResponse, self).__init__()

        self.data = self.get_or_new_from_json_dict(data, EventCommentDataResponse)


class EventCommentDataResponse(Base):
    def __init__(self, id=None, type=None, attributes=None):

        super(EventCommentDataResponse, self).__init__()

        self.id = id
        self.type = type
        self.attributes = self.get_or_new_from_json_dict(attributes, EventCommentAttributesResponse)


class EventCommentAttributesResponse(Base):
    def __init__(self, content=None, created_at=None, updated_at=None):

        super(EventCommentAttributesResponse, self).__init__()

        self.content = content
        self.created_at = created_at
        self.updated_at = updated_at
