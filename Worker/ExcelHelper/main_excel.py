"""
app -> books -> sheets -> range -> value, ...
"""
import xlwings as xw


def write_excel():
    app = xw.App(visible=False, add_book=False)
    wb = app.books.add()
    # sheet1 = wb.sheets["Sheet1"]
    sheet1 = wb.sheets[0]
    print(f"sheet name = {sheet1.name}")
    # sheet1.range("A1").value = "hello"
    # sheet1["A1"].value = ["hello", "world", "are you ok"]
    sheet1.range("A1").value = ["hello", "world", "are you ok???"]
    c1 = sheet1.range("C1")
    c1.color = (255, 0, 0)
    c1.autofit()

    wb.save(r"me.xlsx")
    wb.close()
    app.quit()


def read_excel():
    app = xw.App(visible=False, add_book=False)
    wb = app.books.open(r"me.xlsx")
    sheet1 = wb.sheets["Sheet1"]
    values = sheet1.range("A1:C1").value
    print(values)

    wb.close()
    app.quit()


if __name__ == "__main__":
    print("excel helper")
    write_excel()
    # read_excel()


