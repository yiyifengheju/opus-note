"""
====================================
@File Name: auto_build.py
@Time: 2023/4/10 0:33
@Program IDE：PyCharm
@Create by Author: 一一风和橘
@Motto: "The trick, William Potter, is not minding that it hurts."
@Description:
- 图床重命名
====================================
"""
import os
import shutil

import tqdm

GITHUB_BED = 'https://cdn.jsdelivr.net/gh/yiyifengheju/picbed@main/'
GITEE_BED = 'https://mastermao.gitee.io/picbed/'


def switch_pic_bed(contents):
    new_contents = [line.replace(GITHUB_BED, GITEE_BED) for line in contents]
    return new_contents


def get_html():
    html_files = []
    path = '../site'
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    return html_files


def get_letters(files):
    char_list = []
    t_files = tqdm.tqdm(files)
    for file in t_files:
        with open(file, 'r', encoding='utf8') as f:
            contents = f.readlines()
        t_files.set_description(file)
        # new_contents = switch_pic_bed(contents)
        for content in contents:
            char_list.extend(list(content))
        # with open(file, 'w', encoding='utf8') as f:
        #     f.writelines(new_contents)

    char_simple_list = list(set(char_list))
    return char_simple_list


def merge_css():
    css_path = '../site/stylesheets'
    min_css = os.listdir(css_path)
    css_list = []
    for css in min_css:
        if '.min.css' not in css:
            continue
        if css == 'extra.min.css':
            continue
        with open(f'{css_path}/{css}', 'r', encoding='utf-8') as f:
            content = f.readlines()
        css_list.extend(content)
    shutil.rmtree(css_path)
    os.mkdir('../site/stylesheets')
    with open('../site/stylesheets/extra.css', 'w', encoding='utf-8') as f:
        f.writelines(css_list)


def generate_fonts(letter_list):
    char_unicode = [str(item.encode('unicode_escape').decode()).split('u')[-1].upper() + '\n' for item in
                    letter_list if '\u4e00' <= item <= '\u9fff']
    with open('./Fonts/sc_unicode.txt', 'w', encoding='utf8') as f:
        f.writelines(char_unicode)

    cmd = 'cd ./Fonts && pyftsubset NotoSerifSC.otf --unicodes-file=sc_unicode.txt'
    re = os.system(cmd)
    assert [1, 0][re], '生成字体失败'
    if not os.path.exists('../site/stylesheets/FONTS'):
        os.mkdir('../site/stylesheets/FONTS')
    shutil.copy('./Fonts/NotoSerifSC.subset.otf', '../site/stylesheets/FONTS/NotoSerifSC.subset.otf')
    shutil.copy('./Fonts/Lato.woff2', '../site/stylesheets/FONTS/Lato.woff2')
    shutil.copy('./Fonts/monaco.woff2', '../site/stylesheets/FONTS/monaco.woff2')


def build():
    cmd = 'cd .. && mkdocs build'
    re = os.system(cmd)
    assert [1, 0][re], '构建失败'


if __name__ == '__main__':
    # 部署
    build()

    # 修改图床并获取全部汉字
    html_list = get_html()
    letters = get_letters(html_list)

    # 合并CSS
    merge_css()

    # 生成字体
    generate_fonts(letters)
