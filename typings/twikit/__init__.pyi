"""
This type stub file was generated by pyright.
"""

import asyncio
import os

from ._captcha import Capsolver
from .bookmark import BookmarkFolder
from .client.client import Client
from .community import Community, CommunityCreator, CommunityMember, CommunityRule
from .errors import *
from .geo import Place
from .group import Group, GroupMessage
from .list import List
from .message import Message
from .notification import Notification
from .trend import Trend
from .tweet import CommunityNote, Poll, ScheduledTweet, Tweet
from .user import User
from .utils import build_query

"""
==========================
Twikit Twitter API Wrapper
==========================

https://github.com/d60/twikit
A Python library for interacting with the Twitter API.
"""
__version__ = ...
if os.name == "nt": ...
