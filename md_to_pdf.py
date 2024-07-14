

import os
import markdown
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

def clean_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # 删除不支持的属性
    for img in soup.find_all('img'):
        if 'alt' in img.attrs:
            del img.attrs['alt']

    return str(soup)

def md_to_pdf(input_file, output_file):
    # 读取Markdown文件内容
    with open(input_file, 'r', encoding='utf-8') as file:
        md_content = file.read()
    
    # 将Markdown内容转换为HTML
    html_content = markdown.markdown(md_content)

    # 清理HTML内容
    cleaned_html = clean_html(html_content)
    
    # 创建PDF文档
    doc = SimpleDocTemplate(output_file, pagesize=letter)
    styles = getSampleStyleSheet()
    normal_style = styles['Normal']
    
    # 添加自定义样式
    header_style = ParagraphStyle(name='Header', fontSize=18, leading=22, spaceAfter=10)
    subheader_style = ParagraphStyle(name='SubHeader', fontSize=14, leading=18, spaceAfter=10)

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
    
    # 生成PDF
    doc.build(story)
    print(f"PDF file created: {output_file}")

if __name__ == "__main__":
    md_path = 'title.md'
    if not os.path.exists(md_path):
        raise  # 请替换为你的Markdown文件路径
    output_file = 'pdf/output.pdf' # 请替换为你的PDF输出路径
    md_to_pdf(md_path, output_file)