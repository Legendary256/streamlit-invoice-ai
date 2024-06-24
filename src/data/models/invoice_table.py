import json
import uuid
from typing import Any

from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
)
from sqlalchemy.orm import (
    DeclarativeBase,
    relationship
)


def generate_uuid() -> str:
    return str(uuid.uuid4())


class Base(DeclarativeBase):
    pass


class InvoiceTable(Base):
    __tablename__ = "invoice"

    invoiceId = Column("invoiceId", String, primary_key=True, default=generate_uuid)
    invoiceNo = Column("invoiceNo", String)
    currency = Column("currency", String)
    vatPercent = Column("vatPercent", Integer)
    issuedAt = Column("issuedAt", String)
    dueTo = Column("dueTo", String)
    note = Column("note", String)
    business_id = Column(Integer, ForeignKey("business.businessID"))
    client_id = Column(Integer, ForeignKey("client.clientID"))

    business = relationship("BusinessTable")
    client = relationship("ClientTable")

    def __init__(cls, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        cls.invoiceNo = kwargs["invoiceNo"]
        cls.currency = kwargs["currency"]
        cls.vatPercent = kwargs["vatPercent"]
        cls.issuedAt = kwargs["issuedAt"]
        cls.dueTo = kwargs["dueTo"]
        cls.note = kwargs["note"]
        cls.business_id = kwargs["business_id"]
        cls.client_id = kwargs["client_id"]

    def __repr__(self) -> str:
        return json.dumps(
            {
                "invoiceNo": self.invoiceNo,
                "currency": self.currency,
                "vatPercent": self.vatPercent,
                "issuedAt": self.issuedAt,
                "dueTo": self.dueTo,
                "note": self.note,
                "business_id": self.business_id,
                "client_id": self.client_id,
            }
        )