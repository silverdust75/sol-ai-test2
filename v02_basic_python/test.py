import streamlit as st

# 1. 함수 정의
def kg_to_pound(kg):
    return kg * 2.20462

# 2. 웹 UI 구성
st.title("⚖️ 단위 변환기: kg to pound")
st.write("변환하고 싶은 무게(kg)를 입력하면 파운드(lb)로 계산해 드립니다.")

# 3. 사용자 입력 (웹 페이지의 입력창)
kg = st.number_input("변환할 kg 단위를 입력하세요.", min_value=0.0, format="%.2f")

# 4. 버튼 및 결과 출력
if st.button("변환하기"):
    pound = kg_to_pound(kg)
    st.success(f"결과: {kg}kg은 **{pound:.2f} pound**입니다.")
    st.balloons() # 축하 효과!