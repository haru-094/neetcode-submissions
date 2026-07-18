class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        ones = sum(students)
        zeros = len(students) - ones 

        n = len(students)

        for i in sandwiches:
            if (n == zeros  and ones == 0 and i ==1):
                return zeros

            if (n == ones  and zeros == 0 and i ==0):
                return ones
                
            if i and ones > 0:
                ones -=1
            if not i and zeros > 0:
                zeros -=1
            n -=1

        return 0

