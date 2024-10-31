# def iterativ_quick_sort(arr):
#     stack = [(0, len(arr) - 1)]
#     while stack:
#         start, end = stack.pop()
#         if start < end:
#             pivot_index = bolib_tashlash(arr, start, end)
#             stack.append((start, pivot_index - 1))
#             stack.append((pivot_index + 1, end))
#     return arr
# def bolib_tashlash(arr, start, end):
#     pivot = arr[end]
#     i = start - 1
#     for j in range(start, end):
#         if arr[j] <= pivot:
#             i += 1
#             arr[i], arr[j] = arr[j], arr[i]
#     arr[i + 1], arr[end] = arr[end], arr[i + 1]
#     return i + 1
# arr3 = [3, 6, 8, 10, 1, 2, 1]
# print("Iterativ Quick Sort:", iterativ_quick_sort(arr3))
def qator_boylab_qidirish(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


arr = [15, 3, 9, 8, 20, 7, 12]
qidirilayotgan_elementlar = [8, 15, 20, 3, 7]

print("Qator bo'ylab qidirish natijalari:")

for e in qidirilayotgan_elementlar:
    natija = qator_boylab_qidirish(arr, e)
    print(
        f"Qator bo'ylab qidirish: Element {e} {'topildi indeksda' if natija != -1 else 'topilmadi'}. Indeksi: {natija}")


def ikki_marta_qidirish(arr, x):
    chap, u = 0, len(arr) - 1
    while chap <= u:
        ortacha = (chap + u) // 2
        if arr[ortacha] == x:
            return ortacha
        elif arr[ortacha] < x:
            chap = ortacha + 1
        else:
            u = ortacha - 1
    return -1


qayta_tartiblangan_arr = sorted(arr)

qidirilayotgan_elementlar = [8, 15, 20, 3, 7]

print("\nIkki marta qidirish natijalari:")

for elem in qidirilayotgan_elementlar:
    natija = ikki_marta_qidirish(qayta_tartiblangan_arr, elem)
    print(
        f"Ikki marta qidirish: Element {elem} {'topildi indeksda' if natija != -1 else 'topilmadi'}. Indeksi: {natija}")