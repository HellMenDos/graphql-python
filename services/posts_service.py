from dataclasses import dataclass
import email
from typing import List
from unicodedata import name


@dataclass
class PostScheme:
    id: int
    user_id: int
    title: str
    description: str

posts: List[PostScheme] = [
    {"id": 1, "user_id": 1, "title": "test 2", "description": "description"}
]

def get_by_user(id: int) -> List[PostScheme]:
    return list(post for post in posts if post["user_id"] == id)

def get(id: int) -> PostScheme:
    return next(post for post in posts if post["id"] == id)

def create(user_id: int, title: str, description: str):
    id_next_user = len(posts) + 1

    posts.append({
      "id":id_next_user,
      "user_id":user_id,
      "title":title,
      "description":description
    })

    return {
      "id":id_next_user,
      "user_id":user_id,
      "title":title,
      "description":description
    }