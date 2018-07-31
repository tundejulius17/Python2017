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

    # here we define get info which returns all object information


    def searchProject(self, name):
        'Searches the Project data'
        if self.__name == name:
            return self.__repr__()
        else:
             return 'Project with name: ' + name + ' was not found!'

    def updateProject(self,name,budget):
        if self.__name == name:
         self.__budget = budget

    def __repr__(self):
        'returns all Project data'
        return 'Project(' +'Name:'+ self.__name + ', ' + 'Budget:'+str(
            self.__budget) + ', ' + 'Start Date:'+ self.__startDate + ', ' + 'End Date:'+self.__endDate + ')'

    def __str__(self):
        'Returns a strng representation of the object'
        return 'Name:'+ self.__name + ', ' +'Budget:'+ str(self.__budget) + ', ' + 'Start Date:'+ self.__startDate + ', ' +'End Date:'+self.__endDate

project1 = Project('Road', 5000, '20.5.2016', '31.8.2016')
project2 = Project('School',7000, '1.4.2016', '31.8.2016')
print(project1)
print(project1.searchProject('Road'))
project1_repr = repr(project1)
print('project_repr '+ project1_repr)
print('After updating project')
# make a copy of it and then update
project1_copy = project1
project1_copy.updateProject('Road',24000)
print(project1_copy)
project2.updateProject('School',10000)
print('Porject2 after updating budget: ' + str(project2))
print(project2)
print(project1)

