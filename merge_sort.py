#  --- MERGE SORT ---
# Problemleri küçük parçalara ayırıp çözer ve sonrasında yeniden birleştirir.

# 1.) [16,21,11,8,12,22]
# 2.) [16,21,11] [8,12,22]
# 3.) [16] [21,11] [8] [12,22]
# 4.) [16] [21] [11] [8] [12] [22]
# 5.) [16,21] [11,8] [12,22]
# 6.) [8,11,16,21] [12,22]
# 7.) [8,11,12,16,21,22]

# Big-O gösterimi: O(nlogn)

# Parçalama
def merge_sort(dizi):
    #parçalanmış hallerini görmek istersek bir alt satırdaki print kodunu çalıştırabiliriz.
    #print("Parçalama" + str(dizi))
    if len(dizi) > 1: #tek değer olması
        mid = len(dizi) // 2 
        left_array = dizi[:mid]
        right_array = dizi[mid:]
        merge_sort(left_array)
        merge_sort(right_array)
        merge_sort1(dizi, left_array, right_array)

# Birleştirme
def merge_sort1(dizi, left_array, right_array):
    a = 0
    b = 0
    c = 0

    while a < len(left_array) and b < len(right_array):
        if left_array[a] < right_array[b]:
            dizi[c] = left_array[a]
            a = a + 1
        else:
            dizi[c] = right_array[b]
            b = b + 1
        c = c + 1

    #solda eleman kalması durumunda
    while a < len(left_array):
        dizi[c] = left_array[a]
        a = a + 1
        c = c + 1

    #sağda eleman kalması durumunda
    while b < len(right_array):
        dizi[c] = right_array[b]
        b = b + 1
        c = c + 1

        #birleştirilmş hallerini görmek istersek bir alt satırdaki print kodunu çalıştırabiliriz.
        #print("Birleşme" + str(dizi))

array1 = [16,21,11,8,12,22] 
merge_sort(array1)
print(array1)
