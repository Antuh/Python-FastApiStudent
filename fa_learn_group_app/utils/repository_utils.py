import datetime
import uuid
from fa_learn_app.models.student import StudentIn, StudentOut, StudentStorage


def convert_product_storage_to_out(product: StudentStorage) -> StudentOut:
    # Производит конвертацию ProductSrorage --> ProductOut

    tmp_dict: dict = product.dict()
    tmp_dict.pop("secret_token", None)
    return StudentOut(**tmp_dict)


def convert_product_in_to_storage(product: StudentIn) -> StudentStorage:
    # Производит конвертацию ProductIn --> PrductStorage

    tmp_dict: dict = product.dict()
    product_storage = StudentStorage(id=uuid.uuid4(),
                                     created_at=datetime.datetime.now(),
                                     **tmp_dict)
    return product_storage


def update_product_in_to_storage(id_old :uuid.UUID, product_new: StudentIn) -> StudentStorage:
    # Производит обновление данных

    tmp_dict: dict = product_new.dict()
    product_storage = StudentStorage(id=id_old,
                                     created_at=datetime.datetime.now(),
                                     **tmp_dict)

    return 