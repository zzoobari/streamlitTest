import streamlit as st 
st.title('첫번째 웹 어플 만들기 👋')
st.write('# 1. Markdown 텍스트 작성하기')
st.markdown(
    '''
    # 마크다운 헤더1
    - 마크다운 목록1. **굵게** 표시
    - 마크다운 목록2. *기울임* 표시
        - 마크다운 목록2-1
        - 마크다운 목록2-2

    ## 마크다운 헤더2
    - [네이버](https://naver.com)
    - [구글](https://google.com)

    ### 마크다운 헤더3
    일반 텍스트
    '''
    )
import pandas as pd
st.write('# 2. DataFrame 표시하기') 
df = pd.DataFrame({  # DataFrame 생성
    '이름': ['홍길동', '이순신', '강감찬'],
    '나이': [20, 45, 35]
})
st.dataframe(df)