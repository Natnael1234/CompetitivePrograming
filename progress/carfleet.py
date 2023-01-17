class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for i in range(len(position)):
            dis = target - position[i]
            time = dis/speed[i] 
            cars.append((position[i],time))
        cars.sort(key = lambda x: x[0]) 
        print (cars)
        cars.reverse() 
        print (cars)
        st = []
        for i in range(len(cars)):
            if len(st) == 0:
                st.append(cars[i])
                print (st)
            else:
                if st[-1][1] >= cars[i][1]:
                    continue
                else:
                    st.append(cars[i])
        return len(st)
