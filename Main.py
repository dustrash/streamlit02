import streamlit as st
import firebase_admin
from firebase_admin import credentials, auth, db
import datetime

# Firebase 초기화
if not firebase_admin._apps:
    # Firebase 서비스 계정 정보로부터 초기화
    cred = credentials.Certificate(st.secrets["firebase"])
    firebase_admin.initialize_app(cred)

# 데이터베이스 참조
ref = db.reference("/users")

# 사용자 인증 및 커스텀 토큰 생성
def create_custom_token(email):
    additional_claims = {
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)  # 유효 시간 설정
    }
    try:
        user = auth.get_user_by_email(email)
        custom_token = auth.create_custom_token(user.uid, additional_claims)
        return custom_token
    except Exception as e:
        st.error(f"Error creating custom token: {e}")
        return None

# 사용자 이메일을 통해 커스텀 토큰 생성 (예시: 'user@example.com'을 실제 사용자 이메일로 대체)
custom_token = create_custom_token("firebase-adminsdk-arsle@teststreamlit-3fc73.iam.gserviceaccount.com")

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
