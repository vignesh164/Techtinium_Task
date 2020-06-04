from pprint import pprint 
from collections import Counter

# decleartion for to find combination
new_york_avl_unit=[10,20,40,80,160,320]
india_avl_unit=[10,40,80,160,320]
china_avl_unit=[10,20,80,160]

# decleartion for to find cost for combination
base_data={
    10:{'type':'large', 'unit':10, 'new_york_cost':120, 'india_cost':140, 'china_cost':110},
    20:{'type':'xlarge', 'unit':20, 'new_york_cost':230, 'china_cost':200},
    40:{'type':'2xlarge', 'unit':40, 'new_york_cost':450, 'india_cost':413,},
    80:{'type':'4xlarge', 'unit':80, 'new_york_cost':774, 'india_cost':890, 'china_cost':670},
    160:{'type':'8xlarge', 'unit':160, 'new_york_cost':1400, 'india_cost':1300, 'china_cost':1180},
    320:{'type':'10xlarge', 'unit':320, 'new_york_cost':2820, 'india_cost':2970,},
}

# this decleartion for help to identify region
cites = ['New York', 'India', 'China']
cites_key=['new_york_cost', 'india_cost', 'china_cost']


# Used for combination purpose. Main function to find a all possible combinations
def ways(total, coins):
    ways = [[Counter()]] + [[] for _ in range(total)]
    for coin in coins:
        for i in range(coin, total + 1):
            ways[i] += [way + Counter({coin: 1}) for way in ways[i-coin]]
    return ways[total]


def find_machines(target, hours):
    # checking for input type
    if type(target) != int:
        return 'Unit Must be in Integer'
    if type(hours) != int:
        return 'Hours is Must be in Integer'
    
    final_output = []
    for i, city_unit in enumerate([new_york_avl_unit, india_avl_unit, china_avl_unit]):
        current_city = cites[i]
        
        print('Please Wait checking '+ current_city + ' all combinations ...')
        
        # call to the main function. combination finder
        all_combinations = ways(target, city_unit)
        
        # if combination is available then find a short cost machines
        if all_combinations:
            combinations_cost=[]
            
            # finding a combination cost
            for combination in all_combinations:
                total = 0
                for items in combination.elements():
                    total+=base_data[items][cites_key[i]]
                combinations_cost.append(total)

            
            min_combination_cost = min(combinations_cost)
            min_combination_index = combinations_cost.index(min_combination_cost)

            short_cost_combination = all_combinations[min_combination_index].most_common()

            # form a output format
            machines = []
            for combination in  short_cost_combination:
                machines.append((base_data[combination[0]]['type'], combination[1]))

            final_output.append(
                {
                    'region': current_city,
                    'total_cost': '$'+ str(min_combination_cost * hours),
                    'machines': machines
                }
            )
        else:
            print(cites[i] + ' has No combination Found')
    
    return final_output


#find_machines(1150,1)


if __name__ == "__main__":
    while True:
        try:
            Capacity = int(input("Please Enter a Capacity(integer):"))
            Hours = int(input('Please Enter a Hours(integer):'))
            pprint(find_machines(Capacity, Hours))
            break
        except Exception as e:
            print('Please Enter correct Data - '+ str(e))
       
