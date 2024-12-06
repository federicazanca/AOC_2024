
list1 = []
list2 = []
with open("/home/federica/AOC_2024/day_1/input.txt") as f:
    for line in f:
        list1.append(int(line.split()[0]))
        list2.append(int(line.split()[1]))

list1 = sorted(list1)
list2 = sorted(list2)

# Part 1
tot_dist = 0
for i in range(0,len(list1)): 
    if list2[i] > list1 [i]:
        distance = list2[i] - list1[i]
    else:
        distance = list1[i] - list2[i]
    tot_dist = tot_dist + distance
print(tot_dist)

# Part 2
num_dict = {}
for j in range(len(list2)):
    if list2[j] in num_dict:
        num_dict[list2[j]] += 1
    else:
         num_dict[list2[j]] = 1

tot_sim = 0
for k in range(len(list1)):
    if list1[k] in num_dict.keys():
        similarity = list1[k] * num_dict[list1[k]]
        tot_sim = tot_sim + similarity

print(tot_sim)

