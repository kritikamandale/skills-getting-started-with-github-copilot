import pytest
from fastapi import HTTPException

from src.app import activities, signup_for_activity


def test_signup_rejects_duplicate_email():
    activity_name = "Chess Club"
    email = "duplicate-test@mergington.edu"

    signup_for_activity(activity_name, email)

    try:
        with pytest.raises(HTTPException) as error:
            signup_for_activity(activity_name, email)

        assert error.value.status_code == 400
        assert email in error.value.detail
        assert activities[activity_name]["participants"].count(email) == 1
    finally:
        activities[activity_name]["participants"].remove(email)
