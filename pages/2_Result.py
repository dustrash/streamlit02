import streamlit as st

st.title(f"{st.session_state['result']}/100")






st.session_state['result'] = 0
st.session_state['next'] = 0