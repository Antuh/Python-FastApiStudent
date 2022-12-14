import datetime
import uuid
from typing import Optional
from pydantic import BaseModel



class BaseGroup(BaseModel):
    # Базовый класс для описания студента

    name :str


class GroupIn(BaseGroup):
    # Класс описывает студента, отправленный от пользователя

    secret_token :str

class GroupOut(BaseGroup):
    # Класс описывает студента, который отправляется пользователю (без секретной информации)

    name :str


class GroupStorage(BaseGroup):
    # Класс описывает хранение студента в хранилище

    id :uuid.UUID
    created_at :datetime.datetime
    secret_token :str
