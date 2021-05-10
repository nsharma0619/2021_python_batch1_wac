# def checkodd(n):
#     if n%2!=0:
#         return True
#     return False


# result1 = checkodd(55)
# result2 = checkodd(104)
# print(result1, result2)

# power(a, b) a^b

# def power(a, b):
#     return a**b

# result = power(5,4)
# print(result)


# def isprime(n):
#     for i in range(2, n//2):
#         if n%i==0:
#             return False
#     return True

# print(type(isprime(10)))

# def factorial(n):
#     ans = 1
#     for i in range(1, n+1):
#         ans*=i
#     return ans

# print(factorial(1200))

# lis = [5,6,8,9]
# print(sum(lis))

q = int(input())
i=1
while (i<=q):
     n = int(input())
     a=1
     pf_max=0
     while (a<=n):
          k = 1
          pf=0
          while (k<=a):
               if(a%k==0):
                    c=0
                    j=1
                    for j in range (1, k+1):
                         if (k%j==0):
                              c=c+1

                    if (c==2):
                         pf=pf+1

               k=k+1

          if (pf>=pf_max):
               pf_max = pf 
          a=a+1
     
     print(pf_max)
     i+=1

