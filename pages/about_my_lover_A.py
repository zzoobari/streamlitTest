import streamlit as st
st.header('제가 좋아하는 것들을 소개합니다.⸜(｡˃ ᵕ ˂ )⸝♡')
st.header('저의 취향을 맞춰보세요_정답')
col_1, col_2, col_3 = st.columns([1,1,1]) 
with col_1:
    st.write('음식 부문')
    st.write('정답: 마라탕, 떡볶이, 샤브샤브, 김치볶음밥')
 
with col_2:
    st.write('취미 부문')
    st.write('정답: 틱톡 촬영은 김주연의 취미가 아닙니다.')
    
st.markdown(


    ## 김주연의 블로그
    - [김주연의 블로그](https://blog.naver.com/rlawnqkf21)
    ## 김주연의 유튜브
    - [김지붕붕](https://www.youtube.com/channel/UCNgfnSxxZiP5oFf_bGKDkKw)

with col_3:  
    st.write('기타 부문')
    st.write('정답: 창가자리')

st.write('악기 부문')
st.write('정답은 기타입니다.')
