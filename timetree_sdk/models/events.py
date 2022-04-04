
from .base import Base


class Event(Base):
    def __init__(self, data=None):

        super(Event, self).__init__()

        self.data = self.get_or_new_from_json_dict(data, EventData)


class EventData(Base):
    def __init__(self, attributes=None, relationships=None):

        super(EventData, self).__init__()

        self.attributes = self.get_or_new_from_json_dict(attributes, EventAttributes)
        self.relationships = self.get_or_new_from_json_dict(relationships, EventRelationships)


class EventAttributes(Base):
    def __init__(self, title=None, category=None, all_day=None, start_at=None, start_timezone=None, end_at=None, end_timezone=None, description=None, location=None, location_lat=None, location_lon=None, url=None, relationships=None):

        super(EventAttributes, self).__init__()

        self.title = title
        self.category = category
        self.all_day = all_day
        self.start_at = start_at
        self.start_timezone = start_timezone
        self.end_at = end_at
        self.end_timezone = end_timezone
        self.description = description
        self.location = location
        self.location_lat = location_lat
        self.location_lon = location_lon
        self.url = url
        self.label = self.get_or_new_from_json_dict(relationships, EventRelationships)


class EventRelationships(Base):
    def __init__(self, label=None, attendees=None):

        super(EventRelationships, self).__init__()

        self.label = self.get_or_new_from_json_dict(label, EventRelationshipsLabel)
        self.attendees = self.get_or_new_from_json_dict(attendees, EventRelationshipsAttendees)


class EventRelationshipsLabel(Base):
    def __init__(self, data=None):

        super(EventRelationshipsLabel, self).__init__()

        self.data = self.get_or_new_from_json_dict(data, EventRelationshipsLabelData)


class EventRelationshipsLabelData(Base):
    def __init__(self, id=None, type=None):

        super(EventRelationshipsLabelData, self).__init__()

        self.id = id
        self.type = type


class EventRelationshipsAttendees(Base):
    def __init__(self, data=None):

        super(EventRelationshipsAttendees, self).__init__()

        self.data = [self.get_or_new_from_json_dict(it, EventRelationshipsAttendeesData) for it in data]


class EventRelationshipsAttendeesData(Base):
    def __init__(self, id=None, type=None):

        super(EventRelationshipsAttendeesData, self).__init__()

        self.id = id
        self.type = type


class EventComment(Base):
    def __init__(self, data=None):

        super(EventComment, self).__init__()

        self.data = self.get_or_new_from_json_dict(data, EventCommentData)


class EventCommentData(Base):
    def __init__(self, attributes=None):

        super(EventCommentData, self).__init__()

        self.attributes = self.get_or_new_from_json_dict(attributes, EventCommentAttributes)


class EventCommentAttributes(Base):
    def __init__(self, content=None):

        super(EventCommentAttributes, self).__init__()

        self.content = content
