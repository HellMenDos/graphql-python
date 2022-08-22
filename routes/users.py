from schemes import query,mutation
from services.user_service import users,find_user,add_user


def usersSchemes():
  @query.field("users")
  def users(*_):
    global users
    return users

  @mutation.field("login")
  def login(_, info, email, password):
    return find_user(email, password)

  @mutation.field("reg")
  def reg(_, info, email, name, password):
    return add_user(email, password, name)