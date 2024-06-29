from typing import List, Tuple

from sqlalchemy import and_
from sqlalchemy.orm import Session

from backend.controllers.base_controller import (
    BaseController,
    InvoiceNotFoundException,
    session_scope,
)
from backend.models import BusinessTable, ClientTable, InvoiceTable, ProductTable


class InvoiceController(BaseController):
    @session_scope
    def list(
        self, session: Session
    ) -> Tuple[
        List[InvoiceTable],
        List[BusinessTable],
        List[ClientTable],
        List[List[ProductTable]],
    ]:
        all_invoices = session.query(InvoiceTable).all()

        invoices = []
        businesses = []
        clients = []
        products = []

        for invoice in all_invoices:
            invoice, business, client, product = self.get(
                invoice.invoiceNo, invoice.language
            )

            invoices.append(invoice)
            businesses.append(business)
            clients.append(client)
            products.append(product)

        return invoices, businesses, clients, products

    @session_scope
    def get(
        self, session: Session, invoice_no: str, language: str
    ) -> Tuple[InvoiceTable, BusinessTable, ClientTable, List[ProductTable],]:
        invoice = (
            session.query(InvoiceTable)
            .filter(
                and_(
                    InvoiceTable.invoiceNo == invoice_no,
                    InvoiceTable.language == language,
                )
            )
            .first()
        )

        if invoice is None:
            raise InvoiceNotFoundException(
                f"No invoice found with invoice number {invoice_no} and language {language}"
            )

        business = (
            session.query(BusinessTable)
            .filter_by(businessID=invoice.business_id)
            .first()
        )
        client = (
            session.query(ClientTable).filter_by(clientID=invoice.client_id).first()
        )
        products = (
            session.query(ProductTable).filter_by(invoice_id=invoice.invoiceID).all()
        )

        if business is None:
            raise InvoiceNotFoundException(
                f"No business found with id {invoice.business_id}"
            )

        if client is None:
            raise InvoiceNotFoundException(
                f"No client found with id {invoice.client_id}"
            )

        if not products:
            raise InvoiceNotFoundException(
                f"No products found for invoice with id {invoice.invoiceNo}"
            )

        return invoice, business, client, products

    @session_scope
    def add(
        self, session: Session, invoice: InvoiceTable, products: List[ProductTable]
    ) -> None:
        session.add(invoice)
        for product in products:
            session.add(product)

    @session_scope
    def put(
        self, session: Session, invoice: InvoiceTable, products: List[ProductTable]
    ) -> None:
        result = (
            session.query(InvoiceTable)
            .filter(
                and_(
                    InvoiceTable.invoiceID == invoice.invoiceNo,
                    InvoiceTable.language == invoice.language,
                )
            )
            .first()
        )

        if result is None:
            raise InvoiceNotFoundException(
                f"No invoice found with id {invoice.invoiceNo}"
            )

        session.query(ProductTable).filter_by(invoice_id=result.invoiceID).delete()

        for product in products:
            session.delete(product)

        for key, value in invoice.__dict__.items():
            if key != "_sa_instance_state":
                setattr(result, key, value)

    @session_scope
    def delete(self, session: Session, invoice_no: str, language: str) -> None:
        invoice_table = (
            session.query(InvoiceTable)
            .filter_by(invoiceNo=invoice_no, language=language)
            .first()
        )
        if invoice_table is None:
            raise InvoiceNotFoundException(f"No invoice found with id {invoice_no}")

        session.query(ProductTable).filter_by(
            invoice_id=invoice_table.invoiceID
        ).delete()

        session.delete(invoice_table)
