# Copyright (c) TaKo AI Sp. z o.o.

from src.domain import (
    BusinessEntity,
    CreateBusinessUseCase,
    DeleteBusinessUseCase,
    EditBusinessUseCase,
    GetAllBusinessesNamesUseCase,
    GetBusinessDetailsUseCase,
    GetAllClientsNamesUseCase,
)


class Handler:
    """Facade class for handling business use cases"""

    def __init__(
        self,
        edit_business_use_case: EditBusinessUseCase,
        get_all_businesses_names_use_case: GetAllBusinessesNamesUseCase,
        get_business_details_use_case: GetBusinessDetailsUseCase,
        create_business_use_case: CreateBusinessUseCase,
        delete_business_use_case: DeleteBusinessUseCase,
        get_all_clients_names_use_case: GetAllClientsNamesUseCase,
    ):
        self.edit_business_use_case = edit_business_use_case
        self.get_all_businesses_names_use_case = get_all_businesses_names_use_case
        self.get_business_details_use_case = get_business_details_use_case
        self.create_business_use_case = create_business_use_case
        self.delete_business_use_case = delete_business_use_case
        self.get_all_clients_names_use_case = get_all_clients_names_use_case

    def edit_business(self, business: BusinessEntity) -> None:
        self.edit_business_use_case.execute(business)

    def get_all_businesses_names(self) -> list[str | None]:
        return self.get_all_businesses_names_use_case.execute()

    def get_business_details(self, business_name: str) -> BusinessEntity | None:
        return self.get_business_details_use_case.execute(business_name)

    def create_business(self, business: BusinessEntity) -> None:
        self.create_business_use_case.execute(business)

    def delete_business(self, business_name: str) -> None:
        self.delete_business_use_case.execute(business_name)

    def get_all_clients_names(self) -> list[str | None]:
        return self.get_all_clients_names_use_case.execute()
