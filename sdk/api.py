import requests
import json
from models import (
    UserResponse,
    AttributesResponse,
    CalendarResponse,
    LabelResponse,
    MemberResponse,
    EventResponse
)
import os


class TimeTreeApi():
    DEFAULT_API_ENDPOINT = 'https://timetreeapis.com'

    def __init__(self, access_token, endpoint=DEFAULT_API_ENDPOINT):
        self.endpoint = endpoint
        self.headers = {
            'Accept': 'application/vnd.timetree.v1+json',
            'Authorization': 'Bearer ' + access_token
        }

    def get_user(self):
        response = self._get('/user')
        return UserResponse.new_from_json_dict(response.json()['data'])

    def get_calendars(self, include=None):
        response = self._get('/calendars', params=include)
        return [CalendarResponse.new_from_json_dict(it) for it in response.json()['data']]

    def get_calendar(self, calendar_id, include=None):
        response = self._get(
            '/calendars/{calendar_id}'.format(calendar_id=calendar_id),
            params=include
        )
        return CalendarResponse.new_from_json_dict(response.json()['data'])

    def get_calendar_labels(self, calendar_id):
        response = self._get(
            '/calendars/{calendar_id}/labels'.format(calendar_id=calendar_id)
        )
        return [LabelResponse.new_from_json_dict(it) for it in response.json()['data']]

    def get_calendar_members(self, calendar_id):
        response = self._get(
            '/calendars/{calendar_id}/members'.format(calendar_id=calendar_id)
        )
        return [MemberResponse.new_from_json_dict(it) for it in response.json()['data']]

    def get_event(self, calendar_id, event_id, include=None):
        response = self._get(
            '/calendars/{calendar_id}/events/{event_id}'.format(calendar_id=calendar_id, event_id=event_id),
            params=include
        )
        return EventResponse.new_from_json_dict(response.json()['data'])

    def get_upcoming_events(self, calendar_id, timezone=None, days=None, include=None):
        response = self._get(
            '/calendars/{calendar_id}/upcoming_events'.format(calendar_id=calendar_id)
        )
        return [EventResponse.new_from_json_dict(it) for it in response.json()['data']]

    def _get(self, path, endpoint=None, params=None, headers=None):
        url = (endpoint or self.endpoint) + path

        if headers is None:
            headers = {}
        headers.update(self.headers)

        response = requests.get(url, headers=headers, params=params)

        self.__check_error(response)
        return response

    @staticmethod
    def __check_error(response):
        if 200 <= response.status_code < 300:
            pass
        else:
            print(response.headers)
            raise response.status_code


if __name__ == '__main__':
    api = TimeTreeApi(os.environ['TIME_TREE_API_ACCESS_TOKEN'])
    response = api.get_event(os.environ['TIME_TREE_CALENDAR_ID'], os.environ['TIME_TREE_EVENT_ID'])
    print(response.id)
