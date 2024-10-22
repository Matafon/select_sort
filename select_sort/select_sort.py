select_sort = [int(x) for x in input("Zadej hodnoty seznamu:" ).split(',')]
n = len(select_sort)

for j in range(n - 1):
    i_min = j
    for i in range(j + 1, n):
        if select_sort[i] < select_sort[i_min]:
            i_min = i
    if i_min != j:
        t = select_sort[j]
        select_sort[j] = select_sort[i_min]
        select_sort[i_min] = t

print(select_sort)