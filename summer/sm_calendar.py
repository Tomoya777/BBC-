import os
import datetime as dt
import calendar as cl

def read_Fl( file1 ):
    with open( file1, 'r' , encoding = 'utf-8') as f1:
        str1 = f1.read()
    return str1

def write_Fl( file1,  str1 ):
    with open( file1, 'w', encoding = 'utf-8' ) as f1:
        f1.write( str1 )
    return 0

def generate_Calendar( year , month):
    cal = [""] * 42
    date =  dt.date(year,month,1) #任意の日付を代入
    wd =    date.weekday() #各曜日の情報をint型で取得している(ex 月曜日ならば0)
    if wd > 5:
        wd = wd - 7  #カレンダーに表示するときに改行する手順
    wd += 1
    cal_max = cl.monthrange(year,month)[1] #その年のその月の日数を取得
    for i in range( cal_max ):
        str2 = str(i + 1)
        j = i + wd
        cal[j] = str2 #ここまでは月の最初の曜日に1日を合わせている
    return wd, cal

def get_Schedule( year , month ,cal , wd , str0):
    cal2 =  [""] * len(cal)
    a = str.split("\n")
    for i in range( len(a1) ):
        b = a[i].strip().split(" ")
        c = b[0].split("/")
        if len(c) == 3:
            year2 = c[0]
            month2 = c[1]
            if "*" in year2 or int( year2 ) == year:
                if "*" in month2 or int( month2 ) == month:
                    d = int( c[2] )
                    e = b
                    del e[0]
                    str1 = str( " ".join(e) ).strip()
                    cal2[ d-1 + wd] += str1 + " "
    cal3 = []
    for i in range( len( cal) ):
        cal3.append( cal[i] )
        cal3.append( cal2[i] )
    return cal3

def generate_Ymd():
    now = dt.datetime.now() #現在の時刻(年月日含めて)
    year = now.year
    month = now.month
    day = now.day
    return year, month, day

def prev_next(n, year, month): #nは月の移動するときに使う
    m2 = month + n
    y2 = year + m2//12
    m2 = m2 % 12
    if m2 == 0:
        y2 = y2 - 1
        m2 = 12
    return y2,m2

def generate_Html0(year, month, cal):
    m = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "Octorber", "November", "Decenber"]
    year2,month2 =prev_next(-1, year, month)#前の月に遷移
    prev = str( year2 ) + f'{month2:02}'
    year2,month2 =prev_next( 1, year, month)#次の月に遷移
    next = str( year2 ) + f'{month2:02}'
    return prev,next


def generate_Html1(year, month, str0):
    wd, cal = generate_Calendar(year, month)
    cal2 = get_Schedule(year, month, cal, wd,str0)
    prev2, next2= generate_Html0(year, month, cal2)
    return prev2,next2
