
class solve:
    
    # TwoSum
    def TwoSum(self):
        arr = [1, 2, 3, 4, 5, 6]
        print(arr)
        target = int(input('Enter target: '))
        
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j:
                    if arr[i] + arr[j] == target:
                        print([i], [j])   


    # Palindrome_Letters
    def Pal_Letters(self):
        letters = str(input("Enter word: "))
        reverse_letters = ""
        
        for i in range(len(letters)):
            reverse_letters += letters[len(letters) - i - 1]
            
        if letters == reverse_letters:
            print(f"{letters}: True")
        else:
            print(f"{letters}: False")
            
    
    # Remove_Duplicates
    def remove_Dup(self):
        arr = [0,0,1,1,1,2,2,3,3,4]
        
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j:
                    if arr[i] == arr[j]:
                        arr[j] = "_"

        arr2 = []        
        for i in range(len(arr)):
            if arr[i] != "_":
                arr2.append(arr[i])                
                        
        print(f"Befor: {arr}")
        print(f"After: {arr2}")

 
 
   
solved = solve()
solved.choice()