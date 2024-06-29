# Copyright (c) TaKo AI Sp. z o.o.

import json
from typing import Any

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship

from backend.models import Base


class InvoiceTable(Base):
    __tablename__ = "invoice"

    invoiceId = Column(
        "invoiceId", String, primary_key=True, default=Base.generate_uuid
    )
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

    language = Column("language", String)

    def __init__(self, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.invoiceNo = kwargs["invoiceNo"]
        self.currency = kwargs["currency"]
        self.vatPercent = kwargs["vatPercent"]
        self.issuedAt = kwargs["issuedAt"]
        self.dueTo = kwargs["dueTo"]
        self.note = kwargs["note"]
        self.business_id = kwargs["business_id"]
        self.client_id = kwargs["client_id"]
        self.language = kwargs["language"]

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
                "language": self.language,
            }
        )