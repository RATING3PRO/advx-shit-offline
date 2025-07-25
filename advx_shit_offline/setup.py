from setuptools import setup, find_packages
import os

# 读取README文件
def read_readme():
    try:
        # 尝试从当前目录读取
        with open("README.md", "r", encoding="utf-8") as fh:
            return fh.read()
    except FileNotFoundError:
        try:
            # 尝试从上级目录读取
            with open("../README.md", "r", encoding="utf-8") as fh:
                return fh.read()
        except FileNotFoundError:
            # 如果都找不到，返回默认描述
            return "一个用于随机输出AdventureX文案的Python包（离线版本）"

setup(
    name="advx-shit-offline",
    version="1.0.14",
    author="AdventureX",
    author_email="",
    description="一个用于随机输出AdventureX文案的Python包（离线版本）",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/RATING3PRO/advx-shit-offline",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
    ],
    python_requires=">=3.6",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.0",
            "black>=21.0",
            "flake8>=3.8",
        ],
    },
    include_package_data=True,
    package_data={
        "advx_shit_offline": ["*.md"],
    },
    keywords="adventurex, shit, random, text, offline",
    project_urls={
        "Bug Reports": "https://github.com/RATING3PRO/advx-shit-offline/issues",
        "Source": "https://github.com/RATING3PRO/advx-shit-offline",
        "Documentation": "https://github.com/RATING3PRO/advx-shit-offline#readme",
    },
) 