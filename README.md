# TimeTree SDK for Python

[TimeTree API](https://developers.timetreeapp.com/en/docs/api) SDK for Python.

# Installing

```
$ pip install timetree-sdk
```

# Usage

```python
from timetree_sdk import TimeTreeApi

api = TimeTreeApi('TIME_TREE_API_ACCESS_TOKEN')
calendar = api.get_calendar('TIME_TREE_CALENDAR_ID')
print(calendar.data.attributes.name) # calendar name
```

# API

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
calendar = api.get_calendar('TIME_TREE_CALENDAR_ID')
print(calendar.data.attributes.name) # calendar name
```

### get_calendar_labels

```python
labels = api.get_calendar_labels('TIME_TREE_CALENDAR_ID')
print(labels.data[0].attributes.name) # first calender's label name
```

### get_calendar_members

```python
members = api.get_calendar_members('TIME_TREE_CALENDAR_ID')
print(members.data[0].attributes.name) # first calender's member name
```

## Event

- get_event

- get_upcoming_events

- create_event

- delete_event

- update event

## Event Comment

- create comment to event

# Documentation

Official API documentation

English: https://developers.timetreeapp.com/en/docs/api

Japanese: https://developers.timetreeapp.com/ja/docs/api
