"""
This type stub file was generated by pyright.
"""

import httpx
from dataclasses import dataclass
from datetime import datetime
from typing import Generator, Optional, Union

@dataclass
class JSONTrait:
    def dict(self): # -> dict[str, Any]:
        ...
    
    def json(self): # -> str:
        ...
    


@dataclass
class Coordinates(JSONTrait):
    longitude: float
    latitude: float
    @staticmethod
    def parse(tw_obj: dict): # -> Coordinates | None:
        ...
    


@dataclass
class Place(JSONTrait):
    id: str
    fullName: str
    name: str
    type: str
    country: str
    countryCode: str
    @staticmethod
    def parse(obj: dict): # -> Place:
        ...
    


@dataclass
class TextLink(JSONTrait):
    url: str
    text: str | None
    tcourl: str | None
    @staticmethod
    def parse(obj: dict): # -> TextLink | None:
        ...
    


@dataclass
class UserRef(JSONTrait):
    id: int
    id_str: str
    username: str
    displayname: str
    _type: str = ...
    @staticmethod
    def parse(obj: dict): # -> UserRef:
        ...
    


@dataclass
class User(JSONTrait):
    id: int
    id_str: str
    url: str
    username: str
    displayname: str
    rawDescription: str
    created: datetime
    followersCount: int
    friendsCount: int
    statusesCount: int
    favouritesCount: int
    listedCount: int
    mediaCount: int
    location: str
    profileImageUrl: str
    profileBannerUrl: str | None = ...
    protected: bool | None = ...
    verified: bool | None = ...
    blue: bool | None = ...
    blueType: str | None = ...
    descriptionLinks: list[TextLink] = ...
    pinnedIds: list[int] = ...
    _type: str = ...
    @staticmethod
    def parse(obj: dict, res=...): # -> User:
        ...
    


@dataclass
class Tweet(JSONTrait):
    id: int
    id_str: str
    url: str
    date: datetime
    user: User
    lang: str
    rawContent: str
    replyCount: int
    retweetCount: int
    likeCount: int
    quoteCount: int
    bookmarkedCount: int
    conversationId: int
    conversationIdStr: str
    hashtags: list[str]
    cashtags: list[str]
    mentionedUsers: list[UserRef]
    links: list[TextLink]
    media: Media
    viewCount: int | None = ...
    retweetedTweet: Optional[Tweet] = ...
    quotedTweet: Optional[Tweet] = ...
    place: Optional[Place] = ...
    coordinates: Optional[Coordinates] = ...
    inReplyToTweetId: int | None = ...
    inReplyToTweetIdStr: str | None = ...
    inReplyToUser: UserRef | None = ...
    source: str | None = ...
    sourceUrl: str | None = ...
    sourceLabel: str | None = ...
    card: Union[None, SummaryCard, PollCard, BroadcastCard, AudiospaceCard] = ...
    possibly_sensitive: bool | None = ...
    _type: str = ...
    @staticmethod
    def parse(obj: dict, res: dict):
        ...
    


@dataclass
class MediaPhoto(JSONTrait):
    url: str
    @staticmethod
    def parse(obj: dict): # -> MediaPhoto:
        ...
    


@dataclass
class MediaVideo(JSONTrait):
    thumbnailUrl: str
    variants: list[MediaVideoVariant]
    duration: int
    views: int | None = ...
    @staticmethod
    def parse(obj: dict): # -> MediaVideo:
        ...
    


@dataclass
class MediaAnimated(JSONTrait):
    thumbnailUrl: str
    videoUrl: str
    @staticmethod
    def parse(obj: dict): # -> MediaAnimated | None:
        ...
    


@dataclass
class MediaVideoVariant(JSONTrait):
    contentType: str
    bitrate: int
    url: str
    @staticmethod
    def parse(obj: dict): # -> MediaVideoVariant:
        ...
    


@dataclass
class Media(JSONTrait):
    photos: list[MediaPhoto] = ...
    videos: list[MediaVideo] = ...
    animated: list[MediaAnimated] = ...
    @staticmethod
    def parse(obj: dict): # -> Media:
        ...
    


@dataclass
class Card(JSONTrait):
    ...


@dataclass
class SummaryCard(Card):
    title: str
    description: str
    vanityUrl: str
    url: str
    photo: MediaPhoto | None = ...
    video: MediaVideo | None = ...
    _type: str = ...


@dataclass
class PollOption(JSONTrait):
    label: str
    votesCount: int
    ...


@dataclass
class PollCard(Card):
    options: list[PollOption]
    finished: bool
    _type: str = ...


@dataclass
class BroadcastCard(Card):
    title: str
    url: str
    photo: MediaPhoto | None = ...
    _type: str = ...


@dataclass
class AudiospaceCard(Card):
    url: str
    _type: str = ...


def parse_tweets(rep: httpx.Response, limit: int = ...) -> Generator[Tweet, None, None]:
    ...

def parse_users(rep: httpx.Response, limit: int = ...) -> Generator[User, None, None]:
    ...

def parse_tweet(rep: httpx.Response, twid: int) -> Tweet | None:
    ...

def parse_user(rep: httpx.Response) -> User | None:
    ...

