"""
=========================================================================
@File Name: AutoBuild.py
@Time: 2024/10/22 23:43
@Program IDE：PyCharm
@Create by Author: 一一风和橘
@Motto: "The trick, William Potter, is not minding that it hurts."
@Description:
- 
- 
=========================================================================
"""
import os

import tqdm
from css_html_js_minify import process_single_html_file
import shutil


class PARAM:
    BED_SRC = 'https://cdn.jsdelivr.net/gh/yiyifengheju/picbed@main/'
    BED_DST = 'https://picbed.mastermao.cn/'
    FONT_NOTO = 'NotoSerifSC-SemiBold.otf'


class AutoBuild:
    def __init__(self,
                 swc_bed=False):
        self.bed_src = PARAM.BED_SRC
        self.bed_dst = PARAM.BED_DST
        self.swc_bed = swc_bed

        self.path_site = '../site'
        self.path_fonts = '../site/stylesheets/FONTS'
        self.path_css = '../site/stylesheets'

    def _get_html(self):
        htmls = []
        for root, dirs, files in os.walk(self.path_site):
            for file in files:
                if file.endswith('.html'):
                    htmls.append(os.path.join(root, file))
        return htmls

    def switch_pic_bed(self, contents):
        contents = [line.replace(self.bed_src, self.bed_dst) for line in contents]
        return contents

    def get_letters(self, files):
        char_list = []
        t_files = tqdm.tqdm(files)
        for file in t_files:
            with open(file, 'r', encoding='utf8') as f:
                contents = f.readlines()
            t_files.set_description(file)
            if self.swc_bed:
                contents = self.switch_pic_bed(contents)
                with open(file, 'w', encoding='utf8') as f:
                    f.writelines(contents)
            for content in contents:
                char_list.extend(list(content))
        letters = list(set(char_list))
        return letters

    @staticmethod
    def _build():
        cmd = 'cd .. && mkdocs build'
        re = os.system(cmd)
        assert [1, 0][re], '构建失败'

    @staticmethod
    def generate_fonts(font_family, letters):
        char_unicode = [str(item.encode('unicode_escape').decode()).split('u')[-1].upper() + '\n' for item in
                        letters if '\u4e00' <= item <= '\u9fff']
        with open('./Fonts/sc_unicode.txt', 'w', encoding='utf8') as f:
            f.writelines(char_unicode)

        cmd = f'cd ./Fonts && pyftsubset {font_family} --unicodes-file=sc_unicode.txt'
        re = os.system(cmd)
        assert [1, 0][re], '生成字体失败'

    def copy_fonts(self):
        if not os.path.exists(self.path_fonts):
            os.mkdir(self.path_fonts)
        shutil.copy('./Fonts/NotoSerifSC-SemiBold.subset.otf', f'{self.path_fonts}/NotoSerifSC-SemiBold.subset.otf')
        shutil.copy('./Fonts/Lato.woff2', f'{self.path_fonts}/Lato.woff2')
        shutil.copy('./Fonts/monaco.woff2', f'{self.path_fonts}/monaco.woff2')

    def merge_css(self):
        min_css = os.listdir(self.path_css)
        css_list = []
        for css in min_css:
            if css[-8:] == '.min.css':
                with open(f'{self.path_css}/{css}', 'r', encoding='utf-8') as f:
                    content = f.readlines()
                css_list.extend(content)
        shutil.rmtree(self.path_css)
        os.mkdir(self.path_css)
        with open(f'{self.path_css}/extra.css', 'w', encoding='utf-8') as f:
            f.writelines(css_list)

    def minify_html(self,htmls):
        for html in htmls:
            process_single_html_file(html, overwrite=True)


    def run(self):
        self._build()

        htmls = self._get_html()
        letters = self.get_letters(htmls)
        self.generate_fonts(PARAM.FONT_NOTO, letters)

        self.merge_css()
        self.copy_fonts()

        self.minify_html(htmls)



if __name__ == '__main__':
    ab = AutoBuild()
    ab.run()