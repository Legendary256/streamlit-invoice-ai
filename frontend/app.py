# Copyright (c) TaKo AI Sp. z o.o.

import streamlit as st

from frontend.domain.entities.invoice_entity import InvoiceEntity
from frontend.presentation.pages.ai_agent import build_agent
from frontend.presentation.pages.business_details import build_business_fields
from frontend.presentation.pages.client_details import build_client_fields
from frontend.presentation.pages.history import build_history
from frontend.presentation.pages.invoice_details import build_invoice_fields
from frontend.presentation.widgets.language_selector import build_language_selector
from frontend.utils.language import (
    Language,
)
from frontend.utils.language import i18n as _


class App:
    def __init__(self) -> None:
        if "invoice" not in st.session_state:
            st.session_state.invoice = InvoiceEntity()

        self.invoice = st.session_state.invoice
        self.language = Language()

        tab_names = [
            str(_("invoice_details") + " :page_facing_up:"),
            str(
                _("shared_details")
                + " "
                + _("client_details")
                + " & "
                + _("business_details")
                + " :bust_in_silhouette:"
            ),
            str(_("agent_ai") + " :brain:"),
            str(_("history") + " :scroll:"),
        ]

        self.InvoiceDetails, self.ClientDetails, self.AgentAI, self.History = st.tabs(
            tab_names
        )

    def run(self) -> None:
        with st.sidebar:
            st.header(_("invoice"))

            st.header(_("settings"))
            build_language_selector(self.language)

            if st.button("debug"):
                print(self.invoice)

        with self.InvoiceDetails:
            build_invoice_fields()

        with self.ClientDetails:
            client_column, business_column = st.columns(2)

            with client_column:
                build_client_fields()

            with business_column:
                build_business_fields()

        with self.History:
            build_history()

        with self.AgentAI:
            build_agent()


if __name__ == "__main__":
    app = App()
    app.run()
