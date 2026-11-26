import streamlit as st
from models import gemini

#metadata
st.set_page_config(
    page_title='Gemini API Project',
    page_icon=':robot:',
    layout='wide'
)

st.title('Streamlit :blue[Pro]:red[ject] :grin:', icon = '🤖')
st.header('Gemini Project :green[:robot:]')
st.subheader(':blue[Using] :red[Gemini-3.6-flash] :blue[Model]')

prompt = st.text_area('Enter Your Prompt', placeholder='Ask me anything 😉')
button_clicked = st.button('Send Prompt :airplane:')

if button_clicked:
    if prompt.strip() == '':
        st.warning("Prompt field can not be empty")
    else:
        with st.spinner('Generating Content'):
            answer = gemini(prompt)
            st.success('Content Generated')
            st.write(answer)


