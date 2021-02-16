def to_jaden_case(string):
    list = string.split(' ')
#     print(list)
    output_list = []
    for word in list:
#         print(word)
        output_list.append(word.capitalize())
#         print(output_list)
    output = " ".join(output_list)    
    return output

print(to_jaden_case("hello how are you today"))