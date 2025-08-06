# numpy_day2.py
# 2-KUN: NumPy bo‘yicha amaliy mashqlar (matematik amallar, statistik funksiyalar va h.k.)

import numpy as np

        # 1. Array ustida oddiy matematik amallar
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
print("1. Qo‘shish:", a + b)         # Elementlar bo‘yicha qo‘shish
print("2. Ayirish:", b - a)         # Elementlar bo‘yicha ayirish
print("3. Ko‘paytirish:", a * b)    # Elementlar bo‘yicha ko‘paytirish
print("4. Bo‘lish:", b / a)         # Elementlar bo‘yicha bo‘lish

        # 2. Skalyar bilan amallar
print("\n5. Skalyar bilan qo‘shish:", a + 5)  
print("6. Skalyar bilan ko‘paytirish:", a * 2)  

         # 3. Kvadrat ildiz va daraja
print("\n7. Kvadrat ildiz:", np.sqrt(a))  
print("8. Kvadrat daraja:", np.power(a, 2))  

         # 4. Statistika (o‘rtacha, median, max, min)
print("\n9. O‘rtacha:", np.mean(a))
print("10. Median:", np.median(a))
print("11. Eng katta qiymat:", np.max(a))
print("12. Eng kichik qiymat:", np.min(a))

          # 5. Array elementlarini tartiblash
c = np.array([10, 4, 7, 2, 15, 1])
print("\n13. Saralash (o‘sish tartibida):", np.sort(c))
print("14. Eng katta element indeksi:", np.argmax(c))
print("15. Eng kichik element indeksi:", np.argmin(c))

           # 6. Arrayning shaklini o‘zgartirish
d = np.arange(1, 13)  # 1 dan 12 gacha sonlar
print("\n16. Asl array:", d)
print("17. 3x4 ga reshape:", d.reshape(3, 4))  # 3 qator, 4 ustun
print("18. 2x2x3 (3D reshape):\n", d.reshape(2, 2, 3))

            # 7. Matritsa ko‘paytmasi (np.dot)
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print("\n19. Matritsa ko‘paytmasi:\n", np.dot(A, B))

            # 8. Tasodifiy sonlar bilan ishlash
rand_arr = np.random.randint(1, 50, size=(3, 4))  # 1-50 oralig‘ida 3x4 array
print("\n20. Tasodifiy 3x4 array:\n", rand_arr)

            # 9. Array elementlarini filtrlash (masalan, >10)
print("\n21. 10 dan katta elementlar:", rand_arr[rand_arr > 10])

            # 10. Unikal qiymatlar va ularning soni
uniq_arr = np.array([1, 2, 2, 3, 4, 4, 4, 5])
print("\n22. Unikal qiymatlar:", np.unique(uniq_arr))
print("23. Har bir qiymat soni:", np.unique(uniq_arr, return_counts=True))

            # 11. Boolean mask va shartli almashtirish
x = np.array([10, 20, 30, 40, 50])
mask = x > 25
print("\n24. 25 dan katta bo‘lgan elementlar:", x[mask])
print("25. Shartli almashtirish (agar >25 bo‘lsa 1, aks holda 0):", np.where(x > 25, 1, 0))

            # 12. Nan va Inf bilan ishlash
nan_arr = np.array([1, 2, np.nan, 4, np.inf])
print("\n26. NaN tekshirish:", np.isnan(nan_arr))
print("27. Inf tekshirish:", np.isinf(nan_arr))

            # 13. Arraylarni birlashtirish (concatenate va stack)
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6]])
print("\n28. Concatenate bilan birlashtirish:\n", np.concatenate((arr1, arr2), axis=0))

            # 14. Arrayni bo‘lish (split)
e = np.arange(1, 10)
print("\n29. Split qilingan array:", np.split(e, 3))  # 3 qismga bo‘lish

            # 15. Arange va linspace
print("\n30. np.arange (1 dan 10 gacha):", np.arange(1, 10, 2))
print("31. np.linspace (0 dan 1 gacha 5 nuqta):", np.linspace(0, 1, 5))

            # 16. Random sonlar (float)
print("\n32. np.random.rand (0-1 oralig‘ida):", np.random.rand(3))
print("33. np.random.randn (normal taqsimot):", np.random.randn(3))

            # 17. Broadcast qilish misoli
f = np.array([[1], [2], [3]])
g = np.array([10, 20, 30])
print("\n34. Broadcasting natijasi:\n", f + g)
