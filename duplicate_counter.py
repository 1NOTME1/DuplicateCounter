#ZLICZANIE DUPLIKATOW Z PLIKU
from collections import Counter

input_file = r"C:\Users\USER_NAME\Desktop\duble_python\dane.txt"
output_file = "output.txt"

with open(input_file, 'r') as file:
    data = file.read().splitlines()

# Zlicz wystąpienia danych
data_count = Counter(data)

# Wybierz dane, które występują tylko raz
unique_data = [d for d in data if data_count[d] == 1]

for d in unique_data:
    print(d)

with open(output_file, 'w') as file:
    for d in unique_data:
        file.write(d + '\n')
