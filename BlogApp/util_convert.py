from pathlib import Path
import re
from slugify import slugify

BASE_DIR = Path(__file__).resolve().parent.parent

FILE_NAME = BASE_DIR / "site-2021-12-13.sql"
with open(FILE_NAME, 'r', encoding='utf8') as f:
    content = f.readlines()
    content = [''.join(i) for i in content]
    content = str(content)
    patten = re.compile(
        r"\/\*!40000 ALTER TABLE `blog_blog` DISABLE KEYS \*\/;.*?\(.*?\),.*\/\*!40000 ALTER TABLE `blog_blog` ENABLE KEYS \*\/;",
        re.S)
    # 整个blog_blog表
    content = patten.findall(content)
    content = content[0]
    patten = re.compile(r".*?\((\d+),.*?\),.*?", re.S)
    # 所有的文章id
    ids = patten.findall(content)
    print(f"总共有{len(ids)}个id")
    patten = re.compile(r"\(.*\);", re.S)
    # 所有的文章
    content = patten.findall(content)
    content = content[0]

    patten = re.compile(r"\(\d+.*?\),", re.S)
    content = patten.findall(content)
    # 所有的文章，表格每一条数据是一篇文章(最后一条数据有问题)
    contents = content[:-2]
    # 分析第一条文章，取标题

    with open(BASE_DIR / "new-blog.txt", 'a', encoding='utf-8') as f:
        f.write("INSERT INTO blog_blog VALUES")
    for index in range(len(contents)):
        content = contents[index]
        # content = content[3]
        try:
            id = ids[index]
            patten_title = re.compile(r"\(\d+,(.*?),")
            patten_content = re.compile(r"\(\d+,.*?,(.*?),\\'")
            patten_created_time = re.compile(r"\(\d+,.*?,.*?,(\\'.*?),")
            patten_updated_time = re.compile(r"\(\d+,.*?,.*?,\\'.*?,(\\'.*?),")
            content1 = patten_title.findall(content)
            content2 = patten_content.findall(content)
            content3 = patten_created_time.findall(content)
            content4 = patten_updated_time.findall(content)
            # 一篇的标题
            content1 = content1[0].replace("\\", '')
            slug = "'" + slugify(content1) + "'"
            # 一篇的内容
            content2 = content2[0].replace("\\'", "'").replace(
                '\\"', '"').replace('\\"', '"').replace('\\\\r\\\\n', '\r\n')
            content3 = content3[0].replace("\\", '')
            # 一篇的更新时间
            content4 = content4[0].replace("\\", '')
            with open(BASE_DIR / "new-blog.txt", 'a', encoding='utf-8') as f:
                f.write("(" + id + "," + content1 + "," + slug + "," +
                        content2 + "," + content3 + "," + content4 +
                        ',1,NULL,NULL),')
            print(content1)
        except:
            print("---" + str(content1))
