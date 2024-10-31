import streamlit as st
from utils import load_image, identify_face

# API 키 및 엔드포인트 (Azure 예시)
API_KEY = "YOUR_API_KEY"
API_ENDPOINT = "https://YOUR_REGION.api.cognitive.microsoft.com/face/v1.0/detect"

st.title("Face Identity Checker")
st.header("업로드된 얼굴 이미지를 인식하여 신원을 확인합니다.")

# 파일 업로드 기능
uploaded_file = st.file_uploader("JPG 형식의 얼굴 이미지를 업로드하세요", type=["jpg", "jpeg"])

if uploaded_file is not None:
    # 이미지 로드
    image = load_image(uploaded_file)
    st.image(image, caption="업로드된 이미지", use_column_width=True)

    # 얼굴 인식 처리
    try:
        results = identify_face(uploaded_file, API_KEY, API_ENDPOINT)

        if results:
            st.subheader("인식 결과:")
            for face in results:
                # 예시 정보 표시 (API에서 반환하는 데이터 형식에 따라 수정 필요)
                st.write(f"ID: {face.get('faceId')}")
                st.write(f"감정: {face.get('faceAttributes', {}).get('emotion')}")
                st.write(f"나이: {face.get('faceAttributes', {}).get('age')}")
                st.write("------")
        else:
            st.write("얼굴을 인식하지 못했습니다. 다른 이미지를 시도해보세요.")

    except Exception as e:
        st.error(f"에러 발생: {e}")