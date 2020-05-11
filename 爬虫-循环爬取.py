from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions

# option = ChromeOptions()
# option.add_experimental_option('excludeSwitches', ['enable-automation'])
# driver = Chrome(options=option)

mycount=0
#["湖北",""]
myshengfen=["陕西","内蒙古","辽宁","吉林","黑龙江","上海","江苏","安徽","江西", '湖北', '湖南', '重庆', '四川', '贵州','云南', '广东', '广西', '福建', '甘肃', '宁夏', '新疆', '西藏', '海南', '浙江',
'青海']
myshengfencount=[1258,347,1348,1234,1042,971,2428,742,1333,1986, 1433, 814, 1250, 356, 688, 809, 803, 1035, 490, 198,56 ,305, 386, 1088,
89]
myfinish001={}
myfinish002={}
def myfun1(mystr,myfilename):
    mystr001=str(mystr).split("\n")
    global mycount
    pass
    myfilename2=myfilename+"_data_2018_001.txt"
    myfile = open(myfilename2, "a", encoding="utf-8")

    for k in range(1,len(mystr001)):
        myl0=mystr001[k].split(" ")
        mydict001={}
        mydict001["school_name"]=myl0[0]
        mydict001["zhuanye"] = myl0[1]
        mydict001["shengfen"] = myl0[2]
        mydict001["kaosheng"] = myl0[3]
        mydict001["pici"] = myl0[4]
        mydict001["ave_value"] = myl0[5]
        mydict001["min_value"] = myl0[6]
        mydict001["leixing"] = myl0[7]
        mydict001["year"] = 2018
        myfile.write(str(mydict001)+"\n")
        #print(mycount,k,str(mydict001)+"\n")
        mycount=mycount+1
    myfile.close()
def  myfun2():
    f = csv.reader(open('data_count.csv', 'r', encoding="utf-8"))
    mydic001 = {}
    for i in f:
        print(i[0],int(i[1]))
        mydic001[i[0]] = int(i[1])
    return mydic001
def  myfun3(mydic003):
    writer = csv.writer(open('data_count.csv', 'w', encoding="utf-8", newline=''))
    for key, item in mydic003.items():
        #print((key, item))
        writer.writerow((key, item), )



# 后面是你的浏览器驱动位置，记得前面加r'','r'是防止字符转义的
ii=0
while ii<len(myshengfen):
#for ii in range(0,len(myshengfen)):
    myfinish002=myfun2() #读取当前省份页数
    print(type(myfinish002),myfinish002)
    mypagecount=int(myfinish002[myshengfen[ii]])
    print(myshengfen[ii],myfinish002[myshengfen[ii]])
    if mypagecount==myshengfencount[ii]:#省份 读取完成
        ii=ii+1
        continue

    driver = webdriver.Chrome()
    # 用get打开百度页面
    #https://gkcx.eol.cn/
    #https://gkcx.eol.cn/special "查专业"
    #https://gkcx.eol.cn/linepro “院校分数线”  “专业分数线” “陕西”
    #====1
    myurl=r"https://gkcx.eol.cn/"
    driver.get(myurl)
    sleep(5)
    xu0=WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "nav-li")))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 异步提交，必须把页面滚到最底部
    sleep(3)
    for xx0 in xu0:
        if xx0.text=='查专业':
            xu1=xx0.click()
            sleep(3)
            break
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 异步提交，必须把页面滚到最底部
    sleep(3)
    driver.page_source  # 异步更新数据源
    #====2
    xu0=WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "nav-li")))
    for xx0 in xu0:
        if xx0.text=='院校分数线':
            xu1=xx0.click()
            sleep(3)
            break
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 异步提交，必须把页面滚到最底部
    sleep(3)
    driver.page_source  # 异步更新数据源
    #====3
    xu0=WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "nav-li")))
    for xx0 in xu0:
        if xx0.text=='专业分数线':
            xu1=xx0.click()
            sleep(3)
            break
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 异步提交，必须把页面滚到最底部
    sleep(3)
    driver.page_source  # 异步更新数据源



    myurl=r"https://gkcx.eol.cn/linespecialty?province="+myshengfen[ii]+r"&schoolyear=2018"
    #driver.get(r"https://gkcx.eol.cn/linespecialty?province=天津&schoolyear=2018")
    driver.get(myurl)
    sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")#异步提交，必须把页面滚到最底部
    sleep(2)
    mydata=[]
    j=0
    #for j in range(0,myshengfencount[ii]):
    while  j<myshengfencount[ii]:
        j0=0
        try:
            print("点击下一页--后")
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "fypages"))
            )
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 异步提交，必须把页面滚到最底部
            sleep(3)
            driver.page_source  # 异步更新数据源
            x1=WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.CLASS_NAME,"search-table"))
            )
            # 文本处理
            if j + 1 > mypagecount or mypagecount==0:
                myfun1(x1.text, myshengfen[ii])  # 写入数据
                myfinish002[myshengfen[ii]] = j + 1
                myfun3(myfinish002) #写入当前页码
                myfinish001[myshengfen[ii]] = j + 1
                print("写入页面:",j + 1)
            else:
                print("不写入页面:",j+1,"写完页面：",mypagecount)
        except:
            print("没有发现页面1")
            driver.quit()
            break
        try:
            print(myshengfen[ii],myshengfencount[ii],"1-页码：",j+1," ===x1"*10)
            x3=driver.find_element_by_class_name("fypages")
            x4=x3.find_elements_by_tag_name("li")

            x6=[]
            for kk in x4:
                x6.append(kk)
            print(x6[-1].text,x6[-2].text,x6[-3].text,x6[-4].text,x6[-5].text)
            x5=int(x6[-3].text)
            if  mypagecount-x5>=5:
                pass
                new=x4[-3].click()
                sleep(1)
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, "fypages"))
                )
                #driver.page_source #异步更新数据源
                ##sleep(1)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 异步提交，必须把页面滚到最底部
                #sleep(1)
                driver.page_source  # 异步更新数据源
                print("点击完 本页",j)
                j=x5-1

            else:
                pass
                for i in x4:
                    print(i.text,end=' ')
                    if i.text=='下一页':
                        new=i.click()
                        sleep(1)
                        WebDriverWait(driver, 10).until(
                            EC.presence_of_element_located((By.CLASS_NAME, "fypages"))
                        )
                        #driver.page_source #异步更新数据源
                        ##sleep(1)
                        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 异步提交，必须把页面滚到最底部
                        sleep(1)
                        driver.page_source  # 异步更新数据源
                        print("点击完 下一页2",j+1)
                        j=j+1
                        break
        except:
            pass
            print("点击下一页后，没有发现页面2")
            driver.quit()
            break

    # 关闭浏览器
    driver.quit()
    if j+1==myshengfencount[ii]:
        print(myshengfen[ii],myshengfencount[ii],"1成功了--结束了")
        ii=ii+1
    else:
        myfinish002 = myfun2()  # 读取当前省份页数
        mypagecount = int(myfinish002[myshengfen[ii]])
        print("重新连接省份:",myshengfen[ii],j+1,mypagecount)
