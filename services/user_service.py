from dataclasses import dataclass
import email
from typing import List
from unicodedata import name


@dataclass
class UserScheme:
    id: int
    name: str
    email: str
    password: str

users: List[UserScheme] = [
    {"id": 1, "name": "Kirill", "email": "kirill@gmail.com", "password": "111111"}
]

def find_user(email: str, password: str) -> UserScheme:
    return next(user for user in users 
      if user["email"] == email and user["password"] == password)

def add_user(email: str, password: str, name: str) -> UserScheme:
    id_next_user = len(users) + 1

    users.append({
      "id":id_next_user,
      "email":email,
      "password":password,
      "name":name
    })

    return {
      "id":id_next_user,
      "email":email,
      "password":password,
      "name":name
    }