import datetime
import uuid
from fa_learn_group_app.models.group import GroupIn, GroupOut, GroupStorage


def convert_product_storage_to_out(product: GroupStorage) -> GroupOut:
    # Производит конвертацию ProductSrorage --> ProductOut

    tmp_dict: dict = product.dict()
    tmp_dict.pop("secret_token", None)
    return GroupOut(**tmp_dict)


def convert_product_in_to_storage(product: GroupIn) -> GroupStorage:
    # Производит конвертацию ProductIn --> PrductStorage

    tmp_dict: dict = product.dict()
    product_storage = GroupStorage(id=uuid.uuid4(),
                                     created_at=datetime.datetime.now(),
                                     **tmp_dict)
    return product_storage


def update_product_in_to_storage(id_old :uuid.UUID, product_new: GroupIn) -> GroupStorage:
    # Производит обновление данных

    tmp_dict: dict = product_new.dict()
    product_storage = GroupStorage(id=id_old,
                                     created_at=datetime.datetime.now(),
                                     **tmp_dict)

    return product_storage 