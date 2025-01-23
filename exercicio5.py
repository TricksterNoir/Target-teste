def inverter_string(s):
    return ''.join([s[i] for i in range(len(s) - 1, -1, -1)])

string = input("Digite uma string para inverter: ")
print("String invertida:", inverter_string(string))