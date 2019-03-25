import csv, datetime, copy



'''
修复要求：1.CSV中的数据理论上都是间隔5分钟的取样数据，若间隔大于5分钟则视为数据缺失，需要修复为间隔5分钟一条
修复原则为缺乏的数据向上一个5分钟取，若上一个5分钟也缺失则向上上一个，一次补全。注意时间格式

'''
def fix_csv_per5min():
    totalupdate = []
    with open("1.csv", 'r') as csvFile:
        line_csv = csv.reader(csvFile)
        # 将CSV中的数据存到列表中，列表的形式可以通过下标实现各种需求比较方便
        lines = []
        for line in line_csv:
            lines.append(line)

        # 记录datetime类型相差5分钟的格式，方便后面比较时间差
        mult = datetime.datetime.strptime(lines[2][0], '%m/%d/%Y %H:%M') - datetime.datetime.strptime(lines[1][0], '%m/%d/%Y %H:%M')

        # 检查i和i+1组的时差是否为5分钟，若不是则插入自i组复制后只修改时间的line
        # 这时新插入的line索引为i+1，与i+2（即之前的i+1）再次对比，知道i+n与i+n+1相差5分钟，则一个区间的数据修复完毕
        for i in range(1, len(lines)-1):
            line0 = lines[i]
            line1 = lines[i+1]
            mintime0 = line0[0]
            mintime1 = line1[0]
            mintime0 = datetime.datetime.strptime(mintime0, '%m/%d/%Y %H:%M')
            mintime1 = datetime.datetime.strptime(mintime1, '%m/%d/%Y %H:%M')
            # print(type(mintime0))
            if((mintime1 - mintime0) != mult):
                recursion_insert_list_into_lists(lines, i)
                totalupdate.append(i+1)

    # 保存之前的格式处理
    # 这是我样例数据格式的特殊要求，暂时没有好的方法能更漂亮的解决这个问题
    for i in totalupdate:
        lines[i][0] = lines[i][0][:11] + lines[i][0][12:]
        lines[i][0] = lines[i][0][1:]
    print("一共插入了", len(totalupdate), "组数据")

    # 写入CSV文件
    with open('2.csv', 'w') as myCsv:
        myWriter = csv.writer(myCsv)
        myWriter.writerows(lines)


# 第i组和第i+1组之间插入一个list
def recursion_insert_list_into_lists(lines, i):
    mult = datetime.datetime.strptime(lines[2][0], '%m/%d/%Y %H:%M') - datetime.datetime.strptime(lines[1][0], '%m/%d/%Y %H:%M')
    # linetemp = lines[i]造成深拷贝，如下改成浅拷贝
    linetemp = copy.copy(lines[i])
    linetemp[0] = datetime.datetime.strptime(linetemp[0], '%m/%d/%Y %H:%M')
    linetemp[0] += mult
    linetemp[0] = linetemp[0].strftime('%m/%d/%Y %H:%M')
    lines.insert(i+1, linetemp)
    print(linetemp)
    pass


if __name__ == '__main__':
    fix_csv_per5min()