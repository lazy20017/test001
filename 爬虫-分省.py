from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
mycount=0
#["湖北",""]
myshengfen=["陕西","内蒙古","辽宁","吉林","黑龙江","上海","江苏","安徽","江西", '湖北', '湖南', '重庆', '四川', '贵州','云南', '广东', '广西', '福建', '甘肃', '宁夏', '新疆', '西藏', '海南', '浙江',
'青海']
myshengfencount=[1258,347,1348,1234,1042,971,2428,742,1333,1986, 1433, 814, 1250, 356, 688, 809, 803, 1035, 490, 198,56 ,305, 386, 1088,
89]
myshengfen=myshengfen[::-1]
myshengfencount=myshengfencount[::-1]
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
        print(mycount,k,str(mydict001)+"\n")
        mycount=mycount+1
    myfile.close()


# 后面是你的浏览器驱动位置，记得前面加r'','r'是防止字符转义的
for ii in range(0,len(myshengfen)):
    driver = webdriver.Chrome()
    # 用get打开百度页面
    myurl=r"https://gkcx.eol.cn/linespecialty?province="+myshengfen[ii]+r"&schoolyear=2018"
    #driver.get(r"https://gkcx.eol.cn/linespecialty?province=天津&schoolyear=2018")
    driver.get(myurl)
    sleep(5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")#异步提交，必须把页面滚到最底部
    sleep(2)
    mydata=[]
    for j in range(0,myshengfencount[ii]):
        try:
            x1=WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.CLASS_NAME,"search-table"))
            )
        except:
            pass
        #文本处理
        myfun1(x1.text,myshengfen[ii])
        print(myshengfen[ii],myshengfencount[ii],"2-页码：",j+1," ===x1"*10)
        x3=driver.find_element_by_class_name("fypages")
        x4=x3.find_elements_by_tag_name("li")
        for i in x4:
            print(i.text)
            if i.text=='下一页':
                new=i.click()
                sleep(3)
                driver.page_source #异步更新数据源
                sleep(1)
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # 异步提交，必须把页面滚到最底部
                sleep(1)
                break
    # 关闭浏览器
    driver.quit()
    print(myshengfen[ii],myshengfencount[ii],"2-成功了--结束了")
