from __future__ import annotations

from typing import List, Optional

from strawberry import type, field
from strawberry.types import Info
from sqlalchemy import select

from reddit.base.types import NodeType
from reddit.posts.models import Post
from reddit.comments.types import CommentType
from reddit.database import get_session


@type(name="Post")
class PostType(NodeType):
    title: str = field(
        description="""
        The title of the post.
        """
    )

    text: Optional[str] = field(
        description="""
        The text for the post.
        """
    )

    link: Optional[str] = field(
        description="""
        The link of the post.
        """
    )

    thumbnail: Optional[str] = field(
        description="""
        The thumbnail URL of the post.
        """
    )

    user_id: int = field(
        description="""
        The owner ID of the post.
        """
    )

    subreddit_id: int = field(
        description="""
        The subreddit ID of the post.
        """
    )

    votes: int = field(
        description="""
        The votes the post has.
        """
    )

    comments: List[CommentType] = field(
        description="""
        The comments for the post.
        """
    )

    @classmethod
    async def get_node(cls, info: Info, post_id: str) -> Optional[Post]:
        """
        Gets a post with the given ID.
        """
        query = select(Post).filter_by(id=post_id).first()
        async with get_session() as session:
            user = await session.execute(query)
        return user

    @classmethod
    def from_instance(cls, instance: Post) -> PostType:
        return PostType(
            id=instance.id,
            title=instance.title,
            text=instance.text,
            link=instance.link,
            thumbnail=instance.thumbnail,
            user_id=instance.user_id,
            subreddit_id=instance.subreddit_id,
            votes=instance.votes,
            comments=instance.comments,
        )
