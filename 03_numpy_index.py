#  3-kun: Indexing, Slicing, Boolean Indexing, Fancy Indexing, Shape manipulations
import numpy as np

# 1. 2x3 o‘lchamli massiv yaratish
a = np.array([[1, 2, 3], [4, 5, 6]])
print("2x3 massiv:\n", a)

# 2. Massivning o‘lchami (shape) va o‘lchov darajasi (ndim) ni aniqlash
print("O‘lchami:", a.shape)
print("O‘lchov darajasi:", a.ndim)

# 3. Massivdagi barcha elementlar sonini aniqlash
print("Elementlar soni:", a.size)

# 4. 3x3 bo‘sh (zero) massiv yaratish
b = np.zeros((3, 3))
print("Zero massiv:\n", b)

# 5. 4x2 birlik (ones) massiv yaratish
c = np.ones((4, 2))
print("Ones massiv:\n", c)

# 6. Random sonlar bilan 2x5 massiv
d = np.random.rand(2, 5)
print("Random massiv:\n", d)

# 7. Aralash random butun sonlar (0 dan 10 gacha) bilan massiv
e = np.random.randint(0, 10, (3, 4))
print("Butun random massiv:\n", e)

# 8. Massivni 1D dan 2D ga reshape qilish
f = np.arange(12)
f2 = f.reshape(3, 4)
print("Reshape qilingan massiv:\n", f2)

# 9. Massivning bir ustunini ajratib olish (slicing)
print("Ikkinchi ustun:", f2[:, 1])

# 10. Shartli tanlash – faqat 5 dan katta elementlar
print("5 dan katta elementlar:", f2[f2 > 5])

# 11. Massivdagi maksimal va minimal qiymatlar
print("Maks:", f2.max(), "| Min:", f2.min())

# 12. Massiv bo‘yicha ustunlar kesimida yig‘indi
print("Ustunlar bo‘yicha yig‘indi:", f2.sum(axis=0))

# 13. Massiv bo‘yicha satrlar kesimida o‘rtacha
print("Satrlar bo‘yicha o‘rtacha:", f2.mean(axis=1))

# 14. Massivdagi elementlarning indeksini topish (qayerda 7 bor?)
print("7 elementi qayerda:", np.where(f2 == 7))

# 15. Massivni tekis (flatten) 1D ko‘rinishga o‘tkazish
print("Flatten massiv:", f2.flatten())
