#!/usr/bin/env python3
"""
=============================================================================
Skill 打包器 - 将技能文件夹打包为可分发的 .skill 文件

这个脚本的主要功能是：
1. 验证技能目录结构是否正确
2. 将整个技能文件夹压缩打包为 .skill 文件（本质上是 ZIP 格式）
3. 支持指定输出目录

.skill 文件可以用于分发和共享技能
=============================================================================

使用方法:
    python utils/package_skill.py <path/to/skill-folder> [output-directory]

示例:
    python utils/package_skill.py skills/public/my-skill           # 打包到当前目录
    python utils/package_skill.py skills/public/my-skill ./dist    # 打包到 dist 目录
"""

# ============================================================================
# 导入必要的模块
# ============================================================================
import sys                             # 系统模块，用于处理命令行参数和退出状态
import zipfile                         # ZIP 压缩模块，用于创建 .skill 压缩包
from pathlib import Path               # 路径处理模块，提供面向对象的路径操作
from quick_validate import validate_skill  # 导入验证函数（来自同目录的 quick_validate.py）


# ============================================================================
# 核心功能函数
# ============================================================================

def package_skill(skill_path, output_dir=None):
    """
    将技能文件夹打包为 .skill 文件。
    
    打包流程:
    1. 验证技能文件夹是否存在且格式正确
    2. 检查 SKILL.md 是否存在
    3. 运行验证器确保技能符合规范
    4. 将所有文件压缩为 ZIP 格式的 .skill 文件

    参数:
        skill_path: 技能文件夹的路径
        output_dir: 可选，.skill 文件的输出目录（默认为当前工作目录）

    返回:
        Path: 成功时返回创建的 .skill 文件路径
        None: 发生错误时返回 None
    """
    # --------------------------------------------------------------------------
    # 步骤 1: 解析并验证技能文件夹路径
    # resolve() 将相对路径转换为绝对路径
    # --------------------------------------------------------------------------
    skill_path = Path(skill_path).resolve()

    # 检查技能文件夹是否存在
    if not skill_path.exists():
        print(f"❌ Error: Skill folder not found: {skill_path}")
        return None

    # 检查路径是否为目录（而非文件）
    if not skill_path.is_dir():
        print(f"❌ Error: Path is not a directory: {skill_path}")
        return None

    # --------------------------------------------------------------------------
    # 步骤 2: 检查 SKILL.md 是否存在
    # SKILL.md 是每个技能的核心文件，必须存在
    # --------------------------------------------------------------------------
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        print(f"❌ Error: SKILL.md not found in {skill_path}")
        return None

    # --------------------------------------------------------------------------
    # 步骤 3: 运行验证器
    # 在打包之前确保技能符合规范（名称格式、描述长度等）
    # --------------------------------------------------------------------------
    print("🔍 Validating skill...")
    valid, message = validate_skill(skill_path)  # 调用 quick_validate.py 中的验证函数
    if not valid:
        print(f"❌ Validation failed: {message}")
        print("   Please fix the validation errors before packaging.")
        return None
    print(f"✅ {message}\n")

    # --------------------------------------------------------------------------
    # 步骤 4: 确定输出位置
    # --------------------------------------------------------------------------
    skill_name = skill_path.name  # 获取技能文件夹名称（如 'my-skill'）
    
    if output_dir:
        # 如果指定了输出目录，使用该目录
        output_path = Path(output_dir).resolve()
        output_path.mkdir(parents=True, exist_ok=True)  # 如果不存在则创建
    else:
        # 默认使用当前工作目录
        output_path = Path.cwd()

    # 构造输出文件名：<skill-name>.skill
    skill_filename = output_path / f"{skill_name}.skill"

    # --------------------------------------------------------------------------
    # 步骤 5: 创建 .skill 文件（ZIP 格式）
    # --------------------------------------------------------------------------
    try:
        # 使用 ZIP_DEFLATED 压缩算法创建压缩包
        with zipfile.ZipFile(skill_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # 遍历技能目录下的所有文件
            # rglob('*') 递归匹配所有文件和子目录
            for file_path in skill_path.rglob('*'):
                if file_path.is_file():  # 只处理文件（跳过目录）
                    # 计算文件在 ZIP 中的相对路径
                    # 使用 skill_path.parent 作为基准，这样 ZIP 中会包含技能目录名
                    # 例如：my-skill/SKILL.md, my-skill/scripts/example.py
                    arcname = file_path.relative_to(skill_path.parent)
                    zipf.write(file_path, arcname)  # 将文件添加到 ZIP
                    print(f"  Added: {arcname}")  # 打印添加的文件

        print(f"\n✅ Successfully packaged skill to: {skill_filename}")
        return skill_filename

    except Exception as e:
        print(f"❌ Error creating .skill file: {e}")
        return None


# ============================================================================
# 主函数入口
# ============================================================================

def main():
    """
    脚本的主入口函数
    
    功能:
    1. 解析命令行参数
    2. 调用 package_skill() 进行打包
    3. 根据结果设置退出状态码
    """
    # --------------------------------------------------------------------------
    # 参数验证
    # 至少需要一个参数（技能文件夹路径）
    # --------------------------------------------------------------------------
    if len(sys.argv) < 2:
        print("Usage: python utils/package_skill.py <path/to/skill-folder> [output-directory]")
        print("\nExample:")
        print("  python utils/package_skill.py skills/public/my-skill")
        print("  python utils/package_skill.py skills/public/my-skill ./dist")
        sys.exit(1)  # 退出状态码 1 表示错误

    # --------------------------------------------------------------------------
    # 提取命令行参数
    # --------------------------------------------------------------------------
    skill_path = sys.argv[1]  # 获取技能文件夹路径
    # 如果提供了第二个参数，则作为输出目录
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None

    # 打印打包信息
    print(f"📦 Packaging skill: {skill_path}")
    if output_dir:
        print(f"   Output directory: {output_dir}")
    print()

    # --------------------------------------------------------------------------
    # 执行打包
    # --------------------------------------------------------------------------
    result = package_skill(skill_path, output_dir)

    # 根据结果设置退出状态码
    if result:
        sys.exit(0)  # 成功
    else:
        sys.exit(1)  # 失败


# ============================================================================
# 脚本入口点
# 当直接运行此脚本时（非作为模块导入），执行 main() 函数
# ============================================================================
if __name__ == "__main__":
    main()
