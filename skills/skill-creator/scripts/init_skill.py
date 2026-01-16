#!/usr/bin/env python3
"""
=============================================================================
Skill 初始化器 - 从模板创建新的 Skill（技能）

这个脚本的主要功能是：
1. 在指定路径下创建一个新的 skill 目录
2. 生成标准的 SKILL.md 文件（技能的主要描述文件）
3. 创建示例资源目录结构（scripts/, references/, assets/）
=============================================================================

使用方法:
    init_skill.py <skill-name> --path <path>

示例:
    init_skill.py my-new-skill --path skills/public     # 创建公开技能
    init_skill.py my-api-helper --path skills/private   # 创建私有技能
    init_skill.py custom-skill --path /custom/location  # 自定义位置
"""

# ============================================================================
# 导入必要的模块
# ============================================================================
import sys                    # 系统模块，用于处理命令行参数和退出状态
from pathlib import Path      # 路径处理模块，提供面向对象的路径操作


# ============================================================================
# SKILL.md 模板
# 这是创建新技能时生成的主文件模板
# 包含 YAML frontmatter（前置元数据）和 Markdown 内容
# ============================================================================
SKILL_TEMPLATE = """---
name: {skill_name}
description: [TODO: Complete and informative explanation of what the skill does and when to use it. Include WHEN to use this skill - specific scenarios, file types, or tasks that trigger it.]
---

# {skill_title}

## Overview

[TODO: 1-2 sentences explaining what this skill enables]

## Structuring This Skill

[TODO: Choose the structure that best fits this skill's purpose. Common patterns:

**1. Workflow-Based** (best for sequential processes)
- Works well when there are clear step-by-step procedures
- Example: DOCX skill with "Workflow Decision Tree" → "Reading" → "Creating" → "Editing"
- Structure: ## Overview → ## Workflow Decision Tree → ## Step 1 → ## Step 2...

**2. Task-Based** (best for tool collections)
- Works well when the skill offers different operations/capabilities
- Example: PDF skill with "Quick Start" → "Merge PDFs" → "Split PDFs" → "Extract Text"
- Structure: ## Overview → ## Quick Start → ## Task Category 1 → ## Task Category 2...

**3. Reference/Guidelines** (best for standards or specifications)
- Works well for brand guidelines, coding standards, or requirements
- Example: Brand styling with "Brand Guidelines" → "Colors" → "Typography" → "Features"
- Structure: ## Overview → ## Guidelines → ## Specifications → ## Usage...

**4. Capabilities-Based** (best for integrated systems)
- Works well when the skill provides multiple interrelated features
- Example: Product Management with "Core Capabilities" → numbered capability list
- Structure: ## Overview → ## Core Capabilities → ### 1. Feature → ### 2. Feature...

Patterns can be mixed and matched as needed. Most skills combine patterns (e.g., start with task-based, add workflow for complex operations).

Delete this entire "Structuring This Skill" section when done - it's just guidance.]

## [TODO: Replace with the first main section based on chosen structure]

[TODO: Add content here. See examples in existing skills:
- Code samples for technical skills
- Decision trees for complex workflows
- Concrete examples with realistic user requests
- References to scripts/templates/references as needed]

## Resources

This skill includes example resource directories that demonstrate how to organize different types of bundled resources:

### scripts/
Executable code (Python/Bash/etc.) that can be run directly to perform specific operations.

**Examples from other skills:**
- PDF skill: `fill_fillable_fields.py`, `extract_form_field_info.py` - utilities for PDF manipulation
- DOCX skill: `document.py`, `utilities.py` - Python modules for document processing

**Appropriate for:** Python scripts, shell scripts, or any executable code that performs automation, data processing, or specific operations.

**Note:** Scripts may be executed without loading into context, but can still be read by Claude for patching or environment adjustments.

### references/
Documentation and reference material intended to be loaded into context to inform Claude's process and thinking.

**Examples from other skills:**
- Product management: `communication.md`, `context_building.md` - detailed workflow guides
- BigQuery: API reference documentation and query examples
- Finance: Schema documentation, company policies

**Appropriate for:** In-depth documentation, API references, database schemas, comprehensive guides, or any detailed information that Claude should reference while working.

### assets/
Files not intended to be loaded into context, but rather used within the output Claude produces.

**Examples from other skills:**
- Brand styling: PowerPoint template files (.pptx), logo files
- Frontend builder: HTML/React boilerplate project directories
- Typography: Font files (.ttf, .woff2)

**Appropriate for:** Templates, boilerplate code, document templates, images, icons, fonts, or any files meant to be copied or used in the final output.

---

**Any unneeded directories can be deleted.** Not every skill requires all three types of resources.
"""

# ============================================================================
# 示例脚本模板
# 当创建新技能时，会在 scripts/ 目录下生成这个示例 Python 脚本
# 这只是一个占位符，用户需要替换为实际的脚本逻辑
# ============================================================================
EXAMPLE_SCRIPT = '''#!/usr/bin/env python3
"""
Example helper script for {skill_name}

This is a placeholder script that can be executed directly.
Replace with actual implementation or delete if not needed.

Example real scripts from other skills:
- pdf/scripts/fill_fillable_fields.py - Fills PDF form fields
- pdf/scripts/convert_pdf_to_images.py - Converts PDF pages to images
"""

def main():
    print("This is an example script for {skill_name}")
    # TODO: Add actual script logic here
    # This could be data processing, file conversion, API calls, etc.

if __name__ == "__main__":
    main()
'''

# ============================================================================
# 示例参考文档模板
# 当创建新技能时，会在 references/ 目录下生成这个示例参考文档
# 用于存放详细的 API 文档、工作流指南等
# ============================================================================
EXAMPLE_REFERENCE = """# Reference Documentation for {skill_title}

This is a placeholder for detailed reference documentation.
Replace with actual reference content or delete if not needed.

Example real reference docs from other skills:
- product-management/references/communication.md - Comprehensive guide for status updates
- product-management/references/context_building.md - Deep-dive on gathering context
- bigquery/references/ - API references and query examples

## When Reference Docs Are Useful

Reference docs are ideal for:
- Comprehensive API documentation
- Detailed workflow guides
- Complex multi-step processes
- Information too lengthy for main SKILL.md
- Content that's only needed for specific use cases

## Structure Suggestions

### API Reference Example
- Overview
- Authentication
- Endpoints with examples
- Error codes
- Rate limits

### Workflow Guide Example
- Prerequisites
- Step-by-step instructions
- Common patterns
- Troubleshooting
- Best practices
"""

# ============================================================================
# 示例资源文件模板
# 当创建新技能时，会在 assets/ 目录下生成这个示例资源文件
# assets 目录用于存放模板、图片、字体等不需要加载到上下文的文件
# ============================================================================
EXAMPLE_ASSET = """# Example Asset File

This placeholder represents where asset files would be stored.
Replace with actual asset files (templates, images, fonts, etc.) or delete if not needed.

Asset files are NOT intended to be loaded into context, but rather used within
the output Claude produces.

Example asset files from other skills:
- Brand guidelines: logo.png, slides_template.pptx
- Frontend builder: hello-world/ directory with HTML/React boilerplate
- Typography: custom-font.ttf, font-family.woff2
- Data: sample_data.csv, test_dataset.json

## Common Asset Types

- Templates: .pptx, .docx, boilerplate directories
- Images: .png, .jpg, .svg, .gif
- Fonts: .ttf, .otf, .woff, .woff2
- Boilerplate code: Project directories, starter files
- Icons: .ico, .svg
- Data files: .csv, .json, .xml, .yaml

Note: This is a text placeholder. Actual assets can be any file type.
"""


# ============================================================================
# 辅助函数
# ============================================================================

def title_case_skill_name(skill_name):
    """
    将连字符分隔的技能名称转换为标题格式（Title Case）
    
    例如:
        'my-new-skill' -> 'My New Skill'
        'api-helper' -> 'Api Helper'
    
    参数:
        skill_name: 连字符分隔的技能名称（如 'my-skill'）
    
    返回:
        str: 转换后的标题格式名称
    """
    return ' '.join(word.capitalize() for word in skill_name.split('-'))


# ============================================================================
# 核心功能函数
# ============================================================================

def init_skill(skill_name, path):
    """
    初始化一个新的技能目录，包含模板化的 SKILL.md 文件和示例资源。
    
    这个函数执行以下步骤:
    1. 在指定路径下创建技能目录
    2. 生成 SKILL.md 主文件（从模板填充）
    3. 创建 scripts/ 目录并添加示例脚本
    4. 创建 references/ 目录并添加示例参考文档
    5. 创建 assets/ 目录并添加示例资源文件

    参数:
        skill_name: 技能名称（应为连字符格式，如 'my-skill'）
        path: 应创建技能目录的父路径

    返回:
        Path: 成功创建时返回技能目录的路径
        None: 发生错误时返回 None
    """
    # --------------------------------------------------------------------------
    # 步骤 1: 确定技能目录的完整路径
    # Path(path).resolve() 将相对路径转换为绝对路径
    # --------------------------------------------------------------------------
    skill_dir = Path(path).resolve() / skill_name

    # --------------------------------------------------------------------------
    # 步骤 2: 检查目录是否已存在（避免覆盖已有技能）
    # --------------------------------------------------------------------------
    if skill_dir.exists():
        print(f"❌ Error: Skill directory already exists: {skill_dir}")
        return None

    # --------------------------------------------------------------------------
    # 步骤 3: 创建技能目录
    # parents=True: 如果父目录不存在，也一并创建
    # exist_ok=False: 如果目录已存在则抛出异常
    # --------------------------------------------------------------------------
    try:
        skill_dir.mkdir(parents=True, exist_ok=False)
        print(f"✅ Created skill directory: {skill_dir}")
    except Exception as e:
        print(f"❌ Error creating directory: {e}")
        return None

    # --------------------------------------------------------------------------
    # 步骤 4: 创建 SKILL.md 主文件
    # 使用模板并填充技能名称和标题
    # --------------------------------------------------------------------------
    skill_title = title_case_skill_name(skill_name)  # 转换为标题格式
    skill_content = SKILL_TEMPLATE.format(
        skill_name=skill_name,      # 填充技能名称（连字符格式）
        skill_title=skill_title     # 填充技能标题（Title Case 格式）
    )

    skill_md_path = skill_dir / 'SKILL.md'
    try:
        skill_md_path.write_text(skill_content)  # 写入文件
        print("✅ Created SKILL.md")
    except Exception as e:
        print(f"❌ Error creating SKILL.md: {e}")
        return None

    # --------------------------------------------------------------------------
    # 步骤 5: 创建资源目录和示例文件
    # --------------------------------------------------------------------------
    try:
        # ----- 创建 scripts/ 目录 -----
        # 用于存放可执行的脚本（Python、Bash 等）
        scripts_dir = skill_dir / 'scripts'
        scripts_dir.mkdir(exist_ok=True)
        
        # 创建示例脚本
        example_script = scripts_dir / 'example.py'
        example_script.write_text(EXAMPLE_SCRIPT.format(skill_name=skill_name))
        example_script.chmod(0o755)  # 设置可执行权限 (rwxr-xr-x)
        print("✅ Created scripts/example.py")

        # ----- 创建 references/ 目录 -----
        # 用于存放参考文档（加载到上下文中供 Claude 参考）
        references_dir = skill_dir / 'references'
        references_dir.mkdir(exist_ok=True)
        
        # 创建示例参考文档
        example_reference = references_dir / 'api_reference.md'
        example_reference.write_text(EXAMPLE_REFERENCE.format(skill_title=skill_title))
        print("✅ Created references/api_reference.md")

        # ----- 创建 assets/ 目录 -----
        # 用于存放资源文件（模板、图片、字体等，不加载到上下文）
        assets_dir = skill_dir / 'assets'
        assets_dir.mkdir(exist_ok=True)
        
        # 创建示例资源文件
        example_asset = assets_dir / 'example_asset.txt'
        example_asset.write_text(EXAMPLE_ASSET)
        print("✅ Created assets/example_asset.txt")
        
    except Exception as e:
        print(f"❌ Error creating resource directories: {e}")
        return None

    # --------------------------------------------------------------------------
    # 步骤 6: 打印后续步骤提示
    # --------------------------------------------------------------------------
    print(f"\n✅ Skill '{skill_name}' initialized successfully at {skill_dir}")
    print("\nNext steps:")
    print("1. Edit SKILL.md to complete the TODO items and update the description")
    print("2. Customize or delete the example files in scripts/, references/, and assets/")
    print("3. Run the validator when ready to check the skill structure")

    return skill_dir


# ============================================================================
# 主函数入口
# ============================================================================

def main():
    """
    脚本的主入口函数
    
    功能:
    1. 解析命令行参数
    2. 验证参数格式是否正确
    3. 调用 init_skill() 创建新技能
    4. 根据结果设置退出状态码
    """
    # --------------------------------------------------------------------------
    # 参数验证
    # 期望的命令格式: init_skill.py <skill-name> --path <path>
    # sys.argv[0] = 脚本名
    # sys.argv[1] = skill-name
    # sys.argv[2] = --path
    # sys.argv[3] = path
    # --------------------------------------------------------------------------
    if len(sys.argv) < 4 or sys.argv[2] != '--path':
        # 如果参数不足或格式不正确，显示使用帮助
        print("Usage: init_skill.py <skill-name> --path <path>")
        print("\nSkill name requirements:")
        print("  - Hyphen-case identifier (e.g., 'data-analyzer')")
        print("  - Lowercase letters, digits, and hyphens only")
        print("  - Max 40 characters")
        print("  - Must match directory name exactly")
        print("\nExamples:")
        print("  init_skill.py my-new-skill --path skills/public")
        print("  init_skill.py my-api-helper --path skills/private")
        print("  init_skill.py custom-skill --path /custom/location")
        sys.exit(1)  # 退出状态码 1 表示错误

    # --------------------------------------------------------------------------
    # 提取命令行参数
    # --------------------------------------------------------------------------
    skill_name = sys.argv[1]  # 获取技能名称
    path = sys.argv[3]        # 获取目标路径

    # 打印初始化信息
    print(f"🚀 Initializing skill: {skill_name}")
    print(f"   Location: {path}")
    print()

    # --------------------------------------------------------------------------
    # 执行初始化
    # --------------------------------------------------------------------------
    result = init_skill(skill_name, path)

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
