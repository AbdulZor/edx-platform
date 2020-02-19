"""
API for calendar syncing Course dates with a User.
"""
import logging


log = logging.getLogger(__name__)


def get_calendar_event_id(user, block_key):
    """
    Creates a unique event id based on a user and a course block key

    user (User): The user requesting a calendar event
    block_key (str): The block key containing the date for the calendar event

    returns a string representing the event id
    """
    return user.username + '.' + block_key
