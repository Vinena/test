'''
郑映慧 1619100019  2019/03/30
function:
    1.	新增联系人（查重）
    2.  修改联系人信息（查空（通讯录/联系人））
    3.	删除联系人（查空（通讯录/联系人））
    4.	查询联系人（查空（通讯录/联系人））
    5.  显示所有联系人（通讯录查空）
    6.	退出
    （通讯录可识别空的空能选项）
    注：联系人与联系电话允许为空
'''
func=0
c = {}

#     1.	新增联系人
def func_first_new():
    name=input('名字:')
    if name in c.keys():
        print("该联系人已存在！")
        print('''
    请选择操作：
    1.	删除已有联系人
    2.  修改联系人信息
    3.	查询联系人信息
    4.	返回所有功能
    5.  退出
    ''')

        refunc = input()
        if refunc == '':
            print('未选择功能，返回主菜单！')
        elif refunc == '1':
            del c[name]
            print("'",name,"'",'的信息已删除！')
        elif refunc == '2':
            c[name]=input('联系电话:')
            print("'",name,"'",'的联系电话已修改！')
        elif refunc == '3':
            print("'",name,"'",'的联系电话:',c[name])
        elif refunc == '5':
            func_sixth_exit()
        elif refunc != '4':
            print('无此功能，返回主菜单！')

    else:
        c[name]=input('联系电话:')
        print('已新建联系人',"'",name,"'",'！')
        print()


#     2.  修改联系人信息
def func_second_change(name=0):
    if len(c.keys())==0:
        print('通讯录为空！请先新建联系人！')
        print()
    else:
        if name ==0:
            name = input("名字：")
        if name in c.keys():
            c[name]=input('联系电话:')
            print("'",name,"'",'的联系电话已修改！')
            print()
        else:
            print('无此联系人！')
            rename=input(("请重新输入联系人姓名或按'*'号键返回上一层菜单："))
            if rename != '*':
                func_second_change(rename)

#     3.	删除联系人
def func_third_dele(name=0):
    if len(c.keys())==0:
        print('通讯录为空！请先新建联系人！')
        print()
    else:
        if name ==0:
            name=input('名字:')
        if name in c.keys():
            del c[name]
            print("'",name,"'",'的信息已删除！')
            print()
        else:
            print('无此联系人！')
            rename=input(("请重新输入联系人姓名或按'*'号键返回上一层菜单："))
            if rename != '*':
                func_third_dele(rename)

#     4.	查询联系人
def func_forth_find(name=0):
    if len(c.keys())==0:
        print('通讯录为空！请先新建联系人！')
        print()
    else:
        if name == 0:
            name=input('名字:')
        if name in c.keys():
            print("'",name,"'",'的手机号码：',c[name])
        else:
            print('无此联系人！')
            rename=input(("请重新输入联系人姓名或按'*'号键返回上一层菜单："))
            if rename != '*':
                func_forth_find(rename)

#     5.  显示所有联系人
def func_fifth_list():
    if len(c.keys())==0:
        print('通讯录为空！')
        print()
    else:
        print('''
        是否显示联系人电话？（输入“1”显示，否则不显示）
        ''')
        num_list=input()
        if num_list == '1':
            for i in range (len(c.keys())):
                print("'",list(c.keys())[i],"':",list(c.values())[i])
        else:
            for i in range (len(c.keys())):
                print("'",list(c.keys())[i],"'")


#     6.	退出
def func_sixth_exit():
    print('已退出通讯录！')

# 主函数
print("欢迎进入通讯录！")
while(func!='6'):
    print('''
    1.	新增联系人
    2.  修改联系人信息
    3.	删除联系人
    4.	查询联系人
    5.  显示所有联系人
    6.	退出
    ''')

    func=input()
    if func == '':
        print('未选择功能！')
    elif func =='1' :
        func_first_new()
    elif func =='2' :
        func_second_change()
    elif func =='3' :
        func_third_dele()
    elif func =='4' :
        func_forth_find()
    elif func =='5' :
        func_fifth_list()
    elif func =='6' :
        func_sixth_exit()
    else:
        print('无此功能，请重新输入！')
