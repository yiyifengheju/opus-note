"""
=========================================================================
@File Name: auto_index.py
@Time: 2024/9/10 22:16
@Program IDE：PyCharm
@Create by Author: 一一风和橘
@Motto: "The trick, William Potter, is not minding that it hurts."
@Description:
- 
- 
=========================================================================
"""
import os
import tomllib
import toml
from loguru import logger


def generate_toml(path):
    info_dict = {}
    folders = os.listdir(path)
    if 'info.toml' in folders:
        logger.warning('info.toml is already generated.')
        with open(os.path.join(path, 'info.toml'), "rb") as f:
            info_dict = tomllib.load(f)
        for folder in folders:
            if folder == 'info.toml':
                continue
            if folder == 'index.md':
                continue
            if folder not in info_dict.keys():
                info_dict[folder] = {'info': '', 'emoji': ''}
    else:
        for folder in folders:
            info_dict[folder] = {'info': '', 'emoji': ''}
    with open(os.path.join(path, 'info.toml'), "w", encoding='utf-8') as f:
        toml.dump(info_dict, f)


def generate_index(path):
    # path = r'C:\Users\Artmallo\PycharmProjects\opus-note\src\opus_note\docs\🎁 机器学习'
    with open(os.path.join(path, 'info.toml'), "rb") as f:
        info = tomllib.load(f)
    folders = os.listdir(path)
    tail = os.path.split(path)[-1]
    folder_index_list = ['---\n',
                         f'title: {tail}\n',
                         'comments: false\n',
                         '---\n',
                         '\n'
                         '<div class="grid cards index-info" markdown>\n\n']
    pth_folder_index = os.path.join(path, 'index.md')
    for folder in folders:
        pth = os.path.join(path, folder)
        # print(pth)
        if not os.path.isdir(pth):
            continue
        fa = info[folder]['emoji'] or folder.split(' ')[0]
        fo = folder.split(' ')[1]
        folder_info = [f'-   {fa} __{fo}__\n\n',
                       '\t---\n\n',
                       f'\t{info[folder]["info"]}\n\n',
                       f'\t[:octicons-arrow-right-24: Getting started](./{folder}/index.md)\n\n',
                       ]
        folder_index_list.extend(folder_info)
        files = os.listdir(pth)
        pth_index = os.path.join(path, folder, 'index.md')
        title_list = ['---\n',
                      f'title: {folder}\n',
                      'comments: true\n',
                      '---\n\n',
                      '<div class="grid cards" markdown>\n',
                      '\n']
        for file in files:
            ti = None
            if file == 'index.md':
                continue
            if file.endswith('.md') or file.endswith('.ipynb'):
                pth = os.path.join(path, folder, file)
                with open(pth, 'r', encoding='utf-8') as f:
                    contents = f.readlines()
                for line in contents:
                    if 'title' in line:
                        title = line.strip().split(': ')[-1]
                        fa = title.split(' ')[0]
                        ti = title.split(' ')[1]
                        tmp = f'- {fa} [__{ti}__](./{file})\n'
                        title_list.append(tmp)
                        break
                    if '# ' in line:
                        try:
                            title = line.strip().split('# ')[-1].split('"')[0].split('\\n')[0].strip()
                            fa = title.split(' ')[0]
                            ti = title.split(' ')[1]
                            tmp = f'- {fa} [__{ti}__](./{file})\n'
                            title_list.append(tmp)
                            break
                        except:
                            assert 0, pth
                logger.info(ti)
        title_list.append('\n')
        title_list.append('</div>')
        with open(pth_index, 'w', encoding='utf-8') as f:
            f.writelines(title_list)
    with open(pth_folder_index, 'w', encoding='utf-8') as f:
        folder_index_list.append('</div>')
        f.writelines(folder_index_list)


if __name__ == '__main__':
    folders = ['🎀 软件及配置',
               '🎁 信号处理',
               '🎁 机器学习',
               '🎈 Python',
               '🎈 其他编程',
               '🎈 前端',
               '🏅 我的脚本']
    path = f'../docs/{folders[5]}'
    generate_toml(path)
    generate_index(path)
