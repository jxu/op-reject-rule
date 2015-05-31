coins = (1, 2, 5, 10, 20, 50, 100, 200)

def f(coins, way, current_sum):
    if current_sum >= 200: return (current_sum == 200)
 
    s = 0
    for coin in coins:
        if way == [] or coin <= way[-1]:
            s += f(coins, way + [coin], current_sum + coin)
            
    return s

print(f(coins, [], 0))
