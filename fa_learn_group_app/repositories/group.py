from typing import List, Dict, Optional
import uuid
from fa_learn_group_app.models.group import GroupIn, GroupOut, GroupStorage
from fa_learn_group_app.utils.repository_utils import convert_product_storage_to_out, convert_product_in_to_storage, update_product_in_to_storage

class BaseProductRepository:
    # Базовый класс для реализации функционала работы со студентами

    def get_by_id(self, id :uuid.UUID | int) -> GroupOut:
        raise NotImplementedError

    def get_all(self, limit :int, skip :int) -> List[GroupOut]:
        raise NotImplementedError

    def create(self, product :GroupIn) ->GroupOut:
        raise NotImplementedError

    def updateproduct(self, id : uuid.UUID, product :GroupIn) -> GroupOut:
        raise NotImplementedError

    def delete(self, id :uuid.UUID) -> GroupOut:
        raise NotImplementedError

class ProductTmpRepository(BaseProductRepository):
    # Реализация студента с временным хранилищем в объекте Dict

    def __init__(self):

        # Временное хранилище
        self._dict_products :Dict[uuid.UUID, GroupStorage] = {}

    def get_by_id(self, id :uuid.UUID) -> Optional[GroupOut]:
        # Получение студента по id

        product :GroupStorage = self._dict_products.get(id)
        if product is None:
            return None
        product_out :GroupOut = convert_product_storage_to_out(product)
        return product_out

    def get_all(self, limit :int, skip :int) -> List[GroupOut]:
        # Получение всех студентов

        product_out_list :List[GroupOut] = []
        for _, product in self._dict_products.items():
            product_out_list.append(convert_product_storage_to_out(product))
            return  product_out_list[skip:skip+limit]

    def create(self, product: GroupIn) -> GroupOut:
        # Создание студента

        product_storage: GroupStorage = convert_product_in_to_storage(product)
        self._dict_products.update({product_storage.id: product_storage})
        product_out: GroupOut = convert_product_storage_to_out(product_storage)
        return product_out

    def updateproduct(self, id: uuid.UUID, product_new: GroupIn) -> Optional[GroupOut]:
        # Получение студента по идентификатору для обновления/изменения данных

        product_old: GroupStorage = self._dict_products.get(id)
        if product_old is None:
            return "Данный студент не найден"

        product_update: GroupOut = update_product_in_to_storage(id, product_new)
        self._dict_products.update({product_update.id: product_update})
        product_out: GroupOut = convert_product_storage_to_out(product_update)
        return product_out

    def delete(self, id: uuid.UUID) -> str:
        # Удаление студента по идентификатору

        product: GroupStorage = self._dict_products.get(id)
        if product is None:
            return "Данный студент не найден"
        self._dict_products.pop(id, None)
        return "Студента успешно удален"



