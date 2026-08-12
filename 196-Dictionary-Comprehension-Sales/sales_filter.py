# WAP to create a new dictionary containing only those years in which sales were greater than
# 50,000, using dictionary comprehension.

sales_dict = {2000: 45000,
              2001: 35000,
              2002: 22000,
              2003: 22000,
              2004: 47000,
              2005: 38000,
              2006: 65000,
              2007: 75000}


year_sales = {year:sale for year, sale in sales_dict.items() if sale > 50000}
print(year_sales)  # {2006: 65000, 2007: 75000}