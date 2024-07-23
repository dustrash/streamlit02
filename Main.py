import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth, db
import datetime

# Firebase 초기화
import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth

if not firebase_admin._apps:
    # Firebase 서비스 계정 정보로 초기화
    cred = credentials.Certificate({
        "type": st.secrets["firebase"]["type"],
        "project_id": st.secrets["firebase"]["project_id"],
        "private_key_id": st.secrets["firebase"]["private_key_id"],
        "private_key": st.secrets["firebase"]["private_key"].replace('\\n', '\n'),
        "client_email": st.secrets["firebase"]["client_email"],
        "client_id": st.secrets["firebase"]["client_id"],
        "auth_uri": st.secrets["firebase"]["auth_uri"],
        "token_uri": st.secrets["firebase"]["token_uri"],
        "auth_provider_x509_cert_url": st.secrets["firebase"]["auth_provider_x509_cert_url"],
        "client_x509_cert_url": st.secrets["firebase"]["client_x509_cert_url"]
    })
    firebase_admin.initialize_app(cred)


# 데이터베이스 참조
ref = db.reference("/users")

# 사용자 인증 및 커스텀 토큰 생성

# 폼 입력
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
st.title("Hello World")
st.header("Hello World2")
st.subheader("Hello World3")
st.write(
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. "
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor "
    "in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, "
    "sunt in culpa qui officia deserunt mollit anim id est laborum."
)

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
