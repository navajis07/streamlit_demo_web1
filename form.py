import streamlit as st


Name = st.text_input("enter your name: ")
Father_name = st.text_input("enter your father name: ")
Address = st.text_area("enter your address: ")
Class_name= st.selectbox("select your class: ",(1,2,3,4,5,6))

button = st.button("Done")

if button:
    st.markdown(f"""
                  name : {Name}
                  father_name : {Father_name}
                  address : {Address}
                  class_name : {Class_name}
               """)