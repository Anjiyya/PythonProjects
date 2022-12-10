'''
    This is a project made by students of lovely professional university: Akula Anjiyya, Gudla Srikanth,Mahammad Umar Farooq .
    Project is used to  make a basket and arrange the eggs in it  in such a way that the sum of each row,column and diagnol is equal.
    We used some of the in built functions and logics to built this code .'''
def Odd_Order(n):
    '''Creating a matrix of n order with all entries as "0"
    where the variable "c" is the number of columns and
    the variable r is the number of rows'''
    matrix=[ [0 for c in range(n)]
             for r in range(n)]
    
#Applying the first condition to check that n is Even or Odd or "0"

     # if "n" is  an odd integer

                #Starting from the first position after verifying it's Odd 

    r=n//2
    c=n-1
    i=1 
    limit=n**2
        
        #here limit is the range of eggs that we can arrange in the basket

    while i<=limit:
        if r==-1 and c==n: # Condition if both the rows and columns are out of range 
            r=0
            c=n-2
        else:
                
            if r<0: #Condition if rows are out of range
                r=n-1
                    
            if c==n: #Condition if column out of range
                c=0
                    
        if matrix[r][c]: # Starting to arrange
            c=c-2
            r=r+1
            continue
            
        else: #Condition if the before condition becomes False
            matrix[r][c]=i
                
            i+=1 #Increment of the " i " value
                
        c+=1 #Increment of column
            
        r-=1 # Decrement of rows to skip to another value

        '''Printing the number of Rows '''
    print ("basket for n =", n)
        
        #Print the sum of each row and column of n order matrix
        
    print ("Sum of each row or column",n * (n * n + 1) / 2, "\n")
        
    '''Printing the Basket '''

    print("Basket with arrangement of EGGS is : ")
        
        #Used Nested list
    for r in range(0,n):
        for c in range(0,n):
            print("%2d"%(matrix[r][c]),end="    ")
                        # To display output  
                        # in matrix form 
            if c==n-1:
                print()
        
def Even_Order(n):
    '''Creating a matrix of n order with all "0" entries
where the varaiable "c" is the columns and variable "r" is the rows'''
    matrix=[ [(n*r)+c+1 for c in range(n)] for r in range(n)]
    
        
        #Condition to change the zero elements is (n*n+1)-matrix[r][c]
        # Starting with Top left corner 
    for r in range(n//4): #setting a range to rows
            
        for c in range(n//4): #setting a range to column
                
            matrix[r][c]=(n*n-1)-matrix[r][c]; 

        # Moving to Top right corner 

    for r in range(n//4):

        for c in range(3*(n//4),n):

            matrix[r][c]=(n*n+1)-matrix[r][c];

        # Moving Bottom Left corner

    for r in range(3*(n//4),n):

        for c in range(0,n//4):

            matrix[r][c]=(n*n+1)-matrix[r][c];

        #Moving to Bottom Right corner 

    for r in range(3*(n//4),n):

        for c in range(3*(n//4),n):

            matrix[r][c]=(n*n-1)-matrix[r][c];

        #Center of matrix,order(n/2)*(n/2)

    for r in range(n//4,3*(n//4)):

        for c in range(n//4,3*(n//4)):

            matrix[r][c]=(n*n-1)-matrix[r][c];



    print ("basket for n =", n) #Prints the number of Order

    print ("Sum of each row or column",n * (n * n + 1) / 2, "\n") # Prints the sum of each row and column

#Printing the Basket

    print("Basket with arrangement of EGGS is : ")

    for r in range(n):

        for c in range(n):

            print("%2d"%(matrix[r][c]),end="    ")

        print()
#Taking input of the order 
n=int(input("Enter the number of Rows and Columns : "))

if n%2==0:#condition if "n" is an Even number 
# 
    Even_Order(n)

elif n<=0: # Condition when the input of "n" is less than zero or equal to zero

        print("Enter the positve numbers for result")

else: # Condition if "n" is an Odd number

    Odd_Order(n)
        
    
    
    

