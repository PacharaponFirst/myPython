import streamlit as st

st.header('Pacharapon Yuwansiri and Samart Srichueasakunchai')
#st.image(".pic/me.jpg")
#st.image(".pic/samart.jpg")

colA, colB = st.columns(2)
with colA:
    st.header("Pacharapon Yuwansiri")
    st.image("./pic/me.jpg")

with colB:
    st.header("Samart Srichueasakunchai")
    st.image("./pic/samart.jpg")
   
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

   html_8 = """


<div style="background-color:#EC7063;padding:15px;border-radius:15px 15px 15px 15px;border-style:'solid';border-color:black">
<center><h5>การทำนายข้อมูลดอกไม้</h5></center>
</div>
"""

st.markdown(html_8, unsafe_allow_html=True)
st.markdown("")

pt_len = st.slider("กรุณาเลือกข้อมูล petal.length")
pt_wd = st.slider("กรุณาเลือกข้อมูล petal.width")

sp_len = st.number_input("กรุณาเลือกข้อมูล sepal.length")
sp_wd = st.number_input("กรุณาเลือกข้อมูล sepal.width")

if st.button("ทำนายผล"):
    st.write("ทำนาย")
else:
    st.write("ไม่ทำนาย")