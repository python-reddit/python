"""Get the current Python events from an ics file and format them into a markdown string."""
from __future__ import annotations

from re import search
from typing import Any

import anyio
import arrow
from httpx import AsyncClient, codes
from icalendar import Calendar

__all__ = ("FetchFailedError", "fetch_ics", "format_event", "main", "parse_ics_to_md", "write_to_md_file")


class FetchFailedError(Exception):
    """Raised when the fetch fails for any reason."""


async def fetch_ics(url: str) -> Any:  # noqa: ANN401
    """Fetches the ics file from the given url and returns the text content.

    Args:
        url (str): The url to fetch the ics file from

    Raises:
        FetchFailedException: If the fetch fails for any reason

    Returns:
        str: The text content of the ics file
    """
    async with AsyncClient(follow_redirects=True) as client:
        resp = await client.get(url)
        if resp.status_code != codes.OK:
            msg = f"Status code: {resp.status_code}"
            raise FetchFailedError(msg)
    return resp.text


def format_event(event_time_start: arrow.Arrow, event_time_end: arrow.Arrow | None, summary: str, link: str) -> str:
    """Formats the event into a markdown string.

    Args:
        event_time_start (arrow.Arrow): The start time of the event
        event_time_end (arrow.Arrow): The end time of the event
        summary (str): The summary of the event
        link (str): The link to the event

    Returns:
        str: The markdown string
    """
    start_date_str = event_time_start.format("D MMM")
    end_date_str = event_time_end.format("D MMM") if event_time_end else ""
    date_range = f"{start_date_str} - {end_date_str}" if end_date_str else start_date_str
    return f"* [{summary}]({link}) {date_range}\n"


def parse_ics_to_md(ics_str: str) -> str:
    """Parses the ics string into a markdown string.

    Args:
        ics_str (str): The ics string to parse

    Returns:
        str: The markdown string
    """
    cal = Calendar.from_ical(ics_str)
    now = arrow.now()
    next_month = now.shift(months=1)

    current_events = []
    future_events = []

    for component in cal.walk():
        if component.name == "VEVENT":
            event_time_start = arrow.get(component.get("dtstart").dt)
            event_time_end = arrow.get(component.get("dtend").dt) if component.get("dtend") else None
            description = component.get("description")
            summary = component.get("summary")

            search_result = search(r'(?P<url>https?://[^\s">]+)', description) if description else None
            link = search_result.group("url") if search_result else ""

            event_md = format_event(event_time_start, event_time_end, summary, link)

            if now <= event_time_start < next_month:
                future_events.append(event_md)
            elif now >= event_time_start and (event_time_end is None or now <= event_time_end):
                current_events.append(event_md)

    full_calendar_link = "[Full Events Calendar](https://www.python.org/events/python-events)\n\n"
    current_events_str = "".join(current_events)
    future_events_str = "".join(future_events)

    return f"{full_calendar_link}### Current Events\n{current_events_str}\n### Future Events\n{future_events_str}"


async def write_to_md_file(content: str, file_path: str) -> None:
    """Writes the content to the given file path.

    Args:
        content (str): The content to write
        file_path (str): The file path to write to
    """
    async with await anyio.open_file(file_path, "w") as f:
        await f.write(content)


async def main() -> None:
    """Make events go brr."""
    ics_url = (
        "https://www.google.com/calendar/ical/j7gov1cmnqr9tvg14k621j7t5c@group.calendar.google.com/public/basic.ics"
    )
    ics_str = await fetch_ics(ics_url)
    events_md = parse_ics_to_md(ics_str)
    await write_to_md_file(events_md, "events.md")


if __name__ == "__main__":
    anyio.run(main)
