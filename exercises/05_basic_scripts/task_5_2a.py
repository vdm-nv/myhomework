#!/usr/bin/env python3

# Задание 5.2a
# Всё, как в задании 5.2, но, если пользователь ввел адрес хоста, а не адрес сети,
# надо преобразовать адрес хоста в адрес сети и вывести адрес сети и маску, как в задании 5.2.
# Пример адреса сети (все биты хостовой части равны нулю):
#    * 10.0.1.0/24
#    * 190.1.0.0/16
# Пример адреса хоста:
#    * 10.0.1.1/24 - хост из сети 10.0.1.0/24
#    * 10.0.5.1/30 - хост из сети 10.0.5.0/30
# 
# Если пользователь ввел адрес 10.0.1.1/24,
# вывод должен быть таким:
#
#  Network:
#  10        0         1         0
#  00001010  00000000  00000001  00000000
#
#  Mask:
#    /24

netw = input('Введите адрес IP-сети:')
mask = input('Введите маску сети:')

add = netw.split('.')
mas = mask.split()

ip_temp = '''
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''

print('\n' + '-' * 30)
print('\n' + 'Network:' + ip_temp.format(int(add[0]),int(add[1]),int(add[2]),int(0)))
print('\n' + 'Mask:'+ '\n'+ mask)# + ip_temp.format(int(add[0]),int(add[1]),int(add[2]),int(add[3])))
print('\n' + '-' * 30)

