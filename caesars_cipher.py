def cipher_en(string,shift):
   hash = {
   'a':'1','b':'2','c':'3','d':'4','e':'5','f':'6','g':'7',
   'h':'8','i':'9','j':'10','k':'11','l':'12','m':'13','n':'14',
   'o':'15','p':'16','q':'17','r':'18','s':'19','t':'20','u':'21',
   'v':'22','w':'23','x':'24','y':'25','z':'26',
   }
   ans = []
   nums = []
   string = list(string)
   print(string)
   # print(string.replace(' ','')
   for x in string:
       for key, value in hash.items():
           num = hash[x]
           num = int(num)
           shift = int(shift)
           shifting = num + shift
       nums.append(shifting)
   print(nums) # nums has the values
   num_1 = [ str(item) for item in nums]
   hash_1 = {y:x for x,y in hash.items()} # second hash
   for n in num_1: # converting the values into the key
       for key, value in hash_1.items():
           alpha = hash_1[n]
       ans.append(alpha)
       ans = " ".join(ans)
       print(ans)
 ### decrypt
   for key, value in hash_1.items():
     for n in ans:
         if n in hash:
             output.append(hash_1[n])
         else:
             output.append(n)
     output = " ".join(ans)
     return output
#inputs
string = input()
string = str(string)
shift = input()
shift = str(shift)
print(cipher_en(string, shift)) # calling function
