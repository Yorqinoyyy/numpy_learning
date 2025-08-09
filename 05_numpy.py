# Day 5 - NumPy Advanced Practice
# Author: Yorqinoy
# GitHub: https://github.com/yorqinoyyy
# Description: 20 ta NumPy misoli — oddiydan professionalgacha, yangi mavzular asosida

import numpy as np

# 1. 1D massiv yaratish va teskari tartibda chiqarish
arr = np.arange(10)
print("Original:", arr)
print("Reversed:", arr[::-1])

# 2. 2D massivni tekis (flatten) massivga aylantirish
matrix = np.array([[1, 2], [3, 4], [5, 6]])
flat = matrix.flatten()
print("Flattened array:", flat)

# 3. Massivning shaklini (shape) almashtirish
reshaped = np.arange(12).reshape(3, 4)
print("Reshaped array:\n", reshaped)

# 4. Massivning faqat unik qiymatlarini olish
dup_array = np.array([1, 2, 2, 3, 4, 4, 5])
unique_values = np.unique(dup_array)
print("Unique values:", unique_values)

# 5. Ikki massiv o‘xshashligini tekshirish
a = np.array([1, 2, 3])
b = np.array([1, 2, 3])
print("Arrays equal?", np.array_equal(a, b))

# 6. Massiv ichidagi eng katta va kichik qiymatlarni topish
rand_arr = np.random.randint(1, 100, 10)
print("Array:", rand_arr)
print("Max:", rand_arr.max(), "Min:", rand_arr.min())

# 7. Massivning indekslarini aralashtirish (shuffle)
shuffled = np.random.permutation(rand_arr)
print("Shuffled array:", shuffled)

# 8. 1D massivdagi qiymatlar chastotasini hisoblash
values, counts = np.unique(rand_arr, return_counts=True)
print("Values:", values)
print("Counts:", counts)

# 9. NaN qiymatlarni aniqlash
nan_arr = np.array([1, np.nan, 3, np.nan, 5])
print("NaN mask:", np.isnan(nan_arr))

# 10. NaN qiymatlarni o‘rtacha bilan to‘ldirish
mean_val = np.nanmean(nan_arr)
nan_filled = np.where(np.isnan(nan_arr), mean_val, nan_arr)
print("NaN filled array:", nan_filled)

# 11. Har bir ustun bo‘yicha maksimumni topish
mat = np.random.randint(1, 50, (4, 5))
print("Matrix:\n", mat)
print("Column max:", mat.max(axis=0))

# 12. Massiv elementlarini belgilangan oraliqda kesish (clip)
clip_arr = np.clip(rand_arr, 20, 80)
print("Clipped array:", clip_arr)

# 13. 2D massivni aylantirish (transpose)
print("Transposed matrix:\n", mat.T)

# 14. Har bir elementga funksiyani qo‘llash (vectorize)
def square(x): return x ** 2
square_vec = np.vectorize(square)
print("Squared matrix:\n", square_vec(mat))

# 15. Har bir ustunning normalizatsiyasi (0-1 oraliqqa)
col_min = mat.min(axis=0)
col_max = mat.max(axis=0)
norm_matrix = (mat - col_min) / (col_max - col_min)
print("Column normalized matrix:\n", norm_matrix)

# 16. Diagonal elementlarni olish
diag_matrix = np.arange(1, 17).reshape(4, 4)
print("Matrix:\n", diag_matrix)
print("Diagonal:", np.diag(diag_matrix))

# 17. Massivni ro‘yxatga aylantirish va aksincha
list_from_array = diag_matrix.tolist()
array_from_list = np.array(list_from_array)
print("List:", list_from_array)
print("Array:", array_from_list)

# 18. Massivlarni birlashtirish (stacking)
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print("Vertical stack:\n", np.vstack((arr1, arr2)))
print("Horizontal stack:", np.hstack((arr1, arr2)))

# 19. Kosinus o‘xshashligini hisoblash
vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])
cos_sim = np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))
print("Cosine similarity:", cos_sim)

# 20. Egen qiymatlar va egen vektorlarni hisoblash
sym_matrix = np.array([[2, 1], [1, 2]])
eigenvalues, eigenvectors = np.linalg.eig(sym_matrix)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
