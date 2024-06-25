import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## Function to get response from LLama 2 model

def getLLamaresponse(input_text, no_of_words, blog_style):
    llm=CTransformers(model="models\llama-2-7b-chat.ggmlv3.q8_0.bin", model_type="llama", config={'max_new_tokens':256,
                                                                                                  'temperature': 0.01})
    
## Creating the prompt for the model

    template= """
        Write a blog for {blog_style} job profile for a topic "{input_text}" within {no_of_words} words.
        """

    prompt = PromptTemplate(input_variables=["blog_style","input_text","no_of_words"],
                            template=template)

## Generating the response from the LLama model
    response = llm(prompt.format(blog_style = blog_style, input_text = input_text, no_of_words = no_of_words))
    print(response)
    return response

st.set_page_config(page_title="Generate the Blogs", page_icon="👋", layout="centered", initial_sidebar_state="collapsed")
st.header("Generate the Blogs 👋")

input_text = st.text_input("Enter the Blog Prompt")

## Creating two more columns for additional information

col1, col2 = st.columns([5, 5])

with col1:
    no_of_words = st.text_input("Number of words")
with col2:
    blog_style = st.selectbox('Writing the Blog for',('Researcher', 'Data Scientist', 'Common People'),index=0)

Submit = st.button("Generate Blog")

## Final Output

if Submit:
    st.write(getLLamaresponse(input_text, no_of_words, blog_style))


