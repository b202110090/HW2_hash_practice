#先開檔案
f = open('hw2_data.txt')
#創一個dict
name_dict={}
#一行一行讀文件
for line in f.readlines():
    ##line_no_hang將原本txt檔案中的文字去除換行符號以後存起來
    line_no_hang=line.strip()
    ##如果沒有讀過這個單字
    if line_no_hang not in name_dict.keys():
        ###多建立一個名字進入Dict
        name_dict[line_no_hang] = 1
    ##已有單字就直接增加一次
    else:
        name_dict[line_no_hang] += 1
#關檔案
f.close
#顯示dict的狀況用
print(name_dict)
#顯示總共幾個單字用
print('總共有%d個單字'%(len(name_dict)))
#清楚輸出答案用，把key和value存成字串
list_key = list(name_dict.keys())
list_value = list(name_dict.values())
for i in range(len(list_key)):
    print('單字%s出現%d次'%(list_key[i],list_value[i]))