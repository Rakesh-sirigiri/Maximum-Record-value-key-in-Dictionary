dict = {'gfg' : {'Manjeet' : 5, 'Himani' : 10},
        'is' : {'Manjeet' : 8, 'Himani' : 9},
        'best' : {'Manjeet' : 10, 'Himani' : 15}}
print("The original dictionary is : " + str(dict))
key = 'Himani'
res = max(dict, key = lambda sub: dict[sub][key])
print("The required key is : " + str(res))
