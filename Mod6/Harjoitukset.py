# Funktion määrittely
"""
def do_something():
    print("Doing")
    print("something")
    return "Tässä on plautettava arvo, voi olla mikä vaan"

return_value = do_something()
print(return_value)

# Funktio jolla parametrit/argumentti

def combine_strings(string1, string2):
    combination = f"{string1}, {string2}"
    #print(combination)
    return combination

print(combine_strings("auto", "ajaa"))


combination = combine_strings("kuski", "jarruttaa")
combination = combine_strings(combination, "nopeasti")
print(combination)

# Yksinkertainen laskin, jolle voi antaa tasan 3 parametria, listat ja funktiot


# Funktio ottaa parametrina listan lukuja ja laskee ja palauttaa niiden summan

def calculate_sum(numbers):
    total_sum = 0
    for i in range(len(numbers)):
        total_sum = total_sum + numbers[i]
        numbers[i] = 0 # Nollataan listan käsiteltävä alkio ihan vaan huvikseen
    return total_sum

   # for num in numbers:
    #    total_sum = total_sum + num
    #return total_sum


nums = [3,4,5,10]
print(nums)
print(calculate_sum(nums)) #Menee kohtaan numbers
print(nums)
#print(calculate_sum([3, 4, 5]))
"""



def calculate_sum2(numbers):
    total_sum = 0
    for num in numbers:
        total_sum = total_sum + num
    return total_sum

print(calculate_sum2([2,3,8]))



def calculate_sum2(num1, num2, num3):
    total_sum = 0
    for num in numbers:
        total_sum = total_sum + num
    return total_sum

print(calculate_sum2(2, 3, 8))



def calculate_sum2(*numbers):
    total_sum = 0
    for num in numbers:
        total_sum = total_sum + num
    return total_sum

print(calculate_sum2(2, 3, 8))


# Extraa: Nimetyt parametrit ja oletusarvot
# Yksinkertainen laskin jolle voi antaa 2-3 parametria
def calculate2(number1, number2, calc_type="sum"):
    if calc_type == "sum":
        return number1 + number2
    elif calc_type == "division":
        return number1 / number2

print(calculate2(2.4,3.5))

print(calculate2(2.4,3.5, "division"))

print(calculate2(number2= 2.4, number1=3.5, calc_type="division"))
