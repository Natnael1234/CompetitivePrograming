class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        list1 = list()
        if(len(changed)%2==0):
            changed.sort()
            cnt = Counter(changed)
            for i in changed:
                if (cnt[i]==0):
                    continue
                else:
                    if(cnt.get(2*i,0)>=1):
                        list1.append(i)
                        cnt[2*i]-=1
                        cnt[i]-=1
                    else:
                        return([])
            return(list1)
        else:
            return([])
