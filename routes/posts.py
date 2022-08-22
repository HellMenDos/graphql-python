from this import d
from schemes import query,mutation
from services.posts_service import posts,get,get_by_user,create


def postsSchemes():
  @query.field("post")
  def post(*_, id):
    return get(id)

  @query.field("post_by_user")
  def post_by_user(*_, user_id):
    return get_by_user(user_id)

  @mutation.field('create_post')
  def create_post(*_, user_id,title,description):
    return create(user_id, title, description)