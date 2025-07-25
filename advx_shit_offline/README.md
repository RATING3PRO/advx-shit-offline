# advx-shit-offline

一个用于随机输出AdventureX文案的Python包（离线版本）

## 🚀 快速开始

### 安装

```bash
pip install advx-shit-offline
```

### 使用

```python
from advx_shit_offline import advx
print(advx.random)
```

## 📦 功能特性

- ✅ **离线使用** - 无需网络连接
- ✅ **智能解析** - 自动提取和过滤文案
- ✅ **随机输出** - 从165条文案中随机选择
- ✅ **缓存机制** - 提高性能
- ✅ **完整文案** - 保证多行文案的完整性
- ✅ **自定义路径** - 支持自定义文件路径

## 📖 详细用法

### 基本用法

```python
from advx_shit_offline import advx

# 随机输出一条文案
print(advx.random)
```

### 获取所有文案

```python
from advx_shit_offline import advx

# 获取所有文案
all_texts = advx.get_all()
print(f"总共有 {len(all_texts)} 条文案")

# 显示前5条文案
for i, text in enumerate(all_texts[:5], 1):
    print(f"{i}. {text}")
```

### 自定义文件路径

```python
from advx_shit_offline import AdvXShitOffline

# 使用自定义文件
custom_advx = AdvXShitOffline("your_file.md")
print(custom_advx.random)
```

### 刷新缓存

```python
from advx_shit_offline import advx

# 刷新缓存
advx.refresh()
print(advx.random)
```

## 🎯 示例输出

```
是谁杀死了找💩比赛
原来是可以自行移动的 AI 马桶
再也不用到处找厕所了，更不会有溢出风险
```

## 📁 项目结构

```
advx-shit-offline/
├── advx_shit_offline/
│   └── __init__.py          # 核心代码
├── setup.py                 # 安装配置
├── README.md               # 说明文档
├── LICENSE                 # 许可证
├── requirements.txt        # 依赖文件
└── MANIFEST.in            # 打包配置
```

## 🔧 开发

### 克隆仓库

```bash
git clone https://github.com/RATING3PRO/advx-shit-offline.git
cd advx-shit-offline
```

### 安装开发依赖

```bash
cd advx_shit_offline
pip install -e .[dev]
```

### 构建包

```bash
python setup.py sdist bdist_wheel
```

## 📦 发布

### 手动发布

```bash
# 构建包
python setup.py sdist bdist_wheel

# 检查包
twine check dist/*

# 上传到PyPI
twine upload dist/*
```

### 自动发布

使用GitHub Actions自动发布：

```bash
# 创建标签
git tag v1.0.0
git push origin v1.0.0
```

## 🤝 贡献

欢迎提交Issue和Pull Request！

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](advx_shit_offline/LICENSE) 文件了解详情

## 🔗 相关链接

- [GitHub仓库](https://github.com/RATING3PRO/advx-shit-offline)
- [PyPI包](https://pypi.org/project/advx-shit-offline/)

## ⭐ 支持

如果这个项目对您有帮助，请给我们一个星标！

---

**注意**: 这个包是AdventureX活动的娱乐项目，仅供学习和娱乐使用。 
