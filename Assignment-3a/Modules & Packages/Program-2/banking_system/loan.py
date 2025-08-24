def calculate_emi(principal, annual_rate, years):
    # Convert annual rate to monthly
    monthly_rate = (annual_rate / 100) / 12
    months = years * 12

    # EMI formula
    emi = (principal * monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
    return round(emi, 2)
