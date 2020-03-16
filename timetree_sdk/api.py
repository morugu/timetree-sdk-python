import requests
import json
from .models import (
    UserResponse,
    AttributesResponse,
    CalendarResponse,
    LabelResponse,
    MemberResponse,
    EventResponse,
    Event,
    EventData,
    EventAtributes,
    EventRelationships,
    EventRelationshipsLabel,
    EventRelationshipsLabelData,
    EventRelationshipsAttendees,
    EventRelationshipsAttendeesData
)


class TimeTreeApi():
    DEFAULT_API_ENDPOINT = 'https://timetreeapis.com'

    def __init__(self, access_token, endpoint=DEFAULT_API_ENDPOINT):
        self.endpoint = endpoint
        self.headers = {
            'Accept': 'application/vnd.timetree.v1+json',
            'Authorization': 'Bearer ' + access_token
        }

    def get_current_user(self):
        response = self._get('/user')
        return UserResponse.new_from_json_dict(response.json())

    def get_calendars(self, include=None):
        params = None if include is None else {'include': include}
        response = self._get('/calendars', params=params)
        return [CalendarResponse.new_from_json_dict(it) for it in response.json()]

    def get_calendar(self, calendar_id, include=None):
        params = None if include is None else {'include': include}
        response = self._get(
            '/calendars/{calendar_id}'.format(calendar_id=calendar_id),
            params=params
        )
        return CalendarResponse.new_from_json_dict(response.json())

    def get_calendar_labels(self, calendar_id):
        response = self._get(
            '/calendars/{calendar_id}/labels'.format(calendar_id=calendar_id)
        )
        return LabelResponse.new_from_json_dict(response.json())

    def get_calendar_members(self, calendar_id):
        response = self._get(
            '/calendars/{calendar_id}/members'.format(calendar_id=calendar_id)
        )
        return MemberResponse.new_from_json_dict(response.json())

    def get_event(self, calendar_id, event_id, include=None):
        response = self._get(
            '/calendars/{calendar_id}/events/{event_id}'.format(calendar_id=calendar_id, event_id=event_id),
            params=include
        )
        return EventResponse.new_from_json_dict(response.json())

    def get_upcoming_events(self, calendar_id, timezone=None, days=None, include=None):
        response = self._get(
            '/calendars/{calendar_id}/upcoming_events'.format(calendar_id=calendar_id)
        )
        return EventResponse.new_from_json_dict(response.json())

    def create_event(self, calendar_id, event):
        response = self._post(
            '/calendars/{calendar_id}/events'.format(calendar_id=calendar_id),
            data=event.as_json_string()
        )
        return EventResponse.new_from_json_dict(response.json())

    def delete_event(self, calendar_id, event_id):
        response = self._delete(
            '/calendars/{calendar_id}/events/{event_id}'.format(calendar_id=calendar_id, event_id=event_id)
        )
        return response.status_code

    def _get(self, path, params=None, headers=None):
        url = self.endpoint + path
        if headers is None:
            headers = {}
        headers.update(self.headers)

        response = requests.get(url, headers=headers, params=params)

        self.__check_error(response)
        return response

    def _post(self, path, data=None, headers=None):
        url = self.endpoint + path

        if headers is None:
            headers = {'Content-Type': 'application/json'}
        headers.update(self.headers)

        response = requests.post(
            url, headers=headers, data=data
        )

        self.__check_error(response)
        return response

    def _delete(self, path, data=None, headers=None):
        url = self.endpoint + path

        if headers is None:
            headers = {'Content-Type': 'application/json'}
        headers.update(self.headers)

        response = requests.delete(
            url, headers=headers, data=data
        )

        self.__check_error(response)
        return response

    @staticmethod
    def __check_error(response):
        if 200 <= response.status_code < 300:
            pass
        else:
            print(response.headers)
            raise response.status_code
