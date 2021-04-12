class Fighter:
    def __init__(self, name, nickname, record, height, weight, reach, stance, dob):
        self.name = name
        self.nickname = nickname
        self.record = record
        self.height = height
        self.weight = weight
        self.reach = reach
        self.stance = stance
        self.dob = dob
        self.print = ""
        self.Dict = {}

    def setPrint(self):
        if (self.nickname != 'N/A'):
            nameFormat = self.name.split()
            newName = nameFormat[0] + " \"" + self.nickname + "\" " + nameFormat[1]
            self.Print = "Name: {name} | Record: {record} | Height: {height} | Weight: {weight} | Reach: {reach} | Stance: {stance} | Date of Birth: {dob}"\
                               .format(name=newName, record=self.record, height=self.height, weight=self.weight, reach=self.reach, stance=self.stance, dob=self.dob)
        else:
            self.Print = "Name: {name} | Record: {record} | Height: {height} | Weight: {weight} | Reach: {reach} | Stance: {stance} | Date of Birth: {dob}"\
                               .format(name=self.name, record=self.record, height=self.height, weight=self.weight, reach=self.reach, stance=self.stance, dob=self.dob)
            
    def getPrint(self):
        return self.Print
    
    def setDict(self):
        if (self.nickname != 'N/A'):
            nameFormat = self.name.split()
            newName = nameFormat[0] + " \"" + self.nickname + "\" " + nameFormat[1]
            self.Dict['name'] = newName
            self.Dict['record'] = self.record
            self.Dict['height'] = self.height
            self.Dict['weight'] = self.weight
            self.Dict['reach'] = self.reach
            self.Dict['stance'] = self.stance
            self.Dict['dob'] = self.dob
        else:
            self.Dict['name'] = self.name
            self.Dict['record'] = self.record
            self.Dict['height'] = self.height
            self.Dict['weight'] = self.weight
            self.Dict['reach'] = self.reach
            self.Dict['stance'] = self.stance
            self.Dict['dob'] = self.dob

    def getDict(self):
        return self.Dict
