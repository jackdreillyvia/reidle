import asyncio
import streamlit as st
from datetime import datetime
from streamlit.components.v1 import iframe
import hashlib

st.set_page_config(layout="wide")


@st.experimental_singleton
def get_starter_word() -> str:
    with open("words.csv") as fn:
        words = fn.readlines()
    return words[
        int(hashlib.sha1(datetime.utcnow().date().isoformat().encode()).hexdigest(), 16)
        % len(words)
    ].strip()


async def watch():
    x = 0
    while True:
        timer.markdown(str(x))
        r = await asyncio.sleep(1)
        x += 1


with st.sidebar:
    a, b, c = st.columns(3)
    with a:
        start = st.button("Go!")
    with b:
        word = get_starter_word()
        word
    with c:
        timer = st.empty()

if start:
    iframe("https://www.nytimes.com/games/wordle/index.html", height=1000)
    asyncio.run(watch())
