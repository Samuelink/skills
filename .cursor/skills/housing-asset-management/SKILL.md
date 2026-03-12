---
name: housing-asset-management
description: Generate customized property management proposal reports (HTML webpage) and matching sales scripts for landlords. Use when the user mentions property management proposals, landlord reports, rental management pitches, housing asset management, or needs to create materials for acquiring new property listings for 省心租.
---

# 房屋资产管理 - 业主提案报告生成器

为「省心租」生成定制化的业主提案报告（HTML 网页）和配套话术，用于收房时向业主展示服务方案。

## 触发场景

- 用户需要为某个业主生成提案报告
- 用户需要收房话术
- 用户提到业主报告、租房管理提案、资产管理方案

## 工作流程

### Step 1: 收集房源信息

向用户确认以下必填信息：

| 字段 | 说明 | 示例 |
|------|------|------|
| 业主姓名 | 报告抬头 | 张三 |
| 房屋地址 | 完整地址 | 杭州市西湖区XX路XX号XX室 |
| 户型 | 几室几厅 | 2室1厅1卫 |
| 面积 | 建筑面积(㎡) | 89㎡ |
| 建议月租金 | 市场评估租金 | ¥4,500/月 |
| 房屋现状 | 是否需要保洁/维修 | 需要保洁，无需维修 |

可选信息（有则更好）：
- 楼层/总楼层
- 装修情况（精装/简装/毛坯）
- 配套设施（家电家具清单）
- 周边配套（地铁、商圈等）

### Step 2: 计算费用明细

根据业务模型计算所有费用，详见 [business-model.md](business-model.md)。

核心公式：
- **服务费** = 月租金 ÷ 30 × 3（即3天租金/月）
- **保证金** = 月租金 × 0.5（半个月租金，签约时支付给业主）
- **业主实际月收入** = 月租金 - 服务费

### Step 3: 生成 HTML 报告

使用 [report-template.md](report-template.md) 中的模板生成单文件 HTML 报告。

报告要求：
- **纯 HTML/CSS/JS**，单文件，可直接浏览器打开
- **专业商务风**：深色调、沉稳大气
- **响应式设计**：手机和电脑都能看
- **包含打印样式**：方便打印纸质版
- 所有业主信息、费用明细、服务承诺都要体现

### Step 4: 生成配套话术

使用 [sales-script.md](sales-script.md) 中的模板生成话术。

话术要求：
- 与报告内容一一对应
- 口语化、自然、有说服力
- 按报告章节顺序组织
- 标注关键话术节点（如何回应常见疑虑）

### Step 5: 输出

将以下内容交付给用户：
1. HTML 报告文件
2. 配套话术文本

## 公司信息

| 项目 | 内容 |
|------|------|
| 公司名称 | 省心租 |
| 联系电话 | 138-8888-6688 |
| 服务理念 | 不赚差价，只收服务费；租不出去，分文不取 |

## 补充资源

- 业务模型与费用计算详情：[business-model.md](business-model.md)
- HTML 报告模板与样式规范：[report-template.md](report-template.md)
- 话术模板与应对策略：[sales-script.md](sales-script.md)
