from openpyxl import Workbook

# 액셀 저장 모듈 만들어보기
# listdata = [[],[],[]...]

# print(os) 현재위치 ?


def write_excel_template(filename, sheetname, listdata):
    # 워크북 생성 openpyxl workbook 생성
    wb = Workbook()
    ws = wb.active

    ws.title = sheetname  # 시트명
    ws.column_dimensions["A"].width = 90  # 셀 너비 조정

    # listdata append
    for data in listdata:
        ws.append(data)

    base_dir = "./crawl/file/"  # ipynb 에서 할때랑 경로 잡는게 틀리다 (터미널에 PS E:\source\pythonsource> 까지만 되있음)
    wb.save(base_dir + filename)  # 파일명 으로 저장
    wb.close()


# 모듈 테스트용
if __name__ == "__main__":
    listdata = [["이름", "나이"], ["홍길동", 25], ["성춘향", 22]]
    write_excel_template("temp.xlsx", "test", listdata)
