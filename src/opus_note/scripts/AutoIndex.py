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
import tomllib

import toml
import yaml
from loguru import logger

EXCLUDE_FOLDERS = ['assets', 'blog', 'javascripts', 'stylesheets', '留言板', '🎁 信号处理', '🎈 其他编程']
SKIP_FOLDERS = ['index.toml', 'index.md', 'info.toml', 'nav.toml', '.ipynb_checkpoints', 'datalab-files',
                'catboost_info', '.pages']
TOML_FILE_TEMPLATE = {'title': "",
                      'emoji': "",
                      'info': "",
                      'cover': "",
                      'path': ""
                      }


class AutoIndex:

    def __init__(self,
                 path,
                 exclude_folders=None):

        self.path = path
        if exclude_folders is None:
            self.exclude_folders = EXCLUDE_FOLDERS
        else:
            self.exclude_folders = exclude_folders

    def _get_folders(self):
        folders = os.listdir(self.path)
        folders = [item for item in folders if
                   os.path.isdir(f'{self.path}/{item}') and item not in self.exclude_folders]
        return folders

    @staticmethod
    def _get_toml_template(title):
        tmp = copy.copy(TOML_FILE_TEMPLATE)
        tmp['title'] = title
        return tmp

    @staticmethod
    def _get_metadata(path):
        with open(path, 'r', encoding='utf-8') as f:
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
        pth_index_md = f'{self.path}/{c1_folder}/index.md'
        pth_index_toml = f'{self.path}/{c1_folder}/index.toml'
        with open(pth_index_toml, "rb") as f:
            info_dict = tomllib.load(f)

        info_head = ['---\n',
                     f'title: {c1_folder}\n',
                     'comments: false\n',
                     'hide:\n',
                     '   - toc\n',
                     '---\n',
                     '\n'
                     '<div class="grid cards index-info" markdown>\n\n']

        for key in info_dict.keys():
            title = info_dict[key]['title'].split(' ')[-1]
            is_folder = os.path.isdir(info_dict[key]['path'])
            target = f'./{key}/index.md' if is_folder else f'./{key}'
            cover = f'[![{key}]({info_dict[key]["cover"]}){{.no-glb}}]({target})' if info_dict[key]["cover"] else ''
            msg = info_dict[key]["info"]
            info = [f'-   {info_dict[key]["emoji"]} __[{title}]({target})__\n\n',
                    '\t---\n\n',
                    f'\t{cover}\n\n',
                    f'\t{msg}\n\n',
                    f'\t[:octicons-arrow-right-24: Getting started]({target})\n\n',
                    ]
            info_head.extend(info)

        with open(pth_index_md, 'w', encoding='utf-8') as f:
            info_head.append('</div>')
            f.writelines(info_head)

        files = os.listdir(f'{self.path}/{c1_folder}')
        for file in files:
            if file in SKIP_FOLDERS:
                continue
            if os.path.isfile(f'{self.path}/{c1_folder}/{file}'):
                continue
            else:
                self._generate_index(f'{c1_folder}/{file}')

    def _check_toml(self, c1_folder):
        info_dict = {}
        c2_folders = os.listdir(f'{self.path}/{c1_folder}')
        if 'index.toml' in c2_folders:
            logger.info(f'{c1_folder}/index.toml ✔️')
            with open(f'{self.path}/{c1_folder}/index.toml', "rb") as f:
                info_dict = tomllib.load(f)
            for c2_folder in c2_folders:
                if c2_folder in SKIP_FOLDERS:
                    continue
                if c2_folder not in info_dict.keys():
                    info_dict[c2_folder] = self._get_toml_template(c2_folder)
                pth_file = f'{self.path}/{c1_folder}/{c2_folder}'
                info_dict[c2_folder].update({'path': pth_file})
                if os.path.isfile(pth_file):
                    if c2_folder.endswith('.ipynb'):
                        meta = ''
                    else:
                        meta = self._get_metadata(pth_file)
                    info_dict[c2_folder].update(meta)
                else:
                    self._check_toml(f'{c1_folder}/{c2_folder}')
        else:
            logger.info(f'{c1_folder}/index.toml 🎉🎉')
            for c2_folder in c2_folders:
                if c2_folder in SKIP_FOLDERS:
                    continue
                if c2_folder not in info_dict.keys():
                    info_dict[c2_folder] = self._get_toml_template(c2_folder)
                pth_file = f'{self.path}/{c1_folder}/{c2_folder}'
                info_dict[c2_folder].update({'path': pth_file})
                if os.path.isfile(pth_file):
                    if c2_folder.endswith('.ipynb'):
                        meta = ''
                    else:
                        meta = self._get_metadata(pth_file)
                    info_dict[c2_folder].update(meta)
                else:
                    self._check_toml(f'{c1_folder}/{c2_folder}')
        with open(f'{self.path}/{c1_folder}/index.toml', "w", encoding='utf-8') as f:
            toml.dump(info_dict, f)

    def run(self):
        folders = self._get_folders()
        for c1_folder in folders:
            if c1_folder in SKIP_FOLDERS:
                continue
            self._check_toml(c1_folder)
            self._generate_index(c1_folder)


if __name__ == '__main__':
    pth_docs = '../docs'
    auto_index = AutoIndex(pth_docs)
    auto_index.run()