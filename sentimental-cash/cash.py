from cs50 import get_float


while True:
   n = get_float("Change Owed: ")
   


denominations = {
    'quater': {'value': 0.25, 'count' : 0},
    'dimes': {'value' : 0.10, 'count' : 0},
    'nickel': {'value' : 0.05, 'count' : 0},
    'penny': {'value' : 0.01, 'count' : 0},
}


for coin in denominations:
    value = denominations[coin]['value']
    while change > value:
        change -= value
        denominations[coin['count'] += 1

for coin in denominations.items
