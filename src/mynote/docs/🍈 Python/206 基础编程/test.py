"""
=========================================================================
@File Name: test.py
@Time: 2024/5/14 下午9:16
@Program IDE：PyCharm
@Create by Author: 一一风和橘
@Motto: "The trick, William Potter, is not minding that it hurts."
@Description:
- 
- 
=========================================================================
"""
from concurrent.futures import ThreadPoolExecutor


class Chick:
    def __init__(self):
        pass

    def __run(self):
        # 多线程逻辑
        print('Good at singing and dancing')

    def main(self):
        with ThreadPoolExecutor() as executor:
            executor.submit(self.__run)


class Ikun(Chick):
    def __init__(self):
        super().__init__()

    def __run(self):
        # 新的多线程逻辑
        print('Gene Knee Tie May')


class Chick2:
    def __init__(self):
        pass

    def _run(self):
        # 多线程逻辑
        print('Good at singing and dancing')

    def main(self):
        with ThreadPoolExecutor() as executor:
            executor.submit(self._run)


class Ikun2(Chick2):
    def __init__(self):
        super().__init__()

    def _run(self):
        # 新的多线程逻辑
        print('Gene Knee Tie May')


class Chick3:
    def __init__(self):
        pass

    def __run(self):
        # 多线程逻辑
        print('Good at singing and dancing')

    def main(self):
        with ThreadPoolExecutor() as executor:
            executor.submit(self.__run)


class Ikun3(Chick3):
    def __init__(self):
        super().__init__()

    def _Chick3__run(self):
        # 新的多线程逻辑
        print('Gene Knee Tie May')


if __name__ == '__main__':
    # 输出
    chick = Ikun()
    chick.main()
    # `Good at singing and dancing`

    chick = Ikun2()
    chick.main()
    # `Gene Knee Tie May`

    chick = Ikun3()
    chick.main()
    # `Gene Knee Tie May`