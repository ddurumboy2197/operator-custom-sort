from operator import attrgetter

class Talaba:
    def __init__(self, ism, baho):
        self.ism = ism
        self.baho = baho

talabalar = [
    Talaba("Ali", 85),
    Talaba("Vali", 90),
    Talaba("Hasan", 78),
    Talaba("Husan", 92),
    Talaba("Rustam", 88)
]

# Baho bo'yicha saralash
saralangan_talabalar = sorted(talabalar, key=attrgetter('baho'), reverse=True)

# Natija chiqarish
for talaba in saralangan_talabalar:
    print(f"{talaba.ism}: {talaba.baho}")
```

Kodni ishlatish uchun quyidagilarni amalga oshiring:

1. `Talaba` klassini yaratib, `ism` va `baho` atributlarini kiritib, ularni `__init__` metodida belgilab bering.
2. `talabalar` ro'yxatini yaratib, unda `Talaba` klassidan ob'ektlar yaratib, ularni ro'yxatga qo'shing.
3. `sorted` funksiyasidan foydalanib, `talabalar` ro'yxatini `baho` atributi bo'yicha kattaligidan kichikga qarab saralab, `reverse=True` parametriga `True` qiymatini berib, ro'yxatni teskari tartibda qo'yib bering.
4. `saralangan_talabalar` ro'yxatini chiqarib, unda har bir talabaning ismi va baho qiymatini konsolga chiqaring.
