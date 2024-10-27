def display_main_menu():
    print("Enter some numbers separated by commas(e.g. 5, 67, 32)")

def calc_average(num_list):
    avg=sum(num_list)/len(num_list)
    print(avg)

def get_user_input():
    user_input = input("Enter Numbers : ")
    string_list = user_input.split(",")
    list = []
    for float_list in string_list:
        list.append(int(float_list.strip()))
    print(list)
    return list
    
def find_min_max(num_list):
    print("Maximum : "+ str(max(num_list)))
    print("Minimum : "+ str(min(num_list)))

def sort_temperature(num_list):
    print("Sort_temperature :"+ str(sorted(num_list)))

def calc_median_temperature(num_list):
    ordered_list=sorted(num_list)
    n=len(num_list)
    if (n%2)==1:
        median_term=(n+1)//2
        median=ordered_list[median_term-1]
        print("Median Temperature :"+ str(median))
    else:
        median_term=((n/2)+((n/2)+1))//2
        median=ordered_list[median_term-1]
        print("Median Temperature :"+ str(median))

display_main_menu()
num_list=get_user_input()
print(type(num_list))
calc_average(num_list)
find_min_max(num_list)
sort_temperature(num_list)
ordered_list=sorted(num_list)
calc_median_temperature(num_list)
