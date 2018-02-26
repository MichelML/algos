# Uses python3
import sys

def itemSorter(weightedValue):
    return weightedValue['value'] / weightedValue['weight'] 

def get_optimal_value(capacity, weights, values):
    value = 0.
    remainingCapacity = capacity

    weightAndValues = sorted(list(map(lambda weight: {'weight': weight[1], 'value': values[weight[0]]}, list(enumerate(weights)))), key=itemSorter, reverse=True)
    
    for weightAndValue in weightAndValues:
        if remainingCapacity >= weightAndValue['weight']:
            value += weightAndValue['value']
            remainingCapacity -= weightAndValue['weight']
        elif remainingCapacity != 0:
            remaindingPortion = (remainingCapacity / weightAndValue['weight']) 
            value += weightAndValue['value'] * remaindingPortion 
            remainingCapacity -= remaindingPortion * weightAndValue['weight'] 
    
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
