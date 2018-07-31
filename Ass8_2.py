class Project:
    'Gives information about the project'

    def __init__(self, name, budget, startDate, endDate):
        # here all attirbutes are declared as private
        self.__name = name
        self.__budget = budget
        self.__startDate = startDate
        self.__endDate = endDate

    def setName(self, name):
        return self.__name

    def setBudget(self, budget):
        return self.__budget

    def setStartDate(self, startDate):
        return self.__startDate

    def setEndDate(self, endDate):
        return self.__endDate

    # defining the getters

    def getName(self):
        return self.__name

    def getBudget(self):
        return self.__budget

    def getStartDate(self):
        return self.__startDate

    def getEndDate(self):
        return self.__endDate

    # here we define get info which retruns all object information
    def getInfo(self):
        return 'Project name:' + self.__name + '  ' + 'Budget:' + str(self.__budget) + '  ' \
               + 'Start Date:' + self.__startDate + '  ' + 'End Date:' + self.__endDate

    def searchProject(self, name):
        'Searches the Project data'
        if self.__name == name:
            return self.__repr__()
        else:
             return 'Project with name: ' + name + ' was not found!'

    def updateProject(self,name,budget):
        if self.__name == name:
         self.__budget = budget
        else:
            return 'Project name does not match!'
    def compare(self, project):
        if self.__budget == project.__budget and self.__startDate == project.__startDate:
         return self.__name + ' is the same as ' + project.__name
        else:
            return self.__name + ' is not the same as ' + project.__name


    def __repr__(self):
        'returns all Project data'
        return 'Project(' +'Name:'+ self.__name + ', ' + 'Budget:'+str(
            self.__budget) + ', ' + 'Start Date:'+ self.__startDate + ', ' + 'End Date:'+self.__endDate + ')'

    def __str__(self):
        'Returns a string representatio of the object'
        return 'Name:'+ self.__name + ', ' +'Budget:'+ str(self.__budget) + ', ' + 'Start Date:'+ self.__startDate + ', ' +'End Date:'+self.__endDate
projects = [Project('Road', 5000, '20.5.2016', '31.8.2016'),Project('School',5000, '20.5.2016', '31.8.2016'),Project('Rail',2000,'3.8.2016','6.10.2016')]
index=1
for project in projects:
    print('Project'+ str(index) + ' ' + project.getInfo())
    index += 1

print(projects[1].compare(projects[2]))



