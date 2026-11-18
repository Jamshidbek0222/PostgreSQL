# PostgreSQL

# Database optimisation
    # 1) Query optimisation
    # 2)Indexing
    # 3)Replication
    # 4)Sharding
    
    

# Database Replication (replikatsiya) — bu bitta ma'lumotlar bazasidagi barcha ma'lumotlarni real vaqt rejimida (yoki ma'lum bir vaqt oralig'ida) bir yoki bir nechta boshqa serverlarga avtomatik nusxalab borish jarayonidir.
# Oddiy qilib aytganda, bu ma'lumotlar bazasining bir nechta "egizak" nusxalarini yaratish demakdir.

# Nima uchun replication kerak?

# 1. Ma'lumot yo'qolishining oldini olish (Fault Tolerance / High Availability):
# Agar asosiy server (baza) ishdan chiqsa, yonib ketsa yoki tarmoqdan uzilib qolsa, tizim to'xtab qolmaydi. U avtomatik ravishda zaxira (nusxa) serverga ulanadi va ishlashda davom etadi.
# 2. Tezlikni oshirish (Load Balancing):
# Katta tizimlarda (masalan, Instagram yoki Uzum Marketda) ma'lumot o'qish (SELECT) so'rovlari yozish (INSERT/UPDATE) so'rovlaridan yuz barobar ko'p bo'ladi. Replikatsiya yordamida o'qish yuklamasini bir nechta nusxa bazalar o'rtasida taqsimlash mumkin.
# 3. Analitika va zaxira nusxa (Backup):
# Katta hisobotlarni hisoblash yoki tahlil qilish asosiy bazani sekinlashtirib qo'ymasligi uchun bu ishlar nusxa bazada bajariladi.
