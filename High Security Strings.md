## input - abc

a - 5
b - 6
c - 7

5+6+7 = 18

it is the strength of the password.

only lowercase woed
uske andar predetermined weights.

input

first line - a string containing password

second line - integet denoting the letter a

a - n+0 
b - n+1
c - n+2


z - n+26


## pseudo algorithm:

1.def string_password_weight(string,weight_a)
	1.1 alphalist =list('abcdefghijklmnopqrstuvwxyz')
	1.2 dic_weights = [weight_a+i for i in range(0,26)]
	1.3 my_dic_word_map = dict(zip(alphalist,dic_weight))
	
	1.4 sum_strength_pass = 0

	1.5 for i in string.lower():
	    1.6 sum_strenght_pass+=my_dic_word_map.get(i)
	
	1.7 return sum_strength_pass





# order breakdown of the number sequence

a = 5
b = 6
c = 7

u = 25

v= 0
w = 1
x = 2
y = 3
z = 4





a= 10
b= 11
c = 12
d=13
e=14
f=15
g=16
h=17
i=18
j=19
k=20
l=21
m=22
n=23
o=24
p=25
q=0
r=1


## correction to the num_list number generation:


my_num_list = []

my_sum = 0

for i in range(26):
    if (weight_a+i)<=25:
	my_num_list.append(weight_a+i)
    else:
	my_num_list.append(i+1)
