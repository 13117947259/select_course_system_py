# 课程类
class Course(object):

    def __init__(self, cId, cName, cProperty, cTotalTime, cTeachTime, cTrailTime, cCredit, cDate):
        # 课程编号，课程名称，课程性质，总学时，授课学时，实验或上机学时，学分，开课学期
        self.cId = cId
        self.cName = cName
        self.cProperty = cProperty
        self.cTotalTime = cTotalTime
        self.cTeachTime = cTeachTime
        self.cTrailTime = cTrailTime
        self.cCredit = cCredit
        self.cDate = cDate



