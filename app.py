import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
import json
import openai

openai.api_key = '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'


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Text Improver", layout="centered")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)
 
# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")

prompt = ''

# ---- HEADER SECTION ----
with st.container():
    #st.subheader("Tired of having to analyze and correct text coherence and grammar? 😓")
    st.markdown("<h1 style='text-align: left; color: white; font-size: 26px;'>Tired of having to analyze and correct text coherence and grammar? 😓 </h1>", unsafe_allow_html=True)
    st.markdown("<h1 style='text-align: center; color: white;'>Try TEXT IMPROVER for FREE! ✍ </h1>", unsafe_allow_html=True)
    #st.subheader(
    #    "Text improver is a tool that helps students and professionals streamline their text revision processes, including essays, messages, and similar content. Intrigued? Then give it a try! ✅ ")
    st.markdown("<h1 style='text-align: left; color: white; font-size: 26px;'>Text improver is a tool that helps students and professionals streamline their text revision processes, including essays, messages, and similar content. Intrigued? Then give it a try! ✅ </h1>", unsafe_allow_html=True)

# ---- PROJECTS ----
with st.container():
    st.write("---") 
    grammarColumn, coherencyColumn, cohesionColumn, submitColumn = st.columns((1, 1, 1, 1))

    with grammarColumn: 
        grammar = st.checkbox('Correct Grammar')
    with coherencyColumn:
        coherency = st.checkbox('Improve Coherency')
    with cohesionColumn:
        cohesion = st.checkbox('Enhance Cohesion')
    with submitColumn:
        submitted = st.button('Submit Text')
    
with st.container():
    st.write("---")      # Moved inside the container
    
    inputTextColumn, outputTextColumn = st.columns((1,1))
    
    with inputTextColumn:
        st.header("Your Old Text")
        text_input_area = st.text_area("Enter your text", height=500, max_chars=2000)
    
    
    if(submitted):
        #print('apertei botao')
        if(text_input_area!=''):
            if(coherency or cohesion or grammar):
                prompt = 'Improve this text'

                if coherency:
                    prompt += ' coherency'
                if cohesion:
                    prompt += ' cohesion'
                if grammar:
                    prompt += ' grammar'
                prompt += ':"' + text_input_area + '"'
                
                completion = openai.ChatCompletion.create(
                    model = "gpt-3.5-turbo",
                    messages = [
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )

                prompt = completion.choices[0].message.content.strip('"')
                flagNewPrompt = True

                
    with outputTextColumn:
        st.header("Your New Text!")
        #text_output_area = st.text_area("Copy it and have fun!", height=50, max_chars=500)
        #text_output_area = st.text_area("Copy it and have fun!")
        text_area = st.empty()
     
        text = text_area.text_area("Copy it and have fun!", prompt, height=500, max_chars=2000)
         
# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Simple Instructions")
        st.write(
            """
            - First, paste your text into the 'Your text' box.
            - Then, select the aspects you want to improve in your text: CORRECT GRAMAR, ENHANCE COHESION, and IMPROVE COHERENCE.
            - Third, press the submit button and wait for a while. After that, enjoy your fresh new text!
            - Finally, if you liked TEXT IMPROVER, bookmark this site and SHARE IT WITH YOUR FRIENDS!
            """
        )
        #st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("---")
    st.header("Make suggestions for improvements!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/lucasddoliveira1@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your suggestion/message" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
