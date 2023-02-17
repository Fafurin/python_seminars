# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def dec_to_bin_oct_hex(var, system):
    origin_numb = var
    result = ''
    if var == 1:
        print(str(var) + " в 2-, 8-, 16-системах равно 1")
    else:
        while var > 0:
            result = str(var%system) + result
            var = int(var/system)

        print("Число " + str(origin_numb) + " в " + str(system) + "-системе = " + result)

dec_to_bin_oct_hex(1,2)

dec_to_bin_oct_hex(45,8)

dec_to_bin_oct_hex(45,16)