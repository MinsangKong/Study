def solution(ings, menu, sell):
    answer = 0
    items = dict()
    margins = dict()
    for i in range(len(ings)):
        name, cost = ings[i].split()
        items[name] = int(cost)

    for i in range(len(menu)):
        name, ingredients, cost = menu[i].split()
        ingredientCost = 0
        for ingredient in ingredients:
            ingredientCost += items[ingredient]
        margins[name] = int(cost)-ingredientCost

    for i in range(len(sell)):
        name, count = sell[i].split()
        answer += margins[name]*int(count)
    return answer