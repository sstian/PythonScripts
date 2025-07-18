from fastapi import APIRouter

router = APIRouter(
    # prefix="",  # 该路由下所有路径的前缀
    tags=["users"],   # OpenAPI/Swagger 文档中的标签
)

# @router.get("/users/", tags=["users"])
@router.get("/")
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]


@router.get("/me")
async def read_user_me():
    return {"username": "fakecurrentuser"}


@router.get("/{username}")
async def read_user(username: str):
    return {"username": username}