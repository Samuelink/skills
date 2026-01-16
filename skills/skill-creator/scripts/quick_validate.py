#!/usr/bin/env python3
"""
=============================================================================
技能快速验证器 - 验证技能目录结构和 SKILL.md 格式是否符合规范

这个脚本的主要功能是：
1. 检查 SKILL.md 文件是否存在
2. 验证 YAML frontmatter（前置元数据）格式
3. 验证必填字段（name, description）
4. 验证命名规范和字段长度限制
=============================================================================

使用方法:
    python quick_validate.py <skill_directory>

示例:
    python quick_validate.py skills/public/my-skill

退出码:
    0 - 验证通过
    1 - 验证失败
"""

# ============================================================================
# 导入必要的模块
# ============================================================================
import sys                    # 系统模块，用于处理命令行参数和退出状态
import os                     # 操作系统接口（此文件中未直接使用，可能为兼容性保留）
import re                     # 正则表达式模块，用于格式验证
import yaml                   # YAML 解析模块，用于解析 frontmatter
from pathlib import Path      # 路径处理模块，提供面向对象的路径操作


# ============================================================================
# 核心验证函数
# ============================================================================

def validate_skill(skill_path):
    """
    对技能进行基本验证
    
    验证内容包括:
    1. SKILL.md 文件是否存在
    2. YAML frontmatter 格式是否正确
    3. 必填字段 name 和 description 是否存在
    4. name 是否符合命名规范（连字符格式）
    5. description 是否符合长度和字符限制

    参数:
        skill_path: 技能目录的路径

    返回:
        tuple: (is_valid: bool, message: str)
            - is_valid: True 表示验证通过，False 表示验证失败
            - message: 验证结果消息（成功或错误原因）
    """
    # 将路径转换为 Path 对象
    skill_path = Path(skill_path)

    # ==========================================================================
    # 检查 1: SKILL.md 文件是否存在
    # ==========================================================================
    skill_md = skill_path / 'SKILL.md'
    if not skill_md.exists():
        return False, "SKILL.md not found"

    # ==========================================================================
    # 检查 2: 读取文件内容并验证 frontmatter 存在
    # frontmatter 是文件开头由 --- 包围的 YAML 块
    # ==========================================================================
    content = skill_md.read_text()
    
    # frontmatter 必须以 --- 开头
    if not content.startswith('---'):
        return False, "No YAML frontmatter found"

    # ==========================================================================
    # 检查 3: 提取 frontmatter 内容
    # 使用正则表达式匹配 --- 之间的内容
    # 格式: ---\n<yaml内容>\n---
    # ==========================================================================
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not match:
        return False, "Invalid frontmatter format"

    frontmatter_text = match.group(1)  # 提取 YAML 内容

    # ==========================================================================
    # 检查 4: 解析 YAML frontmatter
    # ==========================================================================
    try:
        frontmatter = yaml.safe_load(frontmatter_text)  # 安全解析 YAML
        # 确保解析结果是字典类型
        if not isinstance(frontmatter, dict):
            return False, "Frontmatter must be a YAML dictionary"
    except yaml.YAMLError as e:
        return False, f"Invalid YAML in frontmatter: {e}"

    # ==========================================================================
    # 检查 5: 验证属性是否在允许列表中
    # 只允许以下属性：name, description, license, allowed-tools, metadata
    # ==========================================================================
    ALLOWED_PROPERTIES = {'name', 'description', 'license', 'allowed-tools', 'metadata'}

    # 检查是否有未知的属性
    unexpected_keys = set(frontmatter.keys()) - ALLOWED_PROPERTIES
    if unexpected_keys:
        return False, (
            f"Unexpected key(s) in SKILL.md frontmatter: {', '.join(sorted(unexpected_keys))}. "
            f"Allowed properties are: {', '.join(sorted(ALLOWED_PROPERTIES))}"
        )

    # ==========================================================================
    # 检查 6: 验证必填字段
    # name 和 description 是必须存在的字段
    # ==========================================================================
    if 'name' not in frontmatter:
        return False, "Missing 'name' in frontmatter"
    if 'description' not in frontmatter:
        return False, "Missing 'description' in frontmatter"

    # ==========================================================================
    # 检查 7: 验证 name 字段
    # ==========================================================================
    name = frontmatter.get('name', '')
    
    # name 必须是字符串类型
    if not isinstance(name, str):
        return False, f"Name must be a string, got {type(name).__name__}"
    
    name = name.strip()  # 去除首尾空白
    
    if name:
        # ----- 验证命名规范 -----
        # name 必须是连字符格式（hyphen-case）：只能包含小写字母、数字和连字符
        if not re.match(r'^[a-z0-9-]+$', name):
            return False, f"Name '{name}' should be hyphen-case (lowercase letters, digits, and hyphens only)"
        
        # name 不能以连字符开头或结尾，也不能包含连续的连字符
        if name.startswith('-') or name.endswith('-') or '--' in name:
            return False, f"Name '{name}' cannot start/end with hyphen or contain consecutive hyphens"
        
        # ----- 验证长度限制 -----
        # name 最多 64 个字符（根据规范）
        if len(name) > 64:
            return False, f"Name is too long ({len(name)} characters). Maximum is 64 characters."

    # ==========================================================================
    # 检查 8: 验证 description 字段
    # ==========================================================================
    description = frontmatter.get('description', '')
    
    # description 必须是字符串类型
    if not isinstance(description, str):
        return False, f"Description must be a string, got {type(description).__name__}"
    
    description = description.strip()  # 去除首尾空白
    
    if description:
        # ----- 检查非法字符 -----
        # description 不能包含尖括号（< 或 >）
        if '<' in description or '>' in description:
            return False, "Description cannot contain angle brackets (< or >)"
        
        # ----- 验证长度限制 -----
        # description 最多 1024 个字符（根据规范）
        if len(description) > 1024:
            return False, f"Description is too long ({len(description)} characters). Maximum is 1024 characters."

    # ==========================================================================
    # 所有检查通过
    # ==========================================================================
    return True, "Skill is valid!"


# ============================================================================
# 脚本入口点
# ============================================================================
if __name__ == "__main__":
    """
    当直接运行此脚本时执行
    
    功能:
    1. 解析命令行参数（期望一个技能目录路径）
    2. 调用 validate_skill() 进行验证
    3. 打印验证结果
    4. 根据验证结果设置退出状态码
    """
    # 检查参数数量
    if len(sys.argv) != 2:
        print("Usage: python quick_validate.py <skill_directory>")
        sys.exit(1)
    
    # 执行验证
    valid, message = validate_skill(sys.argv[1])
    
    # 打印结果
    print(message)
    
    # 设置退出状态码：0 表示成功，1 表示失败
    sys.exit(0 if valid else 1)