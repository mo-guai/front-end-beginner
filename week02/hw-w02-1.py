# 要求一:函式與流程控制
# 完成以下函式，在函式中使用迴圈計算最小值到最大值之間，固定間隔的整數總和。
# 其中你可以假設 max 一定大於 min 且為整數，step 為正整數。



def calculate(min, max, step): 
# 請用你的程式補完這個函式的區塊
#解題重點：Python range() Function

    sum = 0 
    for x in range(min, max + 1, step):
        # print("這時候的x是",x)
        sum += x
    print(sum)

calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6 
calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18 
calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0


# 要求二:Python 字典與列表、JavaScript 物件與陣列
# 完成以下函式，正確計算出非 manager 的員工平均薪資，所謂非 manager 就是在資料中 manager 欄位標註為 False (Python) 或 false (JavaScript) 的員工，程式需考慮員工資料數量 不定的情況。

def avg(data):
    # 請用你的程式補完這個函式的區塊
    length = len(data["employees"])  #抓取employees對應的陣列長度
    sumSalary=0
    notManager=0
    
    # print(data["employees"]) #測試印出data被放入的內容
    
    for n in range(0,length):
        if data["employees"][n]["manager"]==False:
            # print("這時候的n是",n)
            notManager+=1
            sumSalary+= data["employees"][n]["salary"]
    
    print(sumSalary/notManager)
            
            
        
#分析 字典{employees:[{},{},{},{}]}  只有一個配對
#employees 是個陣列 陣列內有四個 字典
#字典內陣列內容判斷
avg({ 
    "employees": [
        {
            "name": "John",
            "salary": 30000,
            "manager": False
        },
        {
            "name": "Bob",
            "salary": 60000,
            "manager": True
        },
        {
            "name": "Jenny",
            "salary": 50000,
            "manager": False
        },
        {
            "name": "Tony",
            "salary": 40000,
            "manager": False
        }
    ]
})  # 呼叫 avg 函式

#要求三 
#完成以下函式，最後能印出程式中註解所描述的結果。

def func(a):
# 請用你的程式補完這個函式的區塊
    def multiply(n1, n2):
        print(a + (n1*n2))
    return multiply

func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14 
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0 
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15 
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果


# 要求四:
# 找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。 
# 提醒:請勿更動題目中任何已經寫好的程式，不可以使用排序相關的內建函式。

def maxProduct(nums):
# 請用你的程式補完這個函式的區塊 #key:練習寫九九乘法表搞清楚雙重回圈
    length=len(nums)  #取得陣列長度
    newArr = []
    multiply_nums=0
    max_num=0
    
    for x in range(0,length):
        # print("這時的x是",x)
        for y in range(0,length):
            # print("這時的x是",x)
            # print("這時的y是",y)
            if nums[x] != nums[y]: #避免自己乘自己
                multiply_nums = nums[x] * nums[y]
                # print("這時的multiply_nums是",multiply_nums)
                newArr.append(multiply_nums)  
                #Python List append() Method  將相乘後的數字，加入新陣列
    max_num=max(newArr)
     
    print(max_num)  #取陣列中的最大值 Python max() Function
                
maxProduct([5, 20, 2, 6])  # 得到 120
maxProduct([10, -20, 0, 3])  # 得到 30
maxProduct([10, -20, 0, -3])  # 得到 60
maxProduct([-1, 2])  # 得到 -2
maxProduct([-1, 0, 2])  # 得到 0
maxProduct([5, -1, -2, 0])  # 得到 2
maxProduct([-5, -2])  # 得到 10


# 要求五:
# WeHelp
# Assignment - Week 2
#  Given an array of integers, show indices of the two numbers such that they add up to a specific target. You can assume that each input would have exactly one solution, and you can not use the same element twice.

def twoSum(nums, target):
# your code here
    length=len(nums)
    for x in range(0,length):
        for y in range(0,length):
            if nums[x]+nums[y]==target:
               return [x,y]
           
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9




# 要求六 ( Optional ):
# 給定只會包含 0 或 1 兩種數字的列表 (Python) 或陣列 (JavaScript)，計算連續出現 0 的最大長度。

def maxZeros(nums):
# 請用你的程式補完這個函式的區塊 
    zeroArr=[]
    zeroCount=0
    maxCount=0
    for x in range(len(nums)): #range(起始值, 終點值, 間隔值) ＝ range(終點值)
        if nums[x]==0:
            zeroCount+=1
            zeroArr.append(zeroCount) #Python List append() Method  將加入新陣列
            
        else:
            zeroCount=0
            zeroArr.append(zeroCount)
            
    # maxCount=max(zeroArr) #取List中最大值 ！！！沒必要存到變數裡（多餘的程式碼）！
    print(max(zeroArr))            
    
maxZeros([0,1,0,0])  # 得到 2
maxZeros([1,0,0,0,0,1,0,1,0,0])  # 得到 4
maxZeros([1,1,1,1,1])  # 得到 0
maxZeros([0,0,0,1,1])  # 得到 3



