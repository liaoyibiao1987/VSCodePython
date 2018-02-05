import xlrd

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
    for i,item in enumerate(books):
        print (int(i+1),item[0],item[1],int(item[2]),int(item[3]))
        sum +=item[3]

    print ("total amount is：",int(sum))

if __name__ == "__main__":
    print_xls('demo.xls')