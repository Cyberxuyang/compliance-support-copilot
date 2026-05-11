import requests
import streamlit as st
import os

BACKEND_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:8000")


st.set_page_config(
    page_title="Compliance Support Copilot",
    page_icon="",
)

st.title("Compliance Support Copilot")

message = st.text_area(
    "Ask a support or compliance question",
    placeholder="Can I get a refund after 14 days?",
)

if st.button("Send"):
    if not message.strip():
        st.warning("Please enter a question.")
    else:
        response = requests.post(
            f"{BACKEND_URL}/chat",
            json={"message": message},
            timeout=10,
        )
        response.raise_for_status()

        data = response.json()

        st.subheader("Answer")
        st.write(data["message"])

        st.subheader("Confidence")
        st.write(data["confidence"])

        st.subheader("Sources")
        if data["sources"]:
            for source in data["sources"]:
                st.write(f"- {source}")
        else:
            st.write("No sources yet. This is a mock response.")
