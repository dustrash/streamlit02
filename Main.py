import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

import datetime


if not firebase_admin._apps:
    # # Firebase 서비스 계정 정보 읽기
    # private_key = st.secrets["firebase"]["private_key"]
    # client_email = st.secrets["firebase"]["client_email"]
    # project_id = st.secrets["firebase"]["project_id"]
    # database_url = st.secrets["firebase"]["database_url"]
    
    # 서비스 계정 JSON 생성
    # service_account_info = {
    #     "type": "service_account",
    #     "project_id": project_id,
    #     "private_key_id": "1e6da85c32825373145e1c142eece635aba8ef0b",  # 실제 값으로 대체 필요
    #     "private_key": private_key,
    #     "client_email": client_email,
    #     "client_id": "115412658206097193951",  # 실제 값으로 대체 필요
    #     "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    #     "token_uri": "https://oauth2.googleapis.com/token",
    #     "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    #     "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/" + client_email
    # }
    # additional_claims = {
    #     "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # 유효 시간 설정
    # }

    # user = auth.get_user_by_email("user@example.com")
    # custom_token = auth.create_custom_token(user.uid, additional_claims)
    
    # Firebase 초기화
    cred = credentials.Certificate(st.secrets["firebase"])
    firebase_admin.initialize_app(cred)

ref = db.reference("/users")

with st.form("my_form"):
    name = st.text_input("Name")
    user_id = st.text_input("User ID")
    password = st.text_input("Password", type="password")

    submitted = st.form_submit_button("Submit")
    if submitted:
        try:
            ref.push({f"id: {user_id}": f"password: {password}, name: {name}"})
            st.success("Data submitted successfully!")
        except Exception as e:
            st.error(f"Error: {e}")
            st.error("An error occurred while submitting data. Please try again.")


# 상태 변수 초기화
if 'result' not in st.session_state:
    st.session_state['result'] = 0
if 'text' not in st.session_state:
    st.session_state['text'] = []
if 'next' not in st.session_state:
    st.session_state['next'] = 0

# Streamlit UI
st.title("hello world")
st.header("hello world2")
st.subheader("hello world3")
st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

code = '''import streamlit as st
st.write("hello world")'''
st.code(code, language='python')

st.divider()

temp = st.text_input("댓글", "")
if st.button("작성"):
    if temp:
        st.session_state['text'].append(temp)
    for i in st.session_state['text']:
        st.write(i)
