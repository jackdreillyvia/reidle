import asyncio
import hashlib
import webbrowser
from datetime import datetime

import streamlit as st


@st.experimental_singleton
def get_starter_word() -> str:
    with open("words.csv") as fn:
        words = fn.readlines()
    return words[
        int(hashlib.sha1(datetime.utcnow().date().isoformat().encode()).hexdigest(), 16)
        % len(words)
    ].strip()


st.header("Reidle")
st.text(f"Starter word: {get_starter_word()}")
if st.button("Open Wordle"):
    webbrowser.open_new_tab("https://www.nytimes.com/games/wordle/index.html")
if st.button("Reset Timer"):
    timer = st.empty()

    async def watch():
        x = 0
        while True:
            timer.markdown(f"Time: {x}")
            r = await asyncio.sleep(1)
            x += 1

    asyncio.run(watch())
