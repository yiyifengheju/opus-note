"""
=========================================================================
@File Name: AutoIndex.py
@Time: 2024/10/22 23:43
@Program IDE：PyCharm
@Create by Author: 一一风和橘
@Motto: "The trick, William Potter, is not minding that it hurts."
@Description:
-
-
=========================================================================
"""

import copy
import os
from pathlib import Path

import toml
import tomllib
import yaml
from loguru import logger

EXCLUDE_FOLDERS = ["assets", "blog", "javascripts", "stylesheets", "留言板"]
SKIP_FOLDERS = [
    "index.toml",
    "index.md",
    "info.toml",
    "nav.toml",
    ".ipynb_checkpoints",
    "datalab-files",
    "catboost_info",
    ".pages",
]
TOML_FILE_TEMPLATE = {
    "title": "",
    "emoji": "",
    "info": "",
    "cover": "",
    "path": "",
}
SVG_FOLDER = ":material-folder-open:"


class AutoIndex:
    def __init__(self, path, exclude_folders=None):
        self.path = path
        self.emojis = []
        if exclude_folders is None:
            self.exclude_folders = EXCLUDE_FOLDERS
        else:
            self.exclude_folders = exclude_folders

    def _get_folders(self):
        folders = os.listdir(self.path)
        return [item for item in folders if Path(f"{self.path}/{item}").is_dir() and item not in self.exclude_folders]

    @staticmethod
    def _get_toml_template(title):
        tmp = copy.copy(TOML_FILE_TEMPLATE)
        tmp["title"] = title
        return tmp

    @staticmethod
    def _get_metadata(path):
        with Path(path).open("r", encoding="utf-8") as f:
            content = f.read()
        start = "---"
        end = "---"
        ss = content.find(start) + len(start)
        ee = content.find(end, ss)
        if ss == -1 or ee == -1:
            return None
        metadata = content[ss:ee].strip()
        return yaml.safe_load(metadata)

    def _generate_index(self, c1_folder):
        pth_index_md = f"{self.path}/{c1_folder}/index.md"
        pth_index_toml = f"{self.path}/{c1_folder}/index.toml"
        with Path(pth_index_toml).open("rb") as f:
            info_dict = tomllib.load(f)

        info_head = [
            "---\n",
            f"title: {c1_folder}\n",
            "comments: false\n",
            "hide:\n",
            "   - toc\n",
            "---\n\n",
            '<div class="grid cards index-info" markdown>\n\n',
        ]

        for key in info_dict:
            title = info_dict[key]["title"].split(" ")[-1]
            is_folder = Path(info_dict[key]["path"]).is_dir()
            target = f"./{key}/index.md" if is_folder else f"./{key}"
            # cover = (
            #     f'[![{key}]({info_dict[key]["cover"]}){{.no-glb}}]({target})\n{{ .description }}\n\n'
            #     if info_dict[key]["cover"]
            #     else ""
            # )
            msg = f'{info_dict[key]["info"]}\n{{ .description }}\n\n' if info_dict[key]["info"] else "\n\n"
            emoji = info_dict[key]["emoji"]
            info = [
                f'-   {emoji}{{ .{emoji.replace(":","")} .icon }} &ensp;&ensp;__[{title}]'
                f'({target}){{ .icon_title }}__\n{{ .cards }}\n\n',
                "\t---\n\n",
                # f"\t{cover}",
                f"\t{msg}",
                f"\t[:octicons-arrow-right-24: Getting started]({target})\n{{ .description }}\n\n",
            ]
            # print(f'.{emoji.replace(":", "")}{{color: ;}}')  # noqa: T201
            self.emojis.append(f'.{emoji.replace(":", "")}{{color: ;}}')
            info_head.extend(info)

        with Path(pth_index_md).open("w", encoding="utf-8") as f:
            info_head.append("</div>")
            f.writelines(info_head)

        files = os.listdir(f"{self.path}/{c1_folder}")
        files = sorted(files, reverse=False)
        for file in files:
            if file in SKIP_FOLDERS:
                continue
            if Path(f"{self.path}/{c1_folder}/{file}").is_file():
                continue
            # self._generate_index(f'{c1_folder}/{file}')
            # 修改这里不再嵌套，直接使用目录
            self._generate_mulu(f"{c1_folder}/{file}")

    def _generate_mulu(self, path):
        with Path(f"{self.path}/{path}/index.toml").open("rb") as f:
            info_dict = tomllib.load(f)
        title = os.path.split(path)[-1]
        info_head = [
            "---\n",
            f"title: {title}\n",
            "comments: false\n",
            "hide:\n",
            "   - toc\n",
            "---\n\n",
            '<div class="grid cards index-info" markdown>\n\n',
            f"-   {SVG_FOLDER}{{.svg_folder}}&emsp;__[{path}](./index.md)__\n{{ .cards }}\n\n",
            "\t---\n\n",
        ]
        for key in info_dict:
            tit = info_dict[key]["title"]
            pth = os.path.split(info_dict[key]["path"])[-1]
            info = f"\t&emsp;:material-arrow-expand-right:&emsp;[{tit}](./{pth})\n\n"
            info_head.append(info)
        with Path(f"{self.path}/{path}/index.md").open("w", encoding="utf-8") as f:
            info_head.append("</div>")
            f.writelines(info_head)

    def _check_toml(self, c1_folder):
        info_dict = {}
        c2_folders = os.listdir(f"{self.path}/{c1_folder}")
        if "index.toml" in c2_folders:
            logger.info(f"{c1_folder}/index.toml ✔️")
            with Path(f"{self.path}/{c1_folder}/index.toml").open("rb") as f:
                info_dict = tomllib.load(f)
            for c2_folder in c2_folders:
                if c2_folder in ["index.toml", "index.md", "info.toml", "nav.toml", ".pages"]:
                    continue
                if c2_folder in SKIP_FOLDERS:
                    continue
                if c2_folder not in info_dict:
                    info_dict[c2_folder] = self._get_toml_template(c2_folder)
                pth_file = f"{self.path}/{c1_folder}/{c2_folder}"
                info_dict[c2_folder].update({"path": f"./{c1_folder}/{c2_folder}"})
                if Path(pth_file).is_file():
                    meta = "" if c2_folder.endswith(".ipynb") else self._get_metadata(pth_file)
                    print(pth_file)
                    info_dict[c2_folder].update(meta)
                else:
                    self._check_toml(f"{c1_folder}/{c2_folder}")
        else:
            logger.info(f"{c1_folder}/index.toml 🎉🎉")
            for c2_folder in c2_folders:
                if c2_folder in ["index.toml", "index.md", "info.toml", "nav.toml", ".pages"]:
                    continue
                if c2_folder in SKIP_FOLDERS:
                    continue
                if c2_folder not in info_dict:
                    info_dict[c2_folder] = self._get_toml_template(c2_folder)
                pth_file = f"{self.path}/{c1_folder}/{c2_folder}"
                info_dict[c2_folder].update({"path": pth_file})
                if Path(pth_file).is_file():
                    meta = "" if c2_folder.endswith(".ipynb") else self._get_metadata(pth_file)
                    info_dict[c2_folder].update(meta)
                else:
                    self._check_toml(f"{c1_folder}/{c2_folder}")
        with Path(f"{self.path}/{c1_folder}/index.toml").open("w", encoding="utf-8") as f:
            info_dict = {k: info_dict[k] for k in sorted(info_dict.keys())}
            toml.dump(info_dict, f)

    def run(self):
        folders = self._get_folders()
        for c1_folder in folders:
            if c1_folder in SKIP_FOLDERS:
                continue
            self._check_toml(c1_folder)
            self._generate_index(c1_folder)


if __name__ == "__main__":
    pth_docs = "../docs"
    auto_index = AutoIndex(pth_docs)
    auto_index.run()

    [print(item) for item in set(auto_index.emojis)]
