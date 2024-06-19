import streamlit as st
st.header('제가 좋아하는 것들을 소개합니다.⸜(｡˃ ᵕ ˂ )⸝♡')
st.header('저의 취향을 맞춰보세요')
col_1, col_2, col_3 = st.columns([1,1,1]) 
with col_1:
    st.write('음식 부문(복수정답)')
    st.checkbox('마라탕')
    st.checkbox('떡볶이')
    st.checkbox('돼지국밥')
    st.checkbox('육회초밥')
    st.checkbox('샤브샤브')
    st.checkbox('김치볶음밥')
 
with col_2:
    st.write('취미 부문')
    st.radio('김주연의 취미가 아닌 것을 고르시오', ['틱톡 촬영', '블로그 쓰기', '유튜브 찍기'])

with col_3:  
    st.write('')
    st.selectbox('3번 컬럼의 셀렉트박스', ['select 1', 'select 2', 'select 3'])
    