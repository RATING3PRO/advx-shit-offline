"""
advx-shit-offline - 一个用于随机输出AdventureX文案的Python包（离线版本）
"""

import random
import re
from typing import List
import os

class AdvXShitOffline:
    """AdventureX文案随机输出器（离线版本）"""
    
    def __init__(self, file_path: str = "Word.md"):
        self.file_path = file_path
        self._cache = None
        
    def _read_local_file(self) -> str:
        """读取本地文件"""
        try:
            if os.path.exists(self.file_path):
                with open(self.file_path, 'r', encoding='utf-8') as f:
                    return f.read()
            else:
                print(f"文件 {self.file_path} 不存在")
                return ""
        except Exception as e:
            print(f"读取文件失败: {e}")
            return ""
    
    def _parse_content(self, content: str) -> List[str]:
        """解析内容，提取文案"""
        if not content:
            return []
        
        # 按行分割内容
        lines = content.split('\n')
        texts = []
        current_text = ""
        
        for line in lines:
            line = line.strip()
            
            # 跳过空行
            if not line:
                if current_text:
                    texts.append(current_text.strip())
                    current_text = ""
                continue
            
            # 跳过纯URL行
            if line.startswith('http') or line.startswith('https'):
                continue
                
            # 跳过代码块标记
            if line.startswith('```'):
                continue
                
            # 跳过HTML标签
            if line.startswith('<') and line.endswith('>'):
                continue
                
            # 跳过纯数字或符号行
            if re.match(r'^[\d\s\-\*\.]+$', line):
                continue
                
            # 跳过过短的行（少于3个字符）
            if len(line) < 3:
                continue
                
            # 如果是新的一段文案，保存之前的
            if current_text and (line.startswith('#') or line.startswith('@') or line.startswith('using')):
                if current_text.strip():
                    texts.append(current_text.strip())
                current_text = line
            else:
                # 累积文案
                if current_text:
                    current_text += "\n" + line
                else:
                    current_text = line
        
        # 添加最后一段文案
        if current_text.strip():
            texts.append(current_text.strip())
        
        # 过滤和清理文案
        cleaned_texts = []
        for text in texts:
            # 跳过过短的文案
            if len(text) < 5:
                continue
                
            # 跳过纯代码块
            if text.startswith('#include') or text.startswith('using ') or text.startswith('namespace'):
                continue
                
            # 跳过纯URL
            if re.match(r'^https?://', text):
                continue
                
            # 清理文案
            cleaned_text = text.strip()
            if cleaned_text and cleaned_text not in cleaned_texts:
                cleaned_texts.append(cleaned_text)
        
        return cleaned_texts
    
    def _get_cached_content(self) -> List[str]:
        """获取缓存的内容"""
        if self._cache is None:
            content = self._read_local_file()
            self._cache = self._parse_content(content)
        
        return self._cache
    
    @property
    def random(self) -> str:
        """获取随机文案"""
        texts = self._get_cached_content()
        if not texts:
            return "暂无可用文案"
        
        return random.choice(texts)
    
    def get_all(self) -> List[str]:
        """获取所有文案"""
        return self._get_cached_content()
    
    def refresh(self):
        """刷新缓存"""
        self._cache = None

# 创建全局实例
advx = AdvXShitOffline()

# 为了兼容性，也可以直接导入
__all__ = ['advx', 'AdvXShitOffline'] 