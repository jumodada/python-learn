
# def calc_bmi(**weight_and_height):
#     print(weight_and_height)
#     # result_dict = {"小李":234,"xiaowang":123} 
#     result_dict = {}
#     for key,value in weight_and_height.items():
#         weight = value[0]
#         height = value[1]
#         bmi = weight/(height*height)
#         result_dict[key]=bmi
#     return result_dict


# result = calc_bmi(xiaowang=[70,1.65],xiaoli=[72,1.7],xiaozhou=[75,1.75])
# print(result)

def calc_bmi(**weight_and_height):
    print(weight_and_height)
    # ([xiaoli,123],(xiaowang,3453))
    # [[xiaoli,123],[xiaowang,456]]
    result_list = []
    for key,value in weight_and_height.items():
        r = []
        weight = value[0]
        height = value[1]
        bmi = weight/(height*height)
        r.append(key)
        r.append(bmi)
        result_list.append(r)
    return result_list
    # return tuple(result_list)
result = calc_bmi(xiaowang=[70,1.65],xiaoli=[72,1.7],xiaozhou=[75,1.75])
print(result)
r1,r2,r3 = calc_bmi(xiaowang=[70,1.65],xiaoli=[72,1.7],xiaozhou=[75,1.75])
print(r1,r2,r3)
