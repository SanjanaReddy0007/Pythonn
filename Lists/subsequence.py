
string = input()
substring = input()

sub_index = 0
sub_len = len(substring)

for char in string:
    if(char == substring[sub_index]):
        sub_index += 1
        if(sub_index == sub_len):
            break

if sub_index == sub_len:
    print("YESS") 
else:
    print("NOO")


