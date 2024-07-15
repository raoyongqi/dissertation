import os
import pypandoc
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image as PdfImage
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from PIL import Image
from fpdf import FPDF
import PyPDF2

def clean_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')

    # 删除不支持的属性
    for img in soup.find_all('img'):
        if 'alt' in img.attrs:
            del img.attrs['alt']

    return str(soup)

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

    # 生成PDF
    doc.build(story)
    print(f"PDF file created: {output_file}")

def images_to_pdf(image_dir, output_path):
    if not os.path.exists(image_dir):
        raise Exception(f"Directory {image_dir} does not exist")

    # 初始化FPDF对象
    pdf = FPDF()

    # 定义A4页面尺寸
    A4_WIDTH = 210  # A4宽度（单位：毫米）
    A4_HEIGHT = 297  # A4高度（单位：毫米）

    def process_image(image_file):
        # 打开图片文件
        image_path = os.path.join(image_dir, image_file)
        image = Image.open(image_path)
        
        # 获取图片尺寸
        width, height = image.size
        aspect_ratio = height / width
        
        # 调整图片尺寸以适应A4页面
        if width > height:
            new_width = A4_WIDTH
            new_height = A4_WIDTH * aspect_ratio
        else:
            new_height = A4_HEIGHT
            new_width = A4_HEIGHT / aspect_ratio
        
        return image_path, new_width, new_height

    # 遍历图片目录中的所有文件并进行处理
    image_files = [f for f in sorted(os.listdir(image_dir)) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    results = [process_image(image_file) for image_file in image_files]

    # 添加图片到PDF
    for image_path, new_width, new_height in results:
        pdf.add_page()
        pdf.image(image_path, 0, 0, new_width, new_height)

    # 保存PDF文件
    pdf.output(output_path)
    print(f'PDF file created: {output_path}')

def merge_pdfs(pdf_list, output_path):
    pdf_merger = PyPDF2.PdfMerger()

    for pdf in pdf_list:
        pdf_merger.append(pdf)

    with open(output_path, 'wb') as output_file:
        pdf_merger.write(output_file)

    print(f'Merged PDF saved as: {output_path}')

if __name__ == "__main__":
    md_path = 'title.md'
    if not os.path.exists(md_path):
        raise FileNotFoundError(f"{md_path} does not exist.")  # 抛出文件未找到异常
    
    font_path = 'SimHei.ttf'  # 请替换为你下载的中文字体路径
    image_dir = 'pic'  # 请替换为你的图片目录路径

    # 生成Markdown内容的PDF
    md_pdf = 'pdf/md_output.pdf'
    md_to_pdf(md_path, md_pdf, font_path)

    # 生成图片内容的PDF
    images_pdf = 'pdf/images_output.pdf'
    images_to_pdf(image_dir, images_pdf)

    # 合并两个PDF文件
    final_output_pdf = 'pdf/final_output.pdf'
    merge_pdfs([md_pdf, images_pdf], final_output_pdf)
