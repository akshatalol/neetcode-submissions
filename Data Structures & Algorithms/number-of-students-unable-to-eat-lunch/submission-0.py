class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        circle=0
        square=0
        counter=0
        for i in students:
            if i==0:
                circle+=1
            else:
                square+=1
        for i in sandwiches:
            if i==0:
                if circle==0:
                    break
                else:
                    circle-=1
            else:
                if square==0:
                    break
                else:
                    square-=1
        return (circle+square)
         
        