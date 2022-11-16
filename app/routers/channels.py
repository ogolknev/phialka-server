from fastapi import APIRouter
import schemas


channels_router = APIRouter(
    prefix = "/channels",
    tags = ["channels"]
)


@channels_router.get("/channels")
async def get_list(info: schemas.Channel):
    return {'status':'OK'}


@channels_router.post("/channels")
async def create_channel(info: schemas.Channel):
    return {'status':'OK'}


@channels_router.get("/channels/{channel_id}")
async def get_info_channel(info: schemas.Channel):
    return {'channel_id':'channel_id'}


@channels_router.patch("/channels/{channel_id}")
async def edit_info_channel(info: schemas.Channel):
    return {'channel_id':'channel_id'}


@channels_router.delete("/channels/{channel_id}")
async def delete_channel(info: schemas.Channel):
    return {'channel_id':'channel_id'}


@channels_router.patch("/channels/{channel_id}/join")
async def join_channel(info: schemas.Channel):
    return {'channel_id':'channel_id'}


@channels_router.patch("/channels/{channel_id}/leave")
async def leave_channel():
    return {'channel_id':'channel_id'}


@channels_router.get("/channels/{channel_id}/posts")
async def get_posts(posts: schemas.Post):
    return {'channel_id':'channel_id'}


@channels_router.post("/channels/{channel_id}/posts")
async def create_posts(posts: schemas.Post):
    return {'channel_id':'channel_id'}


@channels_router.delete("/channels/{channel_id}/posts")
async def delete_posts(posts: schemas.Post):
    return {'channel_id':'channel_id'}


@channels_router.patch("/channels/{channel_id}/posts/{post_id}")
async def edit_posts(posts: schemas.Post):
    return {'post_id':'post_id'}


@channels_router.get("/channels/{channel_id}/members")
async def get_members(posts: schemas.User):
    return {'channel_id':'channel_id'}


@channels_router.patch("/channels/{channel_id}/members")
async def invite_users(posts: schemas.User):
    return {'channel_id':'channel_id'}


@channels_router.get("/channels/{channel_id}/my_role")
async def get_role(roles: schemas.Channel_Role):
    return {'channel_id':'channel_id'}


@channels_router.get("/channels/{channel_id}/roles")
async def get_list_roles(roles: schemas.Channel_Role):
    return {'channel_id':'channel_id'}


@channels_router.post("/channels/{channel_id}/roles")
async def create_roles(roles: schemas.Channel_Role):
    return {'channel_id':'channel_id'}


@channels_router.patch("/channels/{channel_id}/roles")
async def change_roles(roles: schemas.Channel_Role):
    return {'channel_id':'channel_id'}