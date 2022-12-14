import datetime
import uuid
from typing import Optional
from pydantic import BaseModel



class BaseStudent(BaseModel):
    # Базовый класс для описания студента

    first_name :str
    last_name :str
    age :int
    birthday: str
    login: str
    password: str
    id_group: str
    description :Optional[str] = None

class StudentIn(BaseStudent):
    # Класс описывает студента, отправленный от пользователя

    secret_token :str

class StudentOut(BaseStudent):
    # Класс описывает студента, который отправляется пользователю (без секретной информации)

    id :uuid.UUID
    created_at :datetime.datetime
    first_name :str
    last_name :str
    age :int
    birthday: str
    login: str
    id_group: str



class StudentStorage(BaseStudent):
    # Класс описывает хранение студента в хранилище

    id :uuid.UUID
    created_at :datetime.datetime
    secret_token :str
