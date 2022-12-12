import easyocr
reader = easyocr.Reader(['ch_sim','en'])
result = reader.readtext('image/nucleic-acid-20220419.jpg')

print(result)