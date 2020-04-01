# TimeTree SDK for Python

[TimeTree API](https://developers.timetreeapp.com/en/docs/api) SDK for Python.

# Installing

```
$ pip install timetree-sdk
```

# Usage

```python
from timetree_sdk import TimeTreeApi

api = TimeTreeApi('API_ACCESS_TOKEN')
calendar = api.get_calendar('CALENDAR_ID')
print(calendar.data.attributes.name) # calendar name
```

# API

## Oauth

### get_oauth_authorize_url

```python
oauth_authorize_url = TimeTreeApi.get_oauth_authorize_url('CLIENT_ID', 'REDIRECT_URI', 'RESPONSE_TYPE', 'STATE')
```

## User

### get_current_user

```python
user = api.get_current_user()
print(user.data.attributes.name) # user name
```

## Calendar

### get_calendars

```python
calenders = api.get_calendars()
print(calenders.data[0].attributes.name) # first calender name
```

### get_calendar

```python
calendar = api.get_calendar('CALENDAR_ID')
print(calendar.data.attributes.name) # calendar name
```

### get_calendar_labels

```python
labels = api.get_calendar_labels('CALENDAR_ID')
print(labels.data[0].attributes.name) # first calender's label name
```

### get_calendar_members

```python
members = api.get_calendar_members('CALENDAR_ID')
print(members.data[0].attributes.name) # first calender's member name
```

## Event

### get_event

```python
event = api.get_event('CALENDAR_ID', 'EVENT_ID')
print(event.data.attributes.title) # event title
```

### get_upcoming_events

```python
events = api.get_upcoming_events('CALENDAR_ID', 'Asia/Tokyo', 7)
print(events.data[0].attributes.title) # most recent event title in 7 days
```

### create_event

```python
event = Event(
    data=EventData(
        attributes=EventAttributes(
            title='Title',
            category='schedule',
            all_day=False,
            start_at='2020-04-04T11:00:00.000Z',
            end_at='2020-04-04T13:00:00.000Z',
            description='Description',
            location='Location',
            start_timezone='Japan',
            end_timezone='Japan'
        ),
        relationships=EventRelationships(
            label=EventRelationshipsLabel(
                data=EventRelationshipsLabelData(
                    id='LABEL_ID',
                    type='label'
                )
            ),
            attendees=EventRelationshipsAttendees(
                data=[EventRelationshipsAttendeesData(
                    id='USER_ID',
                    type='user'
                )]
            )
        )
    )
)
response = api.create_event('CALENDAR_ID', event)
print(response.data.attributes.title) # Title
```

### delete_event

```python
status_code = api.delete_event('CALENDAR_ID', 'EVENT_ID')
print(status_code) # 204 on success
```

### update event

```python
event = Event(
    data=EventData(
        attributes=EventAttributes(
            title='Updated Title',
            category='schedule',
            all_day=False,
            start_at='2020-04-04T11:30:00.000Z',
            end_at='2020-04-04T13:30:00.000Z',
            description='Description',
            location='Location',
            start_timezone='Japan',
            end_timezone='Japan'
        ),
        relationships=EventRelationships(
            label=EventRelationshipsLabel(
                data=EventRelationshipsLabelData(
                    id='LABEL_ID',
                    type='label'
                )
            ),
            attendees=EventRelationshipsAttendees(
                data=[EventRelationshipsAttendeesData(
                    id='USER_ID',
                    type='user'
                )]
            )
        )
    )
)
response = api.create_event('CALENDAR_ID', 'EVENT_ID', event)
print(response.data.attributes.title) # Updated Title
```

## Event Comment

### create comment to event

```python
comment = EventComment(
    data=EventCommentData(
        attributes=EventCommentAttributes(
            content='Hello, world'
        )
    )
)
event_comment = api.create_event_comment('CALENDAR_ID', 'EVENT_ID', comment)
print(event_comment.data.attributes.content) # Hello, world
```

# Documentation

Official API documentation

English: https://developers.timetreeapp.com/en/docs/api

Japanese: https://developers.timetreeapp.com/ja/docs/api
