from fa_learn_group_app.repositories.group import ProductTmpRepository

TMP_REPOSITORY = ProductTmpRepository()

def get_product_repo() -> ProductTmpRepository:
    # Получение Product репозитория

    return TMP_REPOSITORY