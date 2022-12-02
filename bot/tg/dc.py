from pydantic import BaseModel, Field
from pydantic.schema import List


class MessageFrom(BaseModel):
    id: int
    first_name: str
    last_name: str | None = None
    username: str | None = None


class Chat(BaseModel):
    id: int
    type: str
    first_name: str | None = None
    last_name: str | None = None
    username: str | None = None
    title: str | None = None


class Message(BaseModel):
    message_id: int
    from_: MessageFrom = Field(..., alias='from')
    chat: Chat
    text: str | None = None

    class Config:
        allow_population_by_field_name = True


class UpdateObj(BaseModel):
    update_id: int
    message: Message


class GetUpdateResponse(BaseModel):
    ok: bool
    result: List[UpdateObj] = []


class SendMessageResponse(BaseModel):
    ok: bool
    result: Message
