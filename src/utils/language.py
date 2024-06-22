# Copyright (c) TaKo AI Sp. z o.o.

import gettext
import streamlit as st


class Language:
    language_dict = {'English': 'en', 'Polish': 'pl', 'Dutch': 'nl'}

    def __init__(self):
        self.translations = {
            'en': gettext.translation('base', 'locales', languages=['en']),
            'pl': gettext.translation('base', 'locales', languages=['pl']),
            'nl': gettext.translation('base', 'locales', languages=['nl']),
        }

        if 'language' not in st.session_state:
            st.session_state.language = 'pl'

        self.change_language(st.session_state.language)

    def change_language(self, language):
        st.session_state.language = language
        self.translations[st.session_state.language].install(names=["_"])
