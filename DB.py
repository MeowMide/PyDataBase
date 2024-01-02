import os

class DataBase:

    def __init__(self, name):
        self.name = name + ' py_database'
        x = os.path.exists(self.name)
        if x == False:
            os.mkdir(self.name)

    def newcell(self, cellname, information):
        cell = open(f'{self.name}/{cellname}.pydb', 'w')
        cell.write(information)

    def writecell(self, cellname, information):
        cell = open(f'{self.name}/{cellname}.pydb', 'w')
        cell.write(information)

    def readcell(self, cellname):
        cell = open(f'{self.name}/{cellname}.pydb', 'r')
        return cell.read()