from typing import Optional

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from ..database import Base


class Post(Base):
    """
    Represents a post in a Subreddit.
    """

    __tablename__ = "posts"

    id: Optional[int] = Column(default=None, primary_key=True)

    title: str = Column(String(150))

    text: Optional[str] = Column(String(1024), default=None)

    link: Optional[str] = Column(String(255), default=None, unique=True)

    thumbnail: Optional[str] = Column(String(255), default=None)

    user_id: int = Column(Integer, ForeignKey("users.id"))

    subreddit_id: int = Column(Integer, ForeignKey("subreddits.id"))

    votes: int = Column(Integer, default=1)

    comments = relationship("Comment", back_populates="post", lazy="dynamic")

    def __repr__(self) -> str:
        return f"<Post {self.title}>"
