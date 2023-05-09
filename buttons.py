from aiogram.types import ReplyKeyboardMarkup , KeyboardButton, InlineKeyboardMarkup , InlineKeyboardButton
from  aiogram import types
btn = KeyboardButton("Asosiy Menu")

#--------------------- Asosiy tugmalar ------------------------------

btn6 = KeyboardButton("Orqaga 🔙")
btn2 = KeyboardButton("Ayollar uchun chiqarilgan qaror va farmonlar")
btn3 = KeyboardButton("Ayollar daftari")
btn4 = KeyboardButton("Ayollar uchun Imtiyozli kreditlar")
btn = ReplyKeyboardMarkup(resize_keyboard=True).add(btn3, btn4, btn2, btn6)

#------------------------ Tilni tanlang tugmalari ---------------------------



# -------------------------- Inline Shahar va tumanlar -------------------------------

help_uz = InlineKeyboardMarkup(row_width=2)
help_Fergana = InlineKeyboardButton(text='Farg\'ona viloyati', callback_data='help_f')
help_tashkent = InlineKeyboardButton(text='Toshkent shahri', callback_data='help_t')
help_Andijon = InlineKeyboardButton(text="Andijon viloyati", callback_data='help_a')
help_Namangan = InlineKeyboardButton(text="Namangan viloyati", callback_data='help_n')
help_uz.insert(help_Fergana)
help_uz.insert(help_tashkent)
help_uz.insert(help_Andijon)
help_uz.insert(help_Namangan)

#---------------------------------- WEb sahifani inline ulash------------------------------------

ikb = InlineKeyboardMarkup(row_width=2)

ikb1 = InlineKeyboardButton(text='Bizning Web-saytimiz',
                            url='https://ayollar-huquqlari-mohirfest.netlify.app/')


ikb.add(ikb1)


ikb2 = InlineKeyboardMarkup(row_width=2)

ikb3 = InlineKeyboardButton(text='Web-saytga o\'tish',
                            url='https://qalampir.uz/uz/news/prezident-khotin-k-izlar-uchun-yangidan-yangi-imkoniyatlar-aks-etgan-farmonni-imzoladi-57204')


ikb2.add(ikb3)

#




#------------
# -------------------------------- Telefon raqamini yuborish --------------------------------------

markup_requests = ReplyKeyboardMarkup(resize_keyboard=True)
markup_requests.add(KeyboardButton('Telefon no\'merni ulashish', request_contact=True))

#--------------------------------------------- Gender ----------------------------------------


#--------------------------------------------- Gender tugadi ---------------------------------------

#----------------------------------------------- Sector 1  ---------------------------------------------

sector = InlineKeyboardMarkup(row_width=True)
sector2 = InlineKeyboardButton(text='1-Sektor (Hokim)', callback_data='firsec')
sector3 = InlineKeyboardButton(text='2-Sektor (Prokuror)', callback_data='secosec')
sector4 = InlineKeyboardButton(text='3-Sektor (IIB)', callback_data='thirsec')
sector5 = InlineKeyboardButton(text='4-Sektor (Soliq)', callback_data='fivesec')
sector6 = InlineKeyboardButton(text='Bilmayman', callback_data='sixsec')

sector.add(sector2, sector3, sector4, sector5, sector6)
#------------------------------ Sector 2--------------------------------------------
sector_village = InlineKeyboardMarkup(row_width=True)

village1 = InlineKeyboardButton(text='Toshloq tumani', callback_data='tvill')
village2 = InlineKeyboardButton(text='Marg\'ilon tumani',callback_data='mvill')

sector_village.add(village1, village2)
#----------------------------- Sector 3 ------------------------------------------
sector_village2 = InlineKeyboardMarkup(row_width=True)
village3 = InlineKeyboardButton(text='Yakkatut qishlog\'i', callback_data='yvill')
village4 = InlineKeyboardButton(text='Navbahor qishlog\'i', callback_data='nvill')

sector_village2.add(village3, village4)
#------------------------------ Sector 4 ------------------------------------------------
sector_village3 = InlineKeyboardMarkup(row_width=True)

village4 = InlineKeyboardButton(text='Turvat qishlog\'i', callback_data='tvill')
village5 = InlineKeyboardButton(text='Yuqori qishlog\'i', callback_data='yvill')
village6 = InlineKeyboardButton(text='Zarkent qishlog\'i', callback_data='zvill')

sector_village3.add(village6, village5, village4)
