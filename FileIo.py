# luke Reed 


print("Welcome to the test profiler.")
print("This program will read your test results from an input data file.")
print("It will produce a count of the A's, B's, etc., along with the")
print("test average and the highest and lowest grades in the set.")
#reading in users txt
file_Name = input("Please enter the name of the input data file: ")

studentFile = open(file_Name , "r")
studentList = []
for eachLine in studentFile:
   #reading txt file into list
    x = eachLine.strip()
    studentList.append(x)
#converting list of strings to ints so that sum function can be used
for i in range(0, len(studentList)): 
    studentList[i] = int(studentList[i])

sm = sum(studentList[0:len(studentList)])
Length = len(studentList)
#processing the data
def AVG(sm, Length):
    avg = sm / Length
    return avg;

avg = AVG(sm, Length)
maximum = max(studentList)
minimum =  min(studentList)

a=0
b=0
c=0
d=0
f=0

for i in range(0, len(studentList)):
    if studentList[i] < 100 and studentList[i] >= 90:
        a = a + 1
        
    elif studentList[i] < 90 and studentList[i] >= 80:
        b = b + 1
       
    elif studentList[i] < 80 and studentList[i] >= 70:
        c = c + 1
     
    elif studentList[i] < 70 and studentList[i] >= 60:
        d = d + 1
      
    elif studentList[i] < 60 and studentList[i] >= 0:
        f = f + 1

studentFile.close()

file_Out = input("Please enter the name of the output data file: ")

student_fileout = open(file_Out, "w")

student_fileout.write("--------------------Test Profile-------------------- \n")
student_fileout.write("There were ")
student_fileout.write("{}".format(Length))
student_fileout.write(" test grades read from the input file.\n")
student_fileout.write("The average is {:.2f}\n" .format(avg))

student_fileout.write("The highest grade is {}\n" .format(maximum))
student_fileout.write("The lowest grade is {}\n" .format(minimum))

student_fileout.write("The total of each grade type is as follows: \n") 
student_fileout.write("A: {}\n" .format(a)) 
student_fileout.write("B: {}\n" .format(b)) 
student_fileout.write("C: {}\n" .format(c)) 
student_fileout.write("D: {}\n" .format(d))
student_fileout.write("F: {}\n" .format(f)) 

student_fileout.close()

print("Report Complete - stored in file: {}".format(file_Out))
print("Exiting Program 3")



