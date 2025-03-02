"""
This type stub file was generated by pyright.
"""

from typing import TYPE_CHECKING

import webvtt

from .client.client import Client

if TYPE_CHECKING: ...

class Media:
    """
    A base class representing media object.

    Attributes
    ----------
    id : :class:`str`
        The media ID.
    display_url : :class:`str`
        The display URL.
    expanded_url : :class:`str`
        The expanded display URL.
    media_url : :class:`str`
        The media URL.
    source_status_id : :class:`str`
        The source tweet ID.
    source_user_id : :class:`str`
        The ID of the user who posted the source tweet.
    type : :class:`str`
        The media type.
    url : :class:`str`
        The URL of the media.
    sizes : :class:`dict`
        The sizes of the media.
    original_info : :class:`str`
    width : :class:`int`
        The width of the media.
    height : :class:`int`
        The height of the media.
    focus_rects : :class:`list`
    """
    def __init__(self, client: Client, data: dict) -> None: ...
    @property
    def id(self) -> str: ...
    @property
    def display_url(self) -> str: ...
    @property
    def expanded_url(self) -> str: ...
    @property
    def media_url(self) -> str: ...
    @property
    def source_status_id(self) -> str: ...
    @property
    def source_user_id(self) -> str: ...
    @property
    def type(self) -> str: ...
    @property
    def url(self) -> str: ...
    @property
    def sizes(self) -> dict: ...
    @property
    def original_info(self) -> str: ...
    @property
    def width(self) -> int: ...
    @property
    def height(self) -> int: ...
    @property
    def focus_rects(self) -> list: ...
    async def get(self) -> bytes: ...
    async def download(self, output_path: str) -> None: ...
    def __repr__(self) -> str: ...

class Photo(Media):
    """
    A class representing a photo media object.

    Attributes
    ----------
    features : :class:`dict`
        The features of the photo.
    """
    @property
    def features(self) -> dict: ...

class Stream:
    """
    The Stream class represents a media stream

    Attributes
    ----------
    url : :class:`str`
        The url of the stream.
    bitrate : :class:`int`
        The bitrate of the stream.
    content_type : :class:`str`
        The mimetype of the stream content.
    """
    def __init__(self, client: Client, data: dict) -> None: ...
    @property
    def url(self) -> str: ...
    @property
    def bitrate(self) -> int: ...
    @property
    def content_type(self) -> str: ...
    async def get(self) -> bytes:
        """
        Retrieves the stream content.

        Returns
        -------
        :class:`bytes`
            The raw content of the stream.
        """
        ...

    async def download(self, output_path: str) -> None:
        """
        Downloads the stream content and saves it to the specified file.

        Parameters
        ----------
        output_path : :class:`str`
            The path where the downloaded file will be saved.
        """
        ...

    def __repr__(self) -> str: ...

class AnimatedGif(Media):
    """
    A class representing an animated GIF media object.

    Attributes
    ----------
    video_info : :class:`dict`
        The video information of the GIF.
    aspect_ratio : :class:`tuple[int, int]`
        The aspect ratio of the GIF.
    streams : list[:class:`Stream`]
        The list of video streams for the GIF.
    """
    @property
    def video_info(self) -> dict: ...
    @property
    def aspect_ratio(self) -> tuple[int, int]: ...
    @property
    def streams(self) -> list: ...

class Video(Media):
    """
    A class representing a video media object.


    .. code-block:: python

        # Video download example
        tweet = await client.get_tweet_by_id('00000000000')
        video = tweet.media[0]
        streams = video.streams
        await streams[0].download('output.mp4')

    Attributes
    ----------
    video_info : :class:`dict`
        The video information.
    aspect_ratio : :class:`tuple[int, int]`
        The aspect ratio of the video.
    duration_millis : :class:`int`
        The duration of the video in milliseconds.
    streams : list[:class:`Stream`]
        The list of video streams for the video.
    """
    def __init__(self, client: Client, data: dict) -> None: ...
    @property
    def video_info(self) -> dict: ...
    @property
    def aspect_ratio(self) -> tuple[int, int]: ...
    @property
    def duration_millis(self) -> int: ...
    @property
    def streams(self) -> list[Stream]: ...
    async def get_subtitles(self) -> webvtt.WebVTT | None:
        """
        Retrieves the subtitles for the video.

        Returns
        -------
        :class:`webvtt.WebVTT` | None
            Returns the subtitles for the video. If the video does not have subtitles, returns None.
            Refer https://github.com/glut23/webvtt-py for more information.

        Examples
        --------
        .. code-block:: python

            tweet = await client.get_tweet_by_id('00000000000')
            video = tweet.media[0]
            subtitles = await video.get_subtitles()
            for l in subtitles:
                print(l.start)
                print(l.end)
                print(l.text)
        """
        ...

MEDIA_TYPE = Video | Photo | AnimatedGif
MEDIA_TYPE_MAPPING = ...
