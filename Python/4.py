'''
Список vlans это список VLANов, собранных со всех устройств сети, поэтому в списке есть повторяющиеся номера VLAN. 
Из списка нужно получить уникальный список VLAN-ов, отсортированный по возрастанию номеров. 
'''
vlans = [10, 20, 30, 1, 2, 100, 10, 30, 3, 4, 10]
sorted_vlans = list(sorted(set(vlans)))
print(sorted_vlans)