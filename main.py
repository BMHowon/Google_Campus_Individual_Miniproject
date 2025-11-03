import os
from utils.fetch_novel import fetch_novel_info
from utils.genai_client import GenAIWrapper
from utils.display_image import display_image

# 1️⃣ API 키 설정
GENAI_API_KEY = os.environ.get("GENAI_API_KEY", "YOUR_API_KEY_HERE")
genai = GenAIWrapper(api_key=GENAI_API_KEY)

# 2️⃣ 사용자 입력
novel_title = input("소설 제목 입력: ")
scene_description = input("장면 한 줄 입력: ")

# 3️⃣ 소설 정보 가져오기
novel_info = fetch_novel_info(novel_title)

if not novel_info:
    print("❌ 소설 정보를 찾을 수 없음")
    exit()

print("✅ 소설 정보 가져오기 성공")
print(novel_info[:500], "...")  # 처음 500자 출력

# 4️⃣ 장면 텍스트 생성
scene_prompt = f"'{novel_title}' 소설의 장면을 시각적으로 묘사해줘.\n\n소설 줄거리:\n{novel_info[:2000]}\n\n장면: {scene_description}"
print("\n🔹 LLM 해석 중...")
scene_text = genai.call_text_model(scene_prompt)

if not scene_text:
    print("❌ LLM 호출 실패")
    exit()

print("\n✨ Gemini 해석 결과:\n")
print(scene_text[:1000], "...")  # 일부만 출력

# 5️⃣ 이미지 생성
print("\n🎨 이미지 생성 중...")
image_bytes = genai.call_image_model(scene_text)

if not image_bytes:
    print("❌ 이미지 생성 실패")
    exit()

# 6️⃣ 이미지 출력
display_image(image_bytes)
