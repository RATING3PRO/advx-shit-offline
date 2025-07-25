# advx-shit-offline

一个用于随机输出AdventureX文案的Python包（离线版本）

## 安装

```bash
pip install advx-shit-offline
```

## 使用方法

### 基本用法

```python
from advx_shit_offline import advx
print(advx.random)
```

### 获取所有文案

```python
from advx_shit_offline import advx
all_texts = advx.get_all()
print(f"总共有 {len(all_texts)} 条文案")
```

### 自定义文件路径

```python
from advx_shit_offline import AdvXShitOffline
custom_advx = AdvXShitOffline("your_file.md")
print(custom_advx.random)
```

## 功能特性

- ✅ 支持本地Word.md文件解析
- ✅ 智能文案提取和过滤
- ✅ 随机输出文案
- ✅ 缓存机制提高性能
- ✅ 支持自定义文件路径
- ✅ 完整的文案完整性保证
- ✅ 离线使用，无需网络连接

## 示例

```python
from advx_shit_offline import advx

# 随机输出一条文案
print(advx.random)

# 获取所有文案
all_texts = advx.get_all()
print(f"总共有 {len(all_texts)} 条文案")

# 刷新缓存
advx.refresh()
```

## 项目结构

```
advx-shit-offline/
├── advx_shit_offline/
│   └── __init__.py
├── setup.py
├── README.md
└── requirements.txt
```

## 开发

```bash
# 克隆仓库
git clone https://github.com/RATING3PRO/advx-shit-offline.git
cd advx-shit-offline

# 安装开发依赖
pip install -e .[dev]

# 运行测试
python test_offline.py
```

## 许可证

MIT License

## 贡献

欢迎提交Issue和Pull Request！

## 相关链接

- [GitHub仓库](https://github.com/RATING3PRO/advx-shit-offline)
- [PyPI包](https://pypi.org/project/advx-shit-offline/) 