import wikipediaapi

def fetch_novel_info(novel_title: str) -> str | None:
    """
    Wikipedia에서 소설 정보를 가져옵니다.
    """
    wiki = wikipediaapi.Wikipedia(
        language='ko',
        user_agent='Colab:NovelSceneGenerator:v1.0 (example@example.com)'
    )
    
    page = wiki.page(novel_title)
    if page.exists():
        return page.text
    return None
