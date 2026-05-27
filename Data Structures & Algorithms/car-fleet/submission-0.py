class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        Return the number of different car fleet
        One car is considered a car fleet
        A car fleet can be multiple cars going together, no car can get ahead
        -> Fast car matches slow car speed at that position
        If it catches up at the destination, it still counts as that car fleet

        Constraints:
        O(N^2) is possible -> O(NlogN) is also possible (sorting)
        Every car is at different positions, but speed can be the same
        Speed can be 0
        There can be 1 car

        Different cases:
        Car catches up to a fleet
        Fleet make to target

        Pattern: Stack
        Approach:
        1. Use the length of stack as a counter for fleets?
        2. If two cars intersect, merge them into one in the stack with the slowest car
        '''
        sortCar = []
        time_stk = []
        for i in range(len(position)):
            sortCar.append([position[i], speed[i]])
        
        sortCar.sort(key=lambda x: x[0], reverse=True) # descending position order
        
        for pos, speed in sortCar:
            time = (target - pos) / speed
            if time_stk and time_stk[-1] >= time:
                continue
            time_stk.append(time)
        
        return len(time_stk)