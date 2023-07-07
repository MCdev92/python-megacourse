import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("/Users/mcdev92/repos/python-megacourse/intermediate/portofolio/images/mypic.png")

    
with col2:
    st.title("Manuel Corporan")
    content = """ 
    Hello there thank you for stopping by my website, my name is Manuel, 
    I live in San Lorenzo, California and I am currently pursuing a career
    as a software engineer. I recently graduated from community college 
    with an Associate of Science in Business Administration and Associate of Arts in Economics. 
    I am continuing my studies in California State University - East Bay in the 
    Information Administration field. I have some experience with 
    python, C# and golang programing languages. I am looking forward to 
    improve my skills and become an efficient programmer."""
    
    st.info(content)


content = """ 
    Below you can find some of the projects I have built. Feel free to contact me! """
    
st.write(content)    