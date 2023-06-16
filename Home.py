import streamlit as st

st.header('Pacharapon Yuwansiri and Samart Srichueasakunchai')
st.image(".pic/me.jpg" + ".pic/samart.jpg")
#st.image(".pic/me.jpg")
col1, col2, col3 = st.columns(3)



with col1:
   st.header("Versicolor")
   st.image("./pic/iris1.jpg")

with col2:
   st.header("Verginiga")
   st.image("./pic/iris2.jpg")

with col3:
   st.header("Setosa")
   st.image("./pic/iris3.jpg")
