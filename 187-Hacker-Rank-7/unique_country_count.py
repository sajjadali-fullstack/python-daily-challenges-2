
N = int(input("Enter number of countries: "))
country = set()

for i in range(N):
    country_stamp = input("Enter country name: ")
    country.add(country_stamp)

print(len(country))


'''
5
India
Pakistan
India
Bangladesh
Nepal

'''

# Output
# 4
