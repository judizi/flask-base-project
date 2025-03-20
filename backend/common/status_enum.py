from enum import Enum


class StatusEnum(Enum):
    SUCCESS = "success"
    FAIL = "fail"
    CREATED = "created"
    UPDATED = "updated"
    DELETED = "deleted"
    DUPLICATE = "duplicate"
    ERROR = "error"
    NO_CONTENT = "no_content"
    NOT_FOUND = "not_found"
    BAD_REQUEST = "bad_request"
