from IPython.display import Image, display

def display_image(image_path_or_bytes):
    """
    이미지 파일 경로나 바이트 데이터를 Colab/Notebook에서 출력
    """
    if isinstance(image_path_or_bytes, str):
        display(Image(filename=image_path_or_bytes))
    else:
        display(Image(data=image_path_or_bytes))
