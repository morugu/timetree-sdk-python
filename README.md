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
print(calendar.data.attributes.name) # output your calendar name
```

# API

## User

- get_current_user

## Calendar

- get_calendars

- get_calendar

- get_calendar_labels

- get_calendar_members

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
