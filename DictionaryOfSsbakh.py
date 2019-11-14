import os
import sys

#开始界面
def start():
    os.system("cls")
    #欢迎语
    line1 = "================================================================================"
    line2 = "----------------------------------------"
    line3 = "--------------------------------------------"
    zh_cn_welcome = "欢迎使用施巴赫语翻译系统"
    sk_sk_welcome = "belonemok ukhel ssbakh ubelasaik sistem"
    option1 = ">   1.中文->ssbakh     hanngio->ssbakh   <"
    option2 = ">   2.ssbakh->中文     ssbakh->hanngio   <"
    option3 = ">   3.添加词条         intleg himpik     <"
    option4 = ">   4.退出             band              <"

    print(line1.center(80))
    print(zh_cn_welcome.center(68))
    print(line2.center(80))
    print(sk_sk_welcome.center(80))
    print(line1.center(80))
    print("\n\n\n")
    print(line3.center(80))
    print(option1.center(80))
    print(line3.center(80))
    print(option2.center(80))
    print(line3.center(80))
    print(option3.center(80))
    print(line3.center(80))
    print(option4.center(80))
    print(line3.center(80))
    start_chose = input("\n\n\n请输入选项前的数字，按回车确认:\n")
    if start_chose == "1":
        ZhToSsbakh()
    elif start_chose == "2":
        SsbakhToZh()
    elif start_chose == "3":
        AddWord()
    elif start_chose == "4":
        sys.exit()
    else:
        error = input("输入有误，请重新输入！")

#汉施翻译
def ZhToSsbakh():
    os.system("cls")
    filename = os.getcwd() + str("dic.txt")
    ZhSearch(filename)

def ZhSearch(filename):
    try:
        with open(filename,'r') as dic:
            os.system("cls")
            flag = 0
            keyword = input("请输入汉语：")
            print("ssbakh\t词性\t阴性\t阳性\t复数\t中文\n")
            for line in dic:
                str_result = line
                list = str_result.split('\t')
                zh_all = list[5]
                zh_part = zh_all.split('；')
                len_zh = 0
                len_zh = len(zh_part)
                i = 0
                zh = []
                while(i < len_zh ):
                    buff_list = zh_part[i]
                    zh_one = buff_list.split("，")
                    zh += zh_one
                    i += 1
                if keyword in zh:
                    print (str_result)
                    flag = 1
            if not flag:
                buff = input("暂时没有收录这个词语，请更换词典文件或手动录入,按任意键回到初始菜单")
            chose = input("搜索完成，是否继续搜索?[Y/N]")
            if chose == 'Y' or chose == 'y':
                ZhSearch(filename)
            elif chose == 'N' or chose == 'n':
                chose == input("是否重新选择字典?[Y/N]")
                if chose == 'Y' or chose == 'y':
                    ZhToSsbakh()
                elif chose == 'N' or chose == 'n':
                    buff = input("按任意键返回初始菜单")
                else:
                    buff = input("输入错误！请按任意键")
            else:
                buff = input("输入错误！请按任意键")
            dic.close()
    except OSError as reason:
        print("出错啦！"+str(reason))
        chose = input("是否手动输入词典文件路径？[Y/N]")
        if chose == "Y" or chose == "y":
            newfilename = input("请输入字典文件路径及名称：")
            os.system("cls")
            ZhSearch(newfilename)
        elif chose == "N" or chose == "n":
            buff = input("按任意键返回初始菜单，若要新建词典文件，请选择3")

#施汉翻译
def SsbakhToZh():
    os.system("cls")
    filename = os.getcwd() + str("dic.txt")
    SsSearch(filename)

def SsSearch(filename):
    try:
        with open(filename,'r') as dic:
            os.system("cls")
            flag = 0
            keyword = input("请输入Ssbakh：")
            print("ssbakh\t词性\t阴性\t阳性\t复数\t中文\n")
            for line in dic:
                str_result = line
                list = str_result.split('\t')
                sk_all = list[0]
                if keyword in sk_all:
                    print (str_result)
                    flag = 1
            if not flag:
                buff = input("暂时没有收录这个词语，请更换词典文件或手动录入,按任意键回到初始菜单")
            chose = input("搜索完成，是否继续搜索?[Y/N]")
            if chose == 'Y' or chose == 'y':
                SsSearch(filename)
            elif chose == 'N' or chose == 'n':
                chose == input("是否重新选择字典?[Y/N]")
                if chose == 'Y' or chose == 'y':
                    SsbakhToZh()
                elif chose == 'N' or chose == 'n':
                    buff = input("按任意键返回初始菜单")
                else:
                    buff = input("输入错误！请按任意键")
            else:
                buff = input("输入错误！请按任意键")
            dic.close()
    except OSError as reason:
        print("出错啦！"+str(reason))
        chose = input("是否手动输入词典文件路径？[Y/N]")
        if chose == "Y" or chose == "y":
            newfilename = input("请输入字典文件路径及名称：")
            os.system("cls")
            ZhSearch(newfilename)
        elif chose == "N" or chose == "n":
            buff = input("按任意键返回初始菜单，若要新建词典文件，请选择3")

#打开文件
def OpenDictionary(filename):
	try:
		with open(filename,'r+') as dic:
			data = dic.readlines()
			buff = input("字典打开成功,按任意键继续")
			os.system("cls")
	except OSError as reason:
		print("出错啦！"+str(reason))
		CreatFile(filename)
	else:
		WriteDictionary(filename)

#写入文件
def WriteDictionary(filename):
    restr = inputword()
    print(restr)
    try:
        with open(filename,'a') as dic:
            dic.write(restr)
            dic.close()
            os.system("cls")
    except OSError as reason:
        print("出错啦！"+str(reason))
        buff = input("按任意键返回初始菜单")
    else:
        EditInput(filename)

#编辑输入
def EditInput(filename):
    chose = input("词条录入成功，是否继续？[Y/N]：")
    if chose == "Y" or chose == 'y':
        WriteDictionary(filename)
    elif chose == "N" or chose == 'n':
        buff = ("按任意键返回初始菜单")
    else:
        buff = input("输入错误！请按任意键")
        EditInput(filename)

#输入
def inputword():
    sk = input("请输入单词：\n")
    te = input("请输入词性：\n")
    ea = input("请输入阴性形式:\n")
    ei = input("请输入阳性形式:\n")
    ko = input("请输入复数形式:\n")
    zh = input("请输入中文释义:\n")
    tab = "\t"
    ret = "\n"
    restr = sk+tab+te+tab+ea+tab+ei+tab+ko+tab+zh+ret
    print("restr")
    return restr

#创建文件
def CreatFile(filename):
	chose = input("是否创建文件？[Y/N]：")
	if chose == "Y" or chose == 'y':
		dic = open(filename,mode="w",encoding="utf-8")
		EditFile(filename)
	elif chose == "N" or chose == 'n':
		buff = input("按任意键返回初始菜单")
	else:
		buff = input("输入错误！请按任意键")
		CreatFile(filename)
#编辑文件
def EditFile(filename):
	chose = input("已创建文件，是否编辑？[Y/N]：")
	if chose == "Y" or chose == 'y':
		OpenDictionary(filename)
	elif chose == "N" or chose == 'n':
		buff = input("按任意键返回初始菜单")
	else:
		buff = input("输入错误！请按任意键")
		EditFile(filename)

#添加词条
def AddWord():
	os.system("cls")
	filename = input("请输入字典文件路径及名称：")
	OpenDictionary(filename)



if __name__ == "__main__":
    while(1):
        start()