laptops = ['dell', 'hp', 'lenovo', 'mac']
print(laptops[0])
print(laptops.index('hp')) #gives indexing number of given item
laptops.append('sony') #adds an item to the end of the list
print(laptops)
laptops.insert(2, 'microsoft') # adds an item at the specified index
print(laptops)
laptops.remove('microsoft')  #removes item present at the given index
print(laptops)
removed = laptops.pop(4)   #gives removed item present at the given index and also removes item 
print(removed)
print(laptops)
#again insert the microsoft
laptops.insert(2, 'microsoft')
#again append the microsoft
laptops.append('microsoft')
print(laptops)

count = laptops.count('microsoft') #gives the count of given item in the list
print(count)
laptops.sort() #ascending order
print(laptops)
laptops.sort(reverse=True) #descending order
print(laptops)
laptops.reverse() #reverse the item
print(laptops)
copy_laptops = laptops.copy() #gives copy of mentioned list
print(copy_laptops)
copy_laptops.clear() #clear the list
print(copy_laptops)
a = [1,2,3,4,5]
laptops.extend(a)
print(laptops)