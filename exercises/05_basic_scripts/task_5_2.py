#!/usr/bin/env python3

# Задание 5.2
#
# Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24
# Затем вывести информацию о сети и маске в таком формате:
#    Network:
#    10        1         1         0
#    00001010  00000001  00000001  00000000
#
#    Mask:
#    /24
#    255       255       255       0
#    11111111  11111111  11111111  00000000
# Проверить работу скрипта на разных комбинациях сеть/маска.

netw = input('Введите адрес IP-сети:')
mask = input('Введите маску сети:')

add = netw.split('.')
mas = mask.split()

ip_temp = '''
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''

print('\n' + '-' * 30)
print('\n' + 'Network:' + ip_temp.format(int(add[0]),int(add[1]),int(add[2]),int(add[3])))
print('\n' + 'Mask:'+ '\n'+ mask)# + ip_temp.format(int(add[0]),int(add[1]),int(add[2]),int(add[3])))
print('\n' + '-' * 30)
