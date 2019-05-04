I have learned from this project:

ctrl +4 Spyder注释快捷键

f = open('cdays-4-test.txt', 'r')                   #以读方式打开文件
result = list()
for line in f.readlines():                          #依次读取每行
    line = line.strip()                             #去掉每行头尾空白
    if not len(line) or line.startswith('#'):       #判断是否是空行或注释行
        continue                                    #是的话，跳过不处理
    result.append(line)                             #保存
result.sort()                                       #排序结果
print result
open('cdays-4-result.txt', 'w').write('%s' % '\n'.join(result)) #保存入结果文件


1. Read a file ----Line70
    *Open file
          FILE_NAME = "InputFile7.txt"
       1. with open(FILE_NAME,"r") as f:
            all lines under should indent:select "ctrl+]",or it gives alert: I/O closed
       2.with open(FILE_NAME) as f:
            NO INDENT need
       
    *Readline and Readlines
        f.readline()   #means the pointer move to the first line of the text
        p = float(f.readline())  #means the pointer move to the 2nd line 
                                  and assign the value to p
        f.readline() #pointer keep moving on 
         !!!!! if it is blank line, will skip and pointer to the next

        int(p) for p in f.readline()[1: -1].split(',') 
            #[1:-1] means extract the substring，remove bracket
            split() method returns a list of strings after breaking the given string by the specified separator.
            int(p) is change the p type from string to int. For split makes it to be string list ['2','3','1','1'] instead of [2,3,1,1]
   
   *close file
      "f.close()"
      put this line when all the f.readline() end. 

2.Create a 3*3 all-zeros(float type)matrix 

   trans_matrix = [[0.0]*3 for i in range(3)]
