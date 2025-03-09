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
import shutil
from pathlib import Path

import tqdm
from css_html_js_minify import process_single_html_file


class PARAM:
    BED_SRC = "https://cdn.jsdelivr.net/gh/yiyifengheju/picbed@main/"
    BED_DST = "https://picbed.mastermao.cn/"
    FONT_NOTO = "NotoSerifSC-SemiBold.otf"

    PATH_SITE = "../site"
    PATH_FONTS = "../site/stylesheets/FONTS"
    PATH_CSS = "../site/stylesheets"


class AutoBuild:
    def __init__(self, *, is_switch_bed=False):
        self.bed_src = PARAM.BED_SRC
        self.bed_dst = PARAM.BED_DST
        self.swc_bed = is_switch_bed

    @staticmethod
    def _get_html():
        htmls = []
        for root, _, files in os.walk(PARAM.PATH_SITE):
            tmp = [Path(root, file) for file in files if file.endswith(".html")]
            htmls.extend(tmp)
        return htmls

    def switch_pic_bed(self, contents):
        return [line.replace(self.bed_src, self.bed_dst) for line in contents]

    def get_letters(self, files):
        char_list = []
        t_files = tqdm.tqdm(files)
        for file in t_files:
            with Path(file).open("r", encoding="utf8") as f:
                contents = f.readlines()
            t_files.set_description(file.name)
            if self.swc_bed:
                contents = self.switch_pic_bed(contents)
                with Path(file).open("w", encoding="utf8") as f:
                    f.writelines(contents)
            for content in contents:
                char_list.extend(list(content))
        return list(set(char_list))

    @staticmethod
    def _build():
        cmd = "cd .. && mkdocs build"
        re = os.system(cmd)
        assert [1, 0][re], "构建失败"

    @staticmethod
    def generate_fonts(font_family, letters):
        char_unicode = [
            str(item.encode("unicode_escape").decode()).split("u")[-1].upper() + "\n"
            for item in letters
            if "\u4e00" <= item <= "\u9fff"
        ]
        with Path("./Fonts/sc_unicode.txt").open("w", encoding="utf8") as f:
            f.writelines(char_unicode)

        cmd = f"cd ./Fonts && pyftsubset {font_family} --unicodes-file=sc_unicode.txt"
        re = os.system(cmd)
        assert [1, 0][re], "生成字体失败"

    @staticmethod
    def copy_fonts():
        if not Path(PARAM.PATH_FONTS).exists():
            Path(PARAM.PATH_FONTS).mkdir(parents=True, exist_ok=True)
        shutil.copy("./Fonts/NotoSerifSC-SemiBold.subset.otf", f"{PARAM.PATH_FONTS}/NotoSerifSC-SemiBold.subset.otf")
        shutil.copy("./Fonts/Lato.woff2", f"{PARAM.PATH_FONTS}/Lato.woff2")
        shutil.copy("./Fonts/monaco.woff2", f"{PARAM.PATH_FONTS}/monaco.woff2")

    @staticmethod
    def merge_css():
        min_css = os.listdir(PARAM.PATH_CSS)
        css_list = []
        for css in min_css:
            if css[-8:] == ".min.css":
                with Path(f"{PARAM.PATH_CSS}/{css}").open("r", encoding="utf-8") as f:
                    content = f.readlines()
                css_list.extend(content)
        shutil.rmtree(PARAM.PATH_CSS)
        Path(PARAM.PATH_CSS).mkdir(parents=True, exist_ok=True)
        with Path(f"{PARAM.PATH_CSS}/extra.css").open("w", encoding="utf-8") as f:
            f.writelines(css_list)

    @staticmethod
    def minify_html(htmls):
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


if __name__ == "__main__":
    ab = AutoBuild()
    ab.run()
