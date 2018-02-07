items = {
"dirt": {"weight": 4,"value": 0},
"computer": {"weight": 10, "value": 30},
"fork": {"weight": 5, "value": 1},
"problemSet": {"weight": 0, "value": -10}
}

results = {}

def metric1(item):
    for each in item:
        try:
            results[each] = item[each]["value"] / items[each]["weight"]
        except ZeroDivisionError:
            results[each] = "ZeroDivisionError"
    return results

print("Metric 1 result:\n" + str(metric1(items)))

def metric2(item):
    for each in item:
        results[each] = -(item[each]["weight"])
    return results

print("Metric 2 results:\n" + str(metric2(items)))
