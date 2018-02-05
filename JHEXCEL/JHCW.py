# -*- coding=utf-8 -*-
# coding=utf-8
import xlrd
import configparser


# def getconfig(path):
#     cf = configparser.ConfigParser()
#     cf.read(path)
#     for item in cf.sections():
#         # peersec = cf.items(item)
#         inioptions = cf.options(item)
#         for opt in inioptions:
#             val = cf.get(item, opt)
#             print(item, opt, val)
#     pass


def getJHconfig(path):
    cf = configparser.ConfigParser()
    cf.read(path)
    ret = {}
    for item in (['ValidColumns', 'ColumnsIndex'], ['ValidDataType', 'ColumnsDataType']):
        val = cf.get(item[0], item[1])
        ret[item[1]] = val
    return ret

def print_xls(path):
    data = xlrd.open_workbook(path)
    table = data.sheets()[0]
    nrows = table.nrows
    books = []
    for i in range(nrows):
        ss = table.row_values(i)
        if "book" in ss:
            books.append(ss)
    sum = 0
    for i, item in enumerate(books):
        print(int(i+1), item)
        sum += item[3]

    print("total amount is：", int(sum))

def importexcle(inipath, exclepath):
    configs = getJHconfig(inipath)
    if(len(configs) > 0):
        print(configs)


if __name__ == "__main__":
    importexcle('import.ini', 'demo.xls')
