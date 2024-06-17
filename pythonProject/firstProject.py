class House:

    def __init__(self,wall_area):
        self.wall_area = wall_area

    def paint_needed(self):
        return  self.wall_area*2.5  #per 1sq feet 2.5 paint is used

class Paint:

    def __init__(self,bucket,color):
        self.bucket=bucket
        self.color = color
    def cal_total_price(self):
        if self.color == 'white':
            return self.bucket*1.98
        else:
            return self.bucket*2.13
