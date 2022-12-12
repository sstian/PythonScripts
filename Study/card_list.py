"""
2019.11.09 19:57
列表 字典
"""

ming_dict = {"name": "ming",}
print(ming_dict)

card_list = [
    {"name": "ming",
     "qq": "12345",
     "phone": "10086"},
    {"name": "hong",
     "qq": "54321",
     "phone": "10010"}
]
for card_dict in card_list:
    print(card_dict)
