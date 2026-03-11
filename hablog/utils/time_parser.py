import dateparser
from dateutil import parser


def parse_time(text):
    dt = dateparser.parse(text)
    if dt:
        return dt

    try:
        return parser.parse(text)
    except Exception:
        return None
