salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

total_spend = 0
for _ in range(months):
    total_spend += spend
    spend *= (1 + increase)

money_capital = total_spend - (salary * months)

rounded_money_capital = int(money_capital // 1) + (1 if money_capital % 1 > 0 else 0)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов: ", rounded_money_capital)
