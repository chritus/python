import streamlit as st
import requests
from streamlit_lottie import st_lottie
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# ---- load assets -----
lottie_coding = "https://lottie.host/a09cc486-9705-4de5-9080-4934b3f95bf2/LztZuoQRoR.json"

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code !=300:
        return None
    return r.json()


# ----header section ------
with st.container():
    st.subheader("Hi ,I am Prince 👍")
    st.title("Just my portfolio")
    st.write("I am determined to archive my current goals as software engineer.")
    st.write("[Learn More](http://youtube.com)")
    st.write("I school at gt")
# ------What I do --------
with st.container():
    st.write("-----")
    left_column, right_column =st.columns(2)
    with left_column :
        st.header("What I do 💻")
        st.write("##")
        st.write("""Coding represents the language of innovation.
                 Through programming, I can actively contribute to the creation of cutting-edge solutions that address real-world challenges. 
                 The prospect of being at the forefront of technological advancements is both thrilling and motivating.""")
        st.write("[Call me on whatsapp](https://call.whatsapp.com/video/AtraG8Y89XmulJ9o6aIUxN)")
        st.write("[To asses my github repository](http//youtube.com)") 
        with right_column:
            st.lottie(lottie_coding, height = 300 , key ="coding")
