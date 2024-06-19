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
    st.write('기타 부문')
    st.selectbox('다음 중 김주연이 기차에 앉을 때 선호하는 자리는?', ['창가자리', '복도자리'])

st.write('악기 부문')
select = st.selectbox('김주연이 가장 좋아하는 악기는?', ['피아노', '드럼', '기타'])
st.write(select+'가 선택되었습니다.')
