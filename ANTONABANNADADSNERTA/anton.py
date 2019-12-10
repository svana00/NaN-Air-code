tupl = "arnar", "gylfi", "bjorgvin" ,"eva", "magga", "svana", "hall", "sd",["anton", "hello"]
tupl1 =  "dfd", "dfsfds","fdsfds","sdfdsf",["siggi", "dsf"]
tupl2 = []
tupl2.append(tupl)
tupl2.append(tupl1)
print(len(tupl2))
siggi = tupl2


index = int(input("Hello: "))
list1 = list(tupl2[index])
print(list1)
['tuple', 'list', ['francais', 'deutschland']]
string = " ".join(list1[:-1]) + " " + " ".join(list1[-1])
new_list = string.split()
new_file = new_list[4]
print(new_file)

file_open = open("hello.csv", "r")
file_new = open("new_hello.csv", "w+")
for line in file_open:
    file_new.write(line.replace("antn", "anton").replace("ds", "siggi"))



