#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
advx-shit-offline 演示脚本
"""

from advx_shit_offline import advx

def main():
    print("🎉 AdventureX 文案随机输出器演示 🎉")
    print("=" * 60)
    
    # 获取所有文案
    all_texts = advx.get_all()
    print(f"📊 总共有 {len(all_texts)} 条文案")
    print()
    
    # 演示随机输出
    print("🎲 随机文案演示:")
    for i in range(5):
        random_text = advx.random
        print(f"第{i+1}次: {random_text}")
        print("-" * 60)
    
    print("\n✨ 演示完成！")

if __name__ == "__main__":
    main() 