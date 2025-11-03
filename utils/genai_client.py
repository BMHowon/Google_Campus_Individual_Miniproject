from google.genai import client as genai_client
import base64
import traceback

class GenAIWrapper:
    def __init__(self, api_key: str):
        self.client = genai_client.Client(api_key=api_key)

    def call_text_model(self, prompt: str, model="gemini-1.5-flash", max_output_tokens=512) -> str:
        try:
            resp = self.client.models.generate_content(model=model, contents=prompt)
            # 다양한 SDK 형태 대응
            text = getattr(resp, "text", None)
            if text:
                return text
            try:
                return resp.candidates[0].content[0].text
            except Exception:
                pass
            return str(resp)
        except Exception as e:
            print("LLM 호출 에러:", e)
            traceback.print_exc()
            return None

    def call_image_model(self, prompt: str, model="models/gemini-2.5-flash-image") -> bytes | None:
        try:
            resp = self.client.models.generate_content(
                model=model,
                contents=prompt,
                generation_config={"response_mime_type": "image/png"}
            )
            try:
                b64 = resp.candidates[0].content.parts[0].inline_data.data
                return base64.b64decode(b64)
            except Exception:
                return None
        except Exception as e:
            print("이미지 모델 호출 에러:", e)
            traceback.print_exc()
            return None
