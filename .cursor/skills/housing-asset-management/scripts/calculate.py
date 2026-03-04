"""
房屋资产管理费用计算工具
用途：根据月租金计算服务费、业主收入、首月保障金等关键数据
使用：python calculate.py --rent 5000 --city 北京
"""

import argparse
import json
import math


def calculate_fees(monthly_rent: int, city: str = "") -> dict:
    """根据月租金计算全部费用明细"""
    daily_rent = monthly_rent / 30                    # 日租金
    monthly_fee = math.ceil(daily_rent * 3)           # 月服务费（3天房租）
    owner_monthly = monthly_rent - monthly_fee        # 业主月实收
    yearly_fee = monthly_fee * 12                     # 年服务费
    yearly_income = owner_monthly * 12                # 业主年实收
    half_month = math.ceil(monthly_rent / 2)          # 首月保障赔付金

    return {
        "city": city,
        "monthly_rent": monthly_rent,
        "daily_rent": round(daily_rent, 1),
        "monthly_fee": monthly_fee,
        "owner_monthly_income": owner_monthly,
        "yearly_fee": yearly_fee,
        "owner_yearly_income": yearly_income,
        "half_month_guarantee": half_month,
        "fee_ratio": f"{monthly_fee / monthly_rent * 100:.1f}%",
    }


def format_report(data: dict) -> str:
    """格式化为可读的文本报告"""
    lines = [
        "=" * 40,
        "  房屋资产管理 · 费用计算明细",
        "=" * 40,
        "",
        f"  城市：{data['city']}" if data["city"] else "",
        f"  月租金：{data['monthly_rent']:,} 元",
        f"  日租金：{data['daily_rent']} 元",
        "",
        "  ── 费用明细 ──",
        f"  月服务费（3天房租）：{data['monthly_fee']:,} 元",
        f"  服务费占比：{data['fee_ratio']}",
        f"  业主月实收：{data['owner_monthly_income']:,} 元",
        "",
        "  ── 年度汇总 ──",
        f"  年服务费合计：{data['yearly_fee']:,} 元",
        f"  业主年实收：{data['owner_yearly_income']:,} 元",
        "",
        "  ── 首月保障 ──",
        f"  首月未租出赔付：{data['half_month_guarantee']:,} 元（半月租金）",
        f"  门锁 + 保洁：免费赠送（公司承担）",
        "",
        "=" * 40,
    ]
    return "\n".join(line for line in lines if line is not None)


def main():
    parser = argparse.ArgumentParser(description="房屋资产管理费用计算")
    parser.add_argument("--rent", type=int, required=True, help="月租金（元）")
    parser.add_argument("--city", type=str, default="", help="城市名称")
    parser.add_argument(
        "--json", action="store_true", dest="output_json", help="输出 JSON 格式"
    )
    args = parser.parse_args()

    data = calculate_fees(args.rent, args.city)

    if args.output_json:
        print(json.dumps(data, ensure_ascii=False, indent=2))
    else:
        print(format_report(data))


if __name__ == "__main__":
    main()
