print('\nWelcome to bmi calculator')
weight = float(input('Enter your weight(kg) : '))
height = float(input('Enter your height(cm) : '))
# Main fuction to calculate bmi 
def bmi(weight , height):
    bmi = weight // (height/100)**2
    if bmi < 18.5:
        return '\nUnder weight'
    elif 18.5 <= bmi <= 24.9:
        return '\nNormal\n'
    elif 25 <= bmi <= 29.5:
        return '\nOver weight'
    elif 30 <= bmi <= 34.9:
        return '\nObesity ( Class 1 )'
    elif 35 <= bmi <= 39.9:
        return '\nObesity ( Class 2 )'
    elif bmi >= 40:
        return '\nExtreme obesity'
# Additional function to calculate how much lose or gain weight
def normal_weight(weight , height):
    bmi = weight // (height/100)**2
    if bmi >= 25 :
        normal = ((height/100)**2) * 24.9
        over_weight = weight - normal
        print('Your normal weight is %.0f kg'%normal)
        print('You have to lose %.0f kg\n'%over_weight)
    elif bmi < 18.5:
        normal = ((height/100)**2) * 18.5
        under_weight = normal - weight
        print('Your normal weight is %.0f kg'%normal)
        print('You have to gain %.0f kg\n'%under_weight)
print(bmi(weight,height))
normal_weight(weight,height)
