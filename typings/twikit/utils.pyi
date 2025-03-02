"""
This type stub file was generated by pyright.
"""

from datetime import datetime
from typing import (
    TYPE_CHECKING,
    Any,
    Awaitable,
    Generic,
    Iterator,
    Literal,
    TypedDict,
    TypeVar,
)

from httpx import AsyncHTTPTransport

from .client.client import Client

if TYPE_CHECKING: ...
T = TypeVar("T")

class Result(Generic[T]):
    """
    This class is for storing multiple results.
    The `next` method can be used to retrieve further results.
    As with a regular list, you can access elements by
    specifying indexes and iterate over elements using a for loop.

    Attributes
    ----------
    next_cursor : :class:`str`
        Cursor used to obtain the next result.
    previous_cursor : :class:`str`
        Cursor used to obtain the previous result.
    token : :class:`str`
        Alias of `next_cursor`.
    cursor : :class:`str`
        Alias of `next_cursor`.
    """
    def __init__(
        self,
        results: list[T],
        fetch_next_result: Awaitable | None = ...,
        next_cursor: str | None = ...,
        fetch_previous_result: Awaitable | None = ...,
        previous_cursor: str | None = ...,
    ) -> None: ...
    async def next(self) -> Result[T]:
        """
        The next result.
        """
        ...

    async def previous(self) -> Result[T]:
        """
        The previous result.
        """
        ...

    @classmethod
    def empty(cls):  # -> Self:
        ...
    def __iter__(self) -> Iterator[T]: ...
    def __getitem__(self, index: int) -> T: ...
    def __len__(self) -> int: ...
    def __repr__(self) -> str: ...

class Flow:
    def __init__(self, client: Client, guest_token: str) -> None: ...
    async def execute_task(self, *subtask_inputs, **kwargs) -> None: ...
    async def sso_init(self, provider: str) -> None: ...
    @property
    def token(self) -> str | None: ...
    @property
    def task_id(self) -> str | None: ...

def find_dict(obj: list | dict, key: str | int, find_one: bool = ...) -> list[Any]:
    """
    Retrieves elements from a nested dictionary.
    """
    ...

def httpx_transport_to_url(transport: AsyncHTTPTransport) -> str: ...
def get_query_id(url: str) -> str:
    """
    Extracts the identifier from a URL.

    Examples
    --------
    >>> get_query_id('https://twitter.com/i/api/graphql/queryid/...')
    'queryid'
    """
    ...

def timestamp_to_datetime(timestamp: str) -> datetime: ...
def build_tweet_data(raw_data: dict) -> dict: ...
def build_user_data(raw_data: dict) -> dict: ...
def flatten_params(params: dict) -> dict: ...
def b64_to_str(b64: str) -> str: ...
def find_entry_by_type(entries, type_filter):  # -> None:
    ...

FILTERS = Literal[
    "media", "retweets", "native_video", "periscope", "vine", "images", "twimg", "links"
]

class SearchOptions(TypedDict):
    exact_phrases: list[str]
    or_keywords: list[str]
    exclude_keywords: list[str]
    hashtags: list[str]
    from_user: str
    to_user: str
    mentioned_users: list[str]
    filters: list[FILTERS]
    exclude_filters: list[FILTERS]
    urls: list[str]
    since: str
    until: str
    positive: bool
    negative: bool
    question: bool
    ...

def build_query(text: str, options: SearchOptions) -> str:
    """
    Builds a search query based on the given text and search options.

    Parameters
    ----------
    text : str
        The base text of the search query.
    options : SearchOptions
        A dictionary containing various search options.
        - exact_phrases: list[str]
            List of exact phrases to include in the search query.
        - or_keywords: list[str]
            List of keywords where tweets must contain at least
            one of these keywords.
        - exclude_keywords: list[str]
            A list of keywords that the tweet must contain these keywords.
        - hashtags: list[str]
            List of hashtags to include in the search query.
        - from_user: str
            Specify a username. Only tweets from this user will
            be includedin the search.
        - to_user: str
            Specify a username. Only tweets sent to this user will
            be included in the search.
        - mentioned_users: list[str]
            List of usernames. Only tweets mentioning these users will
            be included in the search.
        - filters: list[FILTERS]
            List of tweet filters to include in the search query.
        - exclude_filters: list[FILTERS]
            List of tweet filters to exclude from the search query.
        - urls: list[str]
            List of URLs. Only tweets containing these URLs will be
            included in the search.
        - since: str
            Specify a date (formatted as 'YYYY-MM-DD'). Only tweets since
            this date will be included in the search.
        - until: str
            Specify a date (formatted as 'YYYY-MM-DD'). Only tweets until
            this date will be included in the search.
        - positive: bool
            Include positive sentiment in the search.
        - negative: bool
            Include negative sentiment in the search.
        - question: bool
            Search for tweets in questionable form.

        https://developer.twitter.com/en/docs/twitter-api/v1/rules-and-filtering/search-operators

    Returns
    -------
    str
        The constructed Twitter search query.
    """
    ...
