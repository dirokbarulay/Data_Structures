# --- INSERTION SORT ---
# Baştaki sıralıdır. İkinci sayı solundaki değer ile karşılaştırılır ve değer kendisinden 
# küçük ise sola doğru kaydırılır.
# Döngüde sıfırıncı indis sıralı kabul edildiği için birinci indisten başlanılır.

# 1.) 22| 27 16 2 18 6
# 2.) 22 27| 16 2 18 6
# 3.) 22 27 16| 2 18 6  ->  22 16 27 2 18 6  ->  16 22 27 2 18 6
# 4.) 16 22 27 2| 18 6  ->  16 22 2 27 18 8  ->  16 2 22 27 18 6  ->  2 16 22 27 18 6
# 5.) 2 16 22 27 18| 6  ->  2 16 22 18 27 6  ->  2 16 18 22 27 6  
# 6.) 2 16 18 22 27 6|  ->  2 16 18 22 6 27  ->  2 16 18 6 22 27  ->  2 16 6 18 22 27  -> 2 6 16 18 22 27

# Big-O gösterimi: O(n^2)

# 18 sayısı ortada bulunduğundan average case içerisine dahil olur.
def inser_sort(dizi):
    for i in range(1, len(dizi)):
        key = dizi[i]
        j = i - 1

        while j >= 0 and key < dizi[j]:
            dizi[j+1] = dizi[j]
            j = j - 1
        dizi[j+1] = key
a_array = [22, 27, 16, 2, 18, 6]
inser_sort(a_array)
print(a_array)



# --- SELECTION SORT ---
# Sel. Sort: Listenin başındaki değer ile en küçük değerin yerini değiştirir. Sonrasında diğer küçük değeri
# değeri arar ama bu sefer il sıradaki değere bakmaz bu işlemi yaparken. En küçük değer ile ikinci sıradaki
# değerlerin yerlerini değiştirir. Ve bu işlem dizi küçüktrn büyüğe sıralayıncaya kadar devam eder.

# [7, 3, 5, 8, 2, 9, 4, 15, 6] 
# 1.) [2, 3, 5, 8, 7, 9, 4, 15, 6]
# 2.) [2, 3, 5, 8, 7, 9, 4, 15, 6]
# 3.) [2, 3, 4, 8, 7, 9, 5, 15, 6]
# 4.) [2, 3, 4, 5, 7, 9, 8, 15, 6]
# 5.) [2, 3, 4, 5, 6, 9, 8, 15, 7]
# 6.) [2, 3, 4, 5, 6, 7, 8, 15, 9]
# 7.) [2, 3, 4, 5, 6, 7, 8, 15, 9]
# 8.) [2, 3, 4, 5, 6, 7, 8, 9, 15]

# Big-O gösterimi: O(n^2)

def sel_sort(dizi1):
    for a in range(len(dizi1)):
        min_index1 = a
        for b in range(a+1, len(dizi1)):
            if dizi1[min_index1] > dizi1[b]:
                min_index1 = b 
        if min_index1 != a:
            dizi1[min_index1], dizi1[a] = dizi1[a], dizi1[min_index1]
b_array = [7, 3, 5, 8, 2, 9, 4, 15, 6]
sel_sort(b_array)
print(b_array)

www.patika.dev 
