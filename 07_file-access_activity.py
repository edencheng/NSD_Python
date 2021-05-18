file = open("devices.txt","a")  #allow to append a item to the file

while True:
    newItem = input("Please Enter the New Devices: ")
    if newItem == "exit":
        print("All done!")
        break
    file.write(newItem+"\n")

file.close()


device_list = []
file = open("devices.txt","r")
for item in file:
    device_list.append(item)

print(device_list)

file.close()


