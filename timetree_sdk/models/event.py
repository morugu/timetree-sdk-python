
from .base import Base


class Event(Base):
    def __init__(self, data=None):

        super(Event, self).__init__()


class EventData(Base):
    def __init__(self):

        super(EventData, self).__init__()


class EventAtributes(Base):
    def __init__(self):

        super(EventAtributes, self).__init__()


class EventRelationships(Base):
    def __init__(self):

        super(EventRelationships, self).__init__()


class EventRelationshipsLabel(Base):
    def __init__(self):

        super(EventRelationshipsLabel, self).__init__()


class EventRelationshipsLabelData(Base):
    def __init__(self):

        super(EventRelationshipsLabelData, self).__init__()


class EventRelationshipsAttendees(Base):
    def __init__(self):

        super(EventRelationshipsAttendees, self).__init__()


class EventRelationshipsAttendeesData(Base):
    def __init__(self):

        super(EventRelationshipsAttendeesData, self).__init__()
