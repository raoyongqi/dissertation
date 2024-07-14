import os
import pypandoc
import requests
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics

def clean_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # 删除不支持的属性
    for img in soup.find_all('img'):
        if 'alt' in img.attrs:
            del img.attrs['alt']

    return str(soup)

def download_image(img_url, img_dir):
    # 提取图片文件名
    img_filename = img_url.split('/')[-1]
    img_path = os.path.join(img_dir, img_filename)

    # 下载图片
    response = requests.get(img_url, stream=True)
    with open(img_path, 'wb') as img_file:
        for chunk in response.iter_content(chunk_size=128):
            img_file.write(chunk)

    return img_path

def md_to_pdf(input_file, output_file, font_path):
    # 注册中文字体
    pdfmetrics.registerFont(TTFont('SimHei', font_path))

    # 将Markdown文件转换为HTML
    html_content = pypandoc.convert_file(input_file, 'html', format='markdown')

    # 清理HTML内容
    cleaned_html = clean_html(html_content)
    
    # 创建PDF文档
    doc = SimpleDocTemplate(output_file, pagesize=letter)
    styles = getSampleStyleSheet()
    normal_style = ParagraphStyle(name='Normal', fontName='SimHei', fontSize=12)
    
    # 添加自定义样式
    header_style = ParagraphStyle(name='Header', fontName='SimHei', fontSize=18, leading=22, spaceAfter=10)
    subheader_style = ParagraphStyle(name='SubHeader', fontName='SimHei', fontSize=14, leading=18, spaceAfter=10)

    story = []
    
    # 将HTML内容解析为Paragraph对象并添加到story中
    soup = BeautifulSoup(cleaned_html, 'html.parser')
    
    for element in soup.contents:
        if element.name == 'h1':
            story.append(Paragraph(element.get_text(), header_style))
            story.append(Spacer(1, 12))
        elif element.name == 'h2':
            story.append(Paragraph(element.get_text(), subheader_style))
            story.append(Spacer(1, 10))
        elif element.name in ['p', 'li']:
            story.append(Paragraph(element.get_text(), normal_style))
            story.append(Spacer(1, 6))
        elif element.name == 'ul':
            for li in element.find_all('li'):
                story.append(Paragraph(f"- {li.get_text()}", normal_style))
                story.append(Spacer(1, 6))
        elif element.name == 'img':
            img_url = element['src']
            img_path = download_image(img_url, 'images')  # 将图片下载到 'images' 文件夹中
            try:
                img = Image(img_path)
                story.append(img)
                story.append(Spacer(1, 12))
            except Exception as e:
                print(f"Failed to insert image '{img_url}': {e}")
                continue
    
    # 生成PDF
    doc.build(story)
    print(f"PDF file created: {output_file}")


if __name__ == "__main__":
    md_path = 'title.md'
    if not os.path.exists(md_path):
        raise  # 请替换为你的Markdown文件路径
    output_file = 'pdf/output.pdf' # 请替换为你的PDF输出路径
    md_to_pdf(md_path, output_file,'SimHei.ttf')
