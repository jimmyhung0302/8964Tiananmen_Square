def compound_interest_calculator(monthly_investment, annual_rate, years):
    # 將年化報酬率轉換為月報酬率
    monthly_rate = annual_rate / 12
    total_months = years * 12
    
    total_amount = 0
    total_invested = 0

    # 逐月計算複利 (假設每個月初投入)
    for month in range(1, total_months + 1):
        total_invested += monthly_investment
        total_amount = (total_amount + monthly_investment) * (1 + monthly_rate)
        
    interest_earned = total_amount - total_invested
    
    print(f"=== {years} 年複利試算結果 ===")
    print(f"每月投入金額: {monthly_investment:,.0f} 元")
    print(f"年化報酬率: {annual_rate * 100:.1f}%")
    print("-" * 25)
    print(f"總投入本金: {total_invested:,.0f} 元")
    print(f"複利賺取利息: {interest_earned:,.0f} 元")
    print(f"期末總金額: {total_amount:,.0f} 元")
    
    return total_amount

# 設定你的條件：每月 5000，年化 6%，投資 18 年
final_value = compound_interest_calculator(monthly_investment=5000, annual_rate=0.06, years=18)