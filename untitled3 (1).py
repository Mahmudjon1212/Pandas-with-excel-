# -*- coding: utf-8 -*-
"""Untitled3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JfXlusbkIkFehO6CcAizqy8x3ZX7d4A7
"""

import pandas as pd
baza={
    "FISH":["Qadanova Zulayxo","Durbek Xalilov", "Jalilov M", "Jo'rayeva G",  "Jo'rayeva G", "Arabboyev A" ],
    "Fan nomi":[ "Sun'iy intelekt", "Sun'iy intelekt", " Kampyuterni tashkil etish", "Elektronoka va Sxamalr", "Elektronoka va Sxamalr","Kiberxavfsizlik asoslari"  ],
    "Mashgulot turi":[ "Amaliy", "Ma'ruza", "Ma'ruza", "Ma'ruza", "Amaliy", "Amaliy"      ],
    "Kafedrasi":["Axborot Texnalogiyalari", "Axborot Texnalogiyalari", ""],
    "Kafedrasi":["Axborot Texnalogiyalari", "Axborot Texnalogiyalari", "Axborot Texnalogiyalari", "Axborot Texnalogiyalari", "Axborot Texnalogiyalari", "Axborot Texnalogiyalari"],

}
dp=pd.DataFrame(baza)
print(dp)

dp.to_excel("o'qituvchilar.xlsx")