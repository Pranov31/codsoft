import random
lower_case="a b c d e f g h i j k l m n o p q r s t u v w x y z "
numeric=[0,1,2,3,4,5,6,7,8,9]
symbol="@ # $ % ^ & * _ < > ? "
upper_case="A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
combined_list=lower_case.split()+upper_case.split()+numeric+symbol.split()
length=int(input("enter a length of the password: "))
temp_password=""

while length>0:
    temp_password+=str(random.choice(combined_list))
    length-=1
print("your generated password is:",temp_password)






