import streamlit as st


answer1 = st.radio("다음 중 논리 연산에서 옳은 것은?",
        ["1 + 1 = 2",
         "1 + 1 = 10",
         "1 + 1 = 3",
         "1 + 1 = 1",
         "1 + 1 = 0"])
if st.button("다음"):
    st.session_state['next'] = 1

if st.session_state['next'] == 1:
    answer2 = st.text_input("파이썬의 출력함수는? (괄호를 빼고 적으시오)")

    if st.button("Submit"):
        if answer1 == "1 + 1 = 1":
            st.session_state['result'] += 50
        if answer2 == "print":
            st.session_state['result'] += 50
        st.switch_page("pages/2_Result.py")