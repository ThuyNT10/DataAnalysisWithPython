# Task 1

#1.1. Tạo một chương trình Python mới có tên “lastname_firstname_grade_the_exams.py.” (Đảm bảo tệp mã nguồn của bạn nằm trong cùng thư mục với tệp dữ liệu bạn vừa tải xuống.)

#1.2. Viết một chương trình cho phép người dùng nhập tên của một tệp và truy cập đọc.
FileName=input("Please enter the file name (i.e class1.txt):") 
FolderPath=r"D:/THUY/DA/6. Ung dung hoc may trong phan tich du lieu/ASM 1/Data Files/"
FilePath=FolderPath + FileName


#1.3. Nếu tệp tồn tại, bạn có thể in ra một thông báo xác nhận. Nếu tệp không tồn tại, bạn nên cho người dùng biết rằng không thể tìm thấy tệp và nhắc lại họ.

import re
if  (int(FileName[5])>=1) and (int(FileName[5])<=8):
    print("The last character of file name is okay")
elif re.match("class"+"\d"+".txt",FileName):
    print("The file name is okay")
else:
    print("Please check file name again, it should be class*.txt (*:1-8)")    


#1.4. Sử dụng try/except để thực hiện việc này
try:
    FileOpen=open(FilePath, "r")
    print('The file name is okay, it is opened now')
except FileNotFoundError:
    print("Please check file name again, it should be class*.txt (*:1-8)")   
else:
    print(FileOpen.read())
finally:
    FileOpen.close()
    print("File is now closed")



# Task 2: Kiểm tra định dạng từng dòng trong mỗi file có đúng không
import re
import statistics
Task2=open("D:/THUY/DA/6. Ung dung hoc may trong phan tich du lieu/ASM 1/My Output/Task2.txt","w")
Task3=open("D:/THUY/DA/6. Ung dung hoc may trong phan tich du lieu/ASM 1/My Output/Task3.txt","w")
#FileNumber=[1,2,3,4,5,6,7,8]
#N=len(FileNumber)
for n in range(1,9):    #range(1,9)/range(N)  #Vòng lặp cho các file từ 1 tới 8
    WriteTask2=""    #sẽ lấy toàn bộ thông tin sau tất cả các vòng lặp, nên để ở ngay sau vòng lặp đầu tiên   
    WriteTask3=""    #sẽ lấy toàn bộ thông tin sau tất cả các vòng lặp, nên để ở ngay sau vòng lặp đầu tiên
    WriteTask4=""    #sẽ lấy toàn bộ thông tin sau tất cả các vòng lặp, nên để ở ngay sau vòng lặp đầu tiên
    GradeOfClass=[]   #list về tổng điểm các học sinh trong từng lớp #theo từng lớp, nên phải đặt sau vòng lặp của lớp
    HighGrade=0       #biến đếm số lượng SV đạt tổng điểm >80 theo từng lớp, đặt sau vòng lặp của lớp
    NumberSkip=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]   #số lượng sinh viên bỏ qua câu hỏi từ 1-25 của từng lớp
    NumberWrong=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]  #số lượng sinh viên trả lời sai câu hỏi từ 1-25 của từng lớp
    FileName="class"+str(n)+".txt"
    print("Filename: ",FileName)
    WriteTask2+="Please enter the file name (i.e class1.txt): "+str(FileName)+"\n"
    WriteTask3+="Please enter the file name (i.e class1.txt): "+str(FileName)+"\n"
    WriteTask2+="Successfully opened: "+str(FileName)+"\n"
    WriteTask3+="Successfully opened: "+str(FileName)+"\n"
    WriteTask2+="**** ANALYZING ****"+"\n"
    WriteTask3+="**** ANALYZING ****"+"\n"
    FolderPath=r"D:/THUY/DA/6. Ung dung hoc may trong phan tich du lieu/ASM 1/Data Files/"
    FilePath=FolderPath + FileName
    FileContent=open(FilePath,'r')
    LineList=FileContent.readlines()
    M=len(LineList)
    print('Total lines of data: ',M) 
          
    InvalidLines=0     #biến tính tổng các dòng dữ liệu sai
    for m in range(M):   #vòng lặp từng dòng (đáp án từng học sinh) trong từng lớp
        LineFile=LineList[m]
        LineFile=LineFile.strip()    #strip():loại bỏ khoảng trắng ở đầu và cuối chuỗi, nếu ko thì giá trị cuối của từng LineFile sẽ là:"W\n": tính điểm ko cho kq đúng 
        LineFile=LineFile.split(",")
        print(LineFile)
           
        if len(LineFile)!=26:
           print('Invalid line of data: does not contain exactly 26 values:\n',LineList[m])
           InvalidLines+=1
           WriteTask2+='Invalid line of data: does not contain exactly 26 values:\n'+str(LineList[m])+'\n'               
           WriteTask3+='Invalid line of data: does not contain exactly 26 values:\n'+str(LineList[m])+'\n'

        elif not re.match("N"+"\d{8}",LineFile[0]):   #dùng elif vì nếu 1 dòng sai ở 2 lỗi thì vẫn chỉ được tính 1 lần
           print('Invalid line of data: N# is invalid:\n',LineList[m])  
           InvalidLines+=1
           WriteTask2+='Invalid line of data: N# is invalid:\n'+str(LineList[m])+'\n'   
           WriteTask3+='Invalid line of data: N# is invalid:\n'+str(LineList[m])+'\n'
        
           
#Task 3: Tính điểm từng sinh viên theo từng lớp, làm các thống kê: 
        Answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
        ANSWER=Answer_key.split(",")
        #print('ANSWER:',ANSWER)
        TotalGrade=[]
        K=len(ANSWER)
           
        for k in range(K):    #vòng lặp các câu hỏi từ 1-25 #range(0,25)
            if (len(LineFile)==26) and (re.match("N"+"\d{8}",LineFile[0])) and (LineFile[k+1]==ANSWER[k]):
                TotalGrade.append(4)  
            elif (len(LineFile)==26) and (re.match("N"+"\d{8}",LineFile[0])) and (LineFile[k+1]!=ANSWER[k]) and (len(LineFile[k+1])==1):
                TotalGrade.append(-1)
                NumberWrong[k]+=1
            elif (len(LineFile)==26) and (re.match("N"+"\d{8}",LineFile[0])) and ((LineFile[k+1])==""):
                TotalGrade.append(0)
                NumberSkip[k]+=1
           
        if sum(TotalGrade)>80:
            HighGrade+=1
                
        print('TotalGrade:',TotalGrade)
        print('Total grade of student',LineList[m][0:9],': ',sum(TotalGrade))

        if (len(LineFile)==26) and (re.match("N"+"\d{8}",LineFile[0])):    #chỉ in những sinh viên có dữ liệu đúng
            WriteTask4+='Total grade of student '+str(LineList[m][0:9])+', '+str(sum(TotalGrade))+'\n'   #liên quan tới vòng lặp M nên để trong vòng lặp M, cùng hàng vòng lặp K    
               
        if sum(TotalGrade)>0:
            GradeOfClass.append(sum(TotalGrade))
                   
    print('Grade of Class '+str(n)+' :',GradeOfClass)

    if InvalidLines==0:
        WriteTask2+="No errors found!"+'\n'
        WriteTask3+="No errors found!"+'\n'
      
    WriteTask2+="**** REPORT ****"+"\n"
    WriteTask3+="**** REPORT ****"+"\n"
            
    print('Total valid lines of data: ',M - InvalidLines) 
    print('Total invalid lines of data: ',InvalidLines)   # đặt thẳng hàng với InvalidLines, là kết quả sau vòng lặp M,K                   
    
    print('Number of skip answer: ',NumberSkip)  #list về số lần bỏ qua các câu hỏi từ 1-25 của từng lớp
    print('Number of wrong answer: ',NumberWrong)   #list về số lần trả lời sai các câu hỏi từ 1-25 của từng lớp

    WriteTask2+='Total valid lines of data: '+str(M - InvalidLines)+'\n'
    WriteTask3+='Total valid lines of data: '+str(M - InvalidLines)+'\n'
    WriteTask2+='Total invalid lines of data: '+str(InvalidLines)+'\n'
    WriteTask3+='Total invalid lines of data: '+str(InvalidLines)+'\n'
    WriteTask2+="                                                                                 "+'\n'
    WriteTask2+="================================================================================="+'\n'
    WriteTask2+="                                                                                 "+'\n'
    WriteTask3+="**** STATISTICS ****"+"\n"
    
    a=max(NumberSkip)      #bài yêu cầu in ra tất cả các giá trị max, nên cần câu lệnh này
    b=[(i+1,j) for i,j in enumerate(NumberSkip) if j==a]
    x=""
    for i in b:  # i này là xét từng tuple trong list b, ko phải i ở trên
        x+=str(i[0])+"-"+str(i[1])+"-"+str(round(a/(M-InvalidLines),2))+"; "
       

    c=max(NumberWrong)     #bài yêu cầu in ra tất cả các giá trị max, nên cần câu lệnh này
    d=[(i+1,j) for i,j in enumerate(NumberWrong) if j==c]
    y=""
    for i in d:  # i này là xét từng tuple trong list d, ko phải i ở trên
        y+=str(i[0])+"-"+str(i[1])+"-"+str(round(c/(M-InvalidLines),2))+"; "


    WriteTask3+='Number of students with total grade > 80: '+str(HighGrade)+'\n'
    WriteTask3+='Mean (average) score: '+str(round(statistics.mean(GradeOfClass),2))+'\n'
    WriteTask3+='Highest score: '+str(max(GradeOfClass))+'\n'
    WriteTask3+='Lowest score: '+str(min(GradeOfClass))+'\n'
    WriteTask3+='Range of score: '+str(max(GradeOfClass) - min(GradeOfClass))+'\n'
    WriteTask3+='Median score: '+str(statistics.median(GradeOfClass))+'\n'
    WriteTask3+='Question that most people skip (Question No-Max number people-Skipped rate): '+x+'\n'
    WriteTask3+='Question that most people answer incorrectly (Question No-Max number people-Incorrect rate): '+y+'\n'
    
    WriteTask3+="                                                                                                                     "+'\n'
    WriteTask3+="====================================================================================================================="+'\n'
    WriteTask3+="                                                                                                                     "+'\n'
    
    
    Task2.write(WriteTask2)
    Task3.write(WriteTask3)
    

# Task 4: in kết quả tổng điểm của các sinh viên theo từng lớp ra từng file txt riêng biệt
    Task4=open("D:/THUY/DA/6. Ung dung hoc may trong phan tich du lieu/ASM 1/My Output/Task4/"+FileName[0:6]+"Grade.txt","w") #Task 4 ko đặt open ngay trên đầu bài như Task 2, Task 3 vì nó liên quan FileName, nên sẽ đặt sau FileName
    Task4.write(WriteTask4)
