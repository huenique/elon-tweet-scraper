"""
This type stub file was generated by pyright.
"""

from datetime import datetime
from typing import TYPE_CHECKING

from httpx import Response

from .client.client import Client
from .tweet import Tweet
from .user import User
from .utils import Result

if TYPE_CHECKING: ...

class List:
    """
    Class representing a Twitter List.

    Attributes
    ----------
    id : :class:`str`
        The unique identifier of the List.
    created_at : :class:`int`
        The timestamp when the List was created.
    default_banner : :class:`dict`
        Information about the default banner of the List.
    banner : :class:`dict`
        Information about the banner of the List. If custom banner is not set,
        it defaults to the default banner.
    description : :class:`str`
        The description of the List.
    following : :class:`bool`
        Indicates if the authenticated user is following the List.
    is_member : :class:`bool`
        Indicates if the authenticated user is a member of the List.
    member_count : :class:`int`
        The number of members in the List.
    mode : {'Private', 'Public'}
        The mode of the List, either 'Private' or 'Public'.
    muting : :class:`bool`
        Indicates if the authenticated user is muting the List.
    name : :class:`str`
        The name of the List.
    pinning : :class:`bool`
        Indicates if the List is pinned.
    subscriber_count : :class:`int`
        The number of subscribers to the List.
    """
    def __init__(self, client: Client, data: dict) -> None: ...
    @property
    def created_at_datetime(self) -> datetime: ...
    async def edit_banner(self, media_id: str) -> Response:
        """
        Edit the banner image of the list.

        Parameters
        ----------
        media_id : :class:`str`
            The ID of the media to use as the new banner image.

        Returns
        -------
        :class:`httpx.Response`
            Response returned from twitter api.

        Examples
        --------
        >>> media_id = await client.upload_media('image.png')
        >>> await media.edit_banner(media_id)
        """
        ...

    async def delete_banner(self) -> Response:
        """
        Deletes the list banner.
        """
        ...

    async def edit(
        self,
        name: str | None = ...,
        description: str | None = ...,
        is_private: bool | None = ...,
    ) -> List:
        """
        Edits list information.

        Parameters
        ----------
        name : :class:`str`, default=None
            The new name for the list.
        description : :class:`str`, default=None
            The new description for the list.
        is_private : :class:`bool`, default=None
            Indicates whether the list should be private
            (True) or public (False).

        Returns
        -------
        :class:`List`
            The updated Twitter list.

        Examples
        --------
        >>> await list.edit(
        ...     'new name', 'new description', True
        ... )
        """
        ...

    async def add_member(self, user_id: str) -> Response:
        """
        Adds a member to the list.
        """
        ...

    async def remove_member(self, user_id: str) -> Response:
        """
        Removes a member from the list.
        """
        ...

    async def get_tweets(
        self, count: int = ..., cursor: str | None = ...
    ) -> Result[Tweet]:
        """
        Retrieves tweets from the list.

        Parameters
        ----------
        count : :class:`int`, default=20
            The number of tweets to retrieve.
        cursor : :class:`str`, default=None
            The cursor for pagination.

        Returns
        -------
        Result[:class:`Tweet`]
            A Result object containing the retrieved tweets.

        Examples
        --------
        >>> tweets = await list.get_tweets()
        >>> for tweet in tweets:
        ...    print(tweet)
        <Tweet id="...">
        <Tweet id="...">
        ...
        ...

        >>> more_tweets = await tweets.next()  # Retrieve more tweets
        >>> for tweet in more_tweets:
        ...     print(tweet)
        <Tweet id="...">
        <Tweet id="...">
        ...
        ...
        """
        ...

    async def get_members(
        self, count: int = ..., cursor: str | None = ...
    ) -> Result[User]:
        """Retrieves members of the list.

        Parameters
        ----------
        count : :class:`int`, default=20
            Number of members to retrieve.

        Returns
        -------
        Result[:class:`User`]
            Members of the list

        Examples
        --------
        >>> members = list_.get_members()
        >>> for member in members:
        ...     print(member)
        <User id="...">
        <User id="...">
        ...
        ...
        >>> more_members = members.next()  # Retrieve more members
        """
        ...

    async def get_subscribers(
        self, count: int = ..., cursor: str | None = ...
    ) -> Result[User]:
        """Retrieves subscribers of the list.

        Parameters
        ----------
        count : :class:`int`, default=20
            Number of subscribers to retrieve.

        Returns
        -------
        Result[:class:`User`]
            Subscribers of the list

        Examples
        --------
        >>> subscribers = list_.get_subscribers()
        >>> for subscriber in subscribers:
        ...     print(subscriber)
        <User id="...">
        <User id="...">
        ...
        ...
        >>> more_subscribers = subscribers.next()  # Retrieve more subscribers
        """
        ...

    async def update(self) -> None: ...
    def __eq__(self, __value: object) -> bool: ...
    def __ne__(self, __value: object) -> bool: ...
    def __repr__(self) -> str: ...
