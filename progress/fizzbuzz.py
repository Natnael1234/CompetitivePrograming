class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        lst = []
        for i in range(1,n+1):
            res=''
            if i%3==0:
                res+='Fizz'
            if i%5==0:
                res+='Buzz'
            if i%3!=0 and i%5!=0:
                res+=str(i)

            lst.append(res)

        return lst
