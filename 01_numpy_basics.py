#NumPy
import numpy as np  

# 1. Python ro'yxati va NumPy massivini solishtirish
python_list = [1, 2, 3, 4, 5]
numpy_array = np.array([1, 2, 3, 4, 5])
print("Python ro'yxati:", python_list)
print("NumPy massivi:", numpy_array)

# 2. np.array() bilan massiv yaratish
arr = np.array([10, 20, 30, 40])
print("Massiv:", arr)

# 3. np.arange() bilan ketma-ket sonlar yaratish
arr_range = np.arange(1, 11)  # 1 dan 10 gacha
print("Ketma-ket sonlar:", arr_range)

# 4. Massiv atributlari
print("Shape:", arr_range.shape)
print("Size:", arr_range.size)
print("Dtype:", arr_range.dtype)

# 5. Nol va birlardan iborat massivlar
zeros = np.zeros((2, 3))
ones = np.ones((3, 2))
print("Nollar massivi:\n", zeros)
print("Birlar massivi:\n", ones)

# 6. Identity (birlik) matritsa
eye = np.eye(3)
print("Identity matritsa:\n", eye)

# 7. np.linspace() bilan teng oraliqli sonlar
lin = np.linspace(0, 1, 5)
print("0 dan 1 gacha 5 ta son:", lin)

# 8. Tasodifiy sonlar (np.random.rand va randint)
rand = np.random.rand(2, 2)
randint_arr = np.random.randint(1, 10, (3, 3))
print("Tasodifiy float sonlar:\n", rand)
print("Tasodifiy int sonlar:\n", randint_arr)

# 9. Elementlar ustida oddiy amallar
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Yig'indi:", a + b)
print("Ayirma:", a - b)
print("Ko'paytma:", a * b)
print("Bo'lish:", a / b)

# 10. Massivni kesish (slicing)
print("Birinchi 3 ta element:", arr_range[:3])
print("Oxirgi 3 ta element:", arr_range[-3:])

# 11. Massivni qayta shakllantirish (reshape)
reshaped = np.arange(1, 10).reshape(3, 3)
print("3x3 massiv:\n", reshaped)

# 12. Boolean indexing
nums = np.array([5, 10, 15, 20, 25])
print("10 dan katta elementlar:", nums[nums > 10])

# 13. Agregat funksiyalar (sum, mean, max, min)
print("Yig'indi:", nums.sum())
print("O'rtacha:", nums.mean())
print("Eng katta:", nums.max())
print("Eng kichik:", nums.min())

# 14. Axis bo'yicha amallar
mat = np.array([[1, 2, 3], [4, 5, 6]])
print("Qatorlar bo'yicha yig'indi:", mat.sum(axis=1))
print("Ustunlar bo'yicha yig'indi:", mat.sum(axis=0))

# 15. np.full(), np.empty()
full_arr = np.full((2, 2), 7)
empty_arr = np.empty((2, 2))
print("7 bilan to'lgan massiv:\n", full_arr)
print("Bo'sh massiv:\n", empty_arr)

# 16. Broadcasting (bitta qiymatni butun massivga qo'shish)
arr_b = np.array([1, 2, 3])
print("Broadcasting natijasi:\n", arr_b + 5)

# 17. Massivni nusxalash (copy) va o'zgartirish
original = np.array([1, 2, 3])
copy_arr = original.copy()
copy_arr[0] = 99
print("Original:", original)
print("Nusxa:", copy_arr)
