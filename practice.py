# word="python"
# for i in range(len(word)-1 , -1 , -1):
#     print(word[i])
# vowels="a,e,i,o,u"
# a="education"
# count=0

# for char in a:
#     if char in vowels:
#         count+= 1
#     print(f"the vowels in {a} is {count}"
# a=0
# b=1

# for _ in range(8):  
#     next_value=a+b
#     print(next_value)
#     a,b=b,next_value

#printing a factorial of  a number
# num=int(input())
# factorial=1
# for i in range(1, num+1):
#     factorial=factorial*i
#     print("fact=",factorial)

# word="Aniket"
# char_count=[]
# for i in word:
#     if i in char_count:
#         char_count[i]=char_count+1
# else:
#     char_count[i]=1
# print(f"the characters in {word} is {char_count}")
word="hippopotamous"
letter=str(input())
count=0
for i in word:
    if i in letter:
        count+=1
    print(f"{letter} appears {count} times")


