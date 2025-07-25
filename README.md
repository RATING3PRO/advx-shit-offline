# advx-shit-offline

一个用于随机输出AdventureX-Shit文案的Python包（离线版本）

## 快速开始

### 安装

```bash
pip install advx-shit-offline
```

### 使用

```python
from advx_shit_offline import advx
print(advx.random)
```

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

## 示例输出(基本用法)

```
是谁杀死了找💩比赛
原来是可以自行移动的 AI 马桶
再也不用到处找厕所了，更不会有溢出风险
```

## 项目结构

```
advx-shit-offline/
├── advx_shit_offline/
│   └── __init__.py          
├── setup.py                 
├── README.md               
├── LICENSE                 
├── requirements.txt        
└── MANIFEST.in            
```

## 贡献

提交Issue和Pull Request

1. Fork 本仓库
2. 创建特性分支 (`git checkout -b feature/AmazingFeature`)
3. 提交更改 (`git commit -m 'Add some AmazingFeature'`)
4. 推送到分支 (`git push origin feature/AmazingFeature`)
5. 打开 Pull Request

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](advx_shit_offline/LICENSE) 文件了解详情

## 相关链接

- [GitHub仓库](https://github.com/RATING3PRO/advx-shit-offline)
- [PyPI包](https://pypi.org/project/advx-shit-offline/)

## 支持

发送邮件(xiesmail2000@gmail.com)

---

**注意**: 这个包是AdventureX黑客放轻松的娱乐项目，仅供学习和娱乐使用。 
