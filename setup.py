from setuptools import setup

setup(
    app=['UIMain.py'],  # 主要应用程序脚本
    data_files=[('WorkSpace', ['WorkSpace/*'])],  # 数据文件
    options={
        'argv_emulation': True,  # 允许通过命令行参数传递给应用程序
        'packages': []  # 需要打包的Python包
    },
    setup_requires=['py2app'],  # 指定需要py2app来进行打包
)