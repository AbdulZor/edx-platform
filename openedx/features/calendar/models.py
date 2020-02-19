"""
Models for Calendar
"""


from django.contrib.auth.models import User
from django.db import models

from opaque_keys.edx.django.models import CourseKeyField


class UserCalendar(models.Model):
    """
    Model to track if a user has the calendar integration enabled for a specific Course

    .. no_pii:
    """
    user = models.ForeignKey(User, db_index=True, on_delete=models.CASCADE)
    course_key = CourseKeyField(max_length=255, db_index=True)
    enabled = models.BooleanField(default=False)
