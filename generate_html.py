import requests
from bs4 import BeautifulSoup

# 定义目录链接
directory_url = "http://43.136.235.235/d/%E8%B5%84%E6%96%99/news"

# 发送HTTP请求并获取目录页面内容
response = requests.get(directory_url)
html_content = response.content

# 使用BeautifulSoup解析HTML内容
soup = BeautifulSoup(html_content, "html.parser")

# 找到所有图片链接
image_links = []
for link in soup.find_all("a"):
    href = link.get("href")
    if href.endswith(".jpg") or href.endswith(".jpeg") or href.endswith(".png"):
        image_links.append(href)

# 生成HTML文件模板
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Image Slider</title>
  <style>
    body {
      margin: 0;
      padding: 0;
      overflow: hidden;
    }
    .slider-container {
      width: 100%;
      height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      overflow: hidden;
    }
    .slider {
      width: 100%;
      display: flex;
      align-items: center;
      transition: transform 0.3s ease;
    }
    .slide {
      flex: 0 0 100%;
      overflow: hidden;
    }
    img {
      width: 100%;
      height: auto;
    }
  </style>
</head>
<body>
  <div class="slider-container">
    <div class="slider">
      %s
    </div>
  </div>

  <script>
    const slider = document.querySelector('.slider');
    const slides = document.querySelectorAll('.slide');
    let currentSlide = 0;

    slider.addEventListener('click', (event) => {
      const width = slides[0].clientWidth;
      const x = event.clientX;

      if (x < window.innerWidth / 2) {
        currentSlide--;
        if (currentSlide < 0) {
          currentSlide = slides.length - 1;
        }
      } else {
        currentSlide++;
        if (currentSlide >= slides.length) {
          currentSlide = 0;
        }
      }
      slider.style.transform = `translateX(-${currentSlide * width}px)`;
    });
  </script>
</body>
</html>
"""

# 替换图片链接
image_tags = ""
for idx, link in enumerate(image_links, start=1):
    image_tags += f"<div class='slide'><img src='{link}' alt='Image {idx}'></div>\n"

# 插入图片链接到HTML模板中
final_html = html_template % image_tags

# 将HTML内容写入文件
with open("image_slider.html", "w") as f:
    f.write(final_html)

print("HTML文件已生成！")
