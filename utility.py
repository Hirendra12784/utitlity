#importing pandas for reading of csv file
import pandas as pd
class Solution:
    def __init__(self):
        self.data=pd.read_csv("C:/Users/DELL/Downloads/book.csv")  # reading csv file
        print(self.data)

    def cal_mean(self,cll):       # for calculating mean of specific column
        D_Mean=self.data[cll].mean()
        return D_Mean

    def cal_median(self,cll):           # for calculating median of specific column
        D_median=self.data[cll].median()
        return D_median

    def speci_val(self,val, cl):        # for filtering records matching with  specific column
        return self.data.loc[self.data[cl] ==val]     
  
    def particular_range(self,val, cl):        # for filtering records matching with  specific column in a range
        n=[float(val)-(5/100)*float(val),float(val)+(5/100)*float(val)]
        return self.data.loc[self.data[cl] <n[1]] [self.data[cl] >n[0]]

    def change_specific(self, cl):             # for calculating change in  specific column
        self.data["new"]=abs(self.data[cl]-self.cal_mean(cl))
        return self.data["new"]

    def average(self):          # calculating average
        print("inside")
    #Average_change=sum(self.data["new"])/len(self.data["new"])
        if "new" in self.data:                   # if data change column is availavble then calculate average of change in that column 
            Average_change= self.cal_mean("new")
            return Average_change
        else: 
            return "no changes detected"
  
    def Min(self):                        # calculating Minimum
        if "new" in self.data:                  # if data change column is availavble then calculate Minimum of change in that column
            Minimum_change=min(self.data["new"])
            return Minimum_change
        else: 
            return "no changes detected"

   
    def Max(self):                        # calculating Maximum
        if "new" in self.data:                # if data change column is availavble then calculate Maximum of change in that column
            print("inside")
            Maximum_change=max(self.data["new"])
            return Maximum_change
        else: 
            return "no changes detected"
  
 # def printdata(self):
  #  print(self.data.head())

obj = Solution()
flag=True
while flag:
    print("The Following are the features available:")
    print("1.Mean of a specific column\n" "2.Median of a specific column\n" "3.Filter all records\n" "4.Filter in Range\n" "5.changes in         value\n" "6 av change \n" "7 min change\n" "8 max change\n")
    a=input("enter your options:")
    print("You have chosen :" +a)
    a = int(a)
# choosing specific values and then comparing
    if a == 1:            #case 1 -> calculating mean for specific column
        x=input("Enter specific column :")
        print("Mean: ", obj.cal_mean(x))
   
    elif a==2:           #case 2 -> calculating median for specific column
        x=input("Enter specific column :")
    # obj.cal_median(x)
        print("Mean: ", obj.cal_median(x))
   
    elif a==3:            #case 3 -> filtering particular value by column and its name 
        x=input("Enter specific value :")
        cl = input("Enter specific column:")
        print("Speci value\n", obj.speci_val(int(x), cl))

    elif a==4:                #case 4 -> filtering particular value by column and its name in a range
        cl=input("Enter specific column :")
        val=input("Enter specific value :")
        print("Range\n", obj.particular_range(int(val), cl))

    elif a==5:                #case 5-> calculating changes in value by specific column
        x=input("Enter specific column :")
        print("change\n", obj.change_specific(x))
    # print(obj.printdata())
        a = input(" Calculate Further !!!! \n 6 Average change: \n 7 MIN change: \n 8 MAX change: \n")
        a = int(a)

        if a == 6:                       # changes values present then calculating average ,minimum and maximum
            print("Average: ", obj.average()) 

        elif a==7:
            print("MIN change: ", obj.Min())

        elif a==8:
            print("MAX change: ", obj.Max())

        else:
            print("There is no such value")

    op=input("Do you want to continue further? \n 1. continue \n 2. exit \n")
    if op=="1":
        flag=True
    else:
        flag=False
