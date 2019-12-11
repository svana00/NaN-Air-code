import datetime

tupl = "arnar", "gylfi", "bjorgvin" ,"eva", "magga", "svana", "hall", "sd",["anton", "hello"]
tupl1 =  "dfd", "dfsfds","fdsfds","sdfdsf",["siggi", "dsf"]
tupl2 = []
tupl2.append(tupl)
tupl2.append(tupl1)
print(len(tupl2))
siggi = tupl2


#index = int(input("Hello: "))

#list1 = list(tupl2[index])
#print(list1)
#['tuple', 'list', ['francais', 'deutschland']]
#string = " ".join(list1[:-1]) + " " + " ".join(list1[-1])
#new_list = string.split()
#new_file = new_list[4]
#print(new_file)

#file_open = open("hello.csv", "r")
#file_new = open("new_hello.csv", "w+")
#for line in file_open:
#    file_new.write(line.replace("antn", "anton").replace("ds", "siggi"))

my_str = "2019-11-02T06:03:00"
print(datetime.datetime.fromisoformat(my_str))
#new = my_str.replace("T", "-").replace(":", "-")
#n_lsit = my_str.split("-")
#n_lsit = [int(i) for i in n_lsit]
#year = n_lsit[0]
#month = n_lsit[1]
#day = n_lsit[2]
#hour = n_lsit[3]
#minute = n_lsit[4]

print(datetime.datetime.now())
now = datetime.datetime.now().replace(microsecond=0).replace(second=0).isoformat()
start = datetime.datetime(2019, 12, 11, 15, 23, 00).isoformat()
end = datetime.datetime(2019, 12, 12, 15, 23, 00).isoformat()
if start <= now <= end:
    print("Tesdi")
