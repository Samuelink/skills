---
name: housing-asset-management
description: Generate property asset management reports and sales scripts for housing rental companies. Calculates service fees, commissions, and generates professional HTML reports for landlord face-to-face meetings. Use when the user mentions housing rental, asset management, landlord acquisition, property report, rent pricing, or service fee calculation.
---

# 房屋租赁资产管理 - 收房话术与报告生成

## 核心业务模型

### 服务定位
- 公司角色：房屋租赁资产管理服务商（非中介赚差价）
- 核心价值：稳定租金 + 专业管理 + 可信赖的服务者
- 收费模式：每月收取 **3天房租** 作为服务费，不赚租金差价

### 服务内容
| 项目 | 说明 |
|------|------|
| 免费保洁 | 入住前专业保洁，提前完成 |
| 智能门锁 | 免费安装，提升安全与便利 |
| 首月承诺 | 承诺首月租出，否则先付业主半月佣金 |
| 日常维护 | 按时维修维护，业主无需操心 |
| 租客管理 | 筛选优质租客，保障出租率 |

### 风险兜底机制
若首月未租出：
1. 门锁 → 送给业主（公司承担）
2. 保洁 → 送给业主（公司承担）
3. 半月租金 → 先行赔付给业主

### 费用计算公式
```
月租金 = 小区租赁均价（由系统/用户提供）
日租金 = 月租金 / 30
服务费 = 日租金 × 3（每月）
业主实收 = 月租金 - 服务费
```

**示例（北京均价 5000 元/月）：**
- 日租金：≈167 元
- 月服务费：≈500 元
- 业主月实收：≈4,500 元

---

## 工作流程

当用户需要生成收房报告或准备面访话术时，按以下步骤执行：

### Step 1: 收集房源信息

向用户收集以下必要信息：

```
必填信息：
- [ ] 业主姓名
- [ ] 小区名称
- [ ] 城市
- [ ] 房屋户型（如：两室一厅）
- [ ] 房屋面积（平方米）
- [ ] 楼层信息
- [ ] 小区近期租赁均价（月租金）
- [ ] 房屋当前状态（空置/在住/装修中）

选填信息：
- [ ] 装修情况（精装/简装/毛坯）
- [ ] 朝向
- [ ] 是否有电梯
- [ ] 特殊卖点（地铁近、学区等）
```

### Step 2: 计算费用

使用计算脚本生成费用明细：

```bash
python scripts/calculate.py --rent 5000 --city 北京
```

或在对话中直接计算：
- 月服务费 = 月租金 / 30 × 3
- 首月保障金 = 月租金 / 2（仅未租出时赔付）
- 年服务费总计 = 月服务费 × 12

### Step 3: 生成资产管理报告

基于收集的信息，使用 [report-template.html](report-template.html) 模板生成专业的 HTML 报告。

报告包含以下模块：
1. **封面** - 公司品牌 + 业主/房源信息
2. **市场分析** - 小区租赁均价、周边对比
3. **服务方案** - 完整服务内容清单
4. **费用明细** - 透明的费用计算表
5. **风险保障** - 首月承诺 + 兜底方案
6. **合作流程** - 签约到入住的时间线

### Step 4: 准备面访话术

根据房源具体情况，从 [sales-scripts.md](sales-scripts.md) 中选取并定制话术。

---

## 报告生成规范

1. 所有金额保留整数，使用千分位分隔符
2. 百分比保留一位小数
3. 报告日期使用生成当天日期
4. HTML 报告需可直接在浏览器打开并打印
5. 配色方案：专业蓝（#1a56db）+ 白底，体现信任感

---

## 补充资源

- 标准话术参考：[sales-scripts.md](sales-scripts.md)
- 报告 HTML 模板：[report-template.html](report-template.html)
- 费用计算工具：[scripts/calculate.py](scripts/calculate.py)
