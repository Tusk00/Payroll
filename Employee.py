class Payable:
    def calcPay(self):
        return 0.0
#####################################################
class Employee(Payable):
    __nextID = 1

    def __init__(self, firstName, lastName, hireDate, benefits):
        self.__employeeID = Employee.__nextID
        Employee.__nextID += 1
        self.__firstName = firstName
        self.__lastName = lastName
        self.__hireDate = hireDate
        self.__benefits = benefits

    def getId(self):
        return self.__employeeID

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getHireDate(self):
        return self.__hireDate

    def setFirstName(self, name):
        self.__firstName = name

    def setLastName(self, name):
        self.__lastName = name

    def getBenefits(self):
        return self.__benefits
    
    def setBenesits(self, benefits):
        self.__benefits = benefits

    def __str__(self):
        output = "Employee Name: " + self.__firstName + " " + self.__lastName + "\n"
        output += "Employee ID: " + str(self.__employeeID) + "\n"
        output += "Hire Date: " + self.__hireDate + "\n"
        output += self.__benefits.__str__()
        return output

    def calcPay(self):
        return 0.0
#####################################################
class Invoice(Payable):
    def __init__(self, productName, quantity, price):
        self.__productName = productName
        self.__quantity = quantity
        self.__pricePerItem = price
    
    def calcPay(self):
        return self.__quantity * self.__pricePerItem

    def __str__(self):
        strPrice = "${:.2f}".format(self.__pricePerItem)
        strCalcPay = "${:.2f}".format(self.calcPay())
        output = self.__productName + " x " + str(self.__quantity)
        output += " each @ " + strPrice + " = " + strCalcPay
        return output
#####################################################
class Benefits:
    def __init__(self):
        self.__lifeInsAmount = 0.0
        self.__healthInsCo = "Unspecified"
        self.__dependents = 0

    def getLifeInsAmount(self):
        return self.__lifeInsAmount
    
    def setLifeInsAmount(self, amount):
        if amount >= 0:
            self.__lifeInsAmount = amount

    def getHealthInsCo(self):
        return self.__HealthInsCo
    
    def setHealthInsCo(self, insuranceCo):
        self.__healthInsCo = insuranceCo

    def getDependents(self):
        return self.__dependents

    def setDependents(self, dep):
        if dep >= 0:
            self.__dependents = dep

    def __str__(self):
        strLifeAmt = "${:.2f}".format(self.__lifeInsAmount)
        output = "Life insurance amount: " + strLifeAmt + "\n"
        output += "Health insurance company: " + self.__healthInsCo + "\n"
        output += "Dependents: " + str(self.__dependents) + "\n"
        return output
#####################################################
class WorkGroup:
    def __init__(self):
        self.__groupName = "Unnamed Work Group"
        self.__employees = []
        self.__supervisor = None

    def setGroupName(self, name):
        self.__groupName = name

    def getGroupName(self):
        return self.__groupName

    def addEmployee(self, employee):
        self.__employees.append(employee)

    def setSupervisor(self, supervisor):
        self.__supervisor = supervisor
        s = self.getEmployee(supervisor.getId())
        if s is None:
            self.addEmployee(supervisor)

    def getSupervisor(self):
        return self.__supervisor

    def getEmployee(self,employeeID):
        for e in self.__employees:
            if e.getId() == employeeID:
                return e
            return None

    def count(self):
        return len(self.__employees)

    def remove(self, employeeID):
        e = self.getEmployee(employeeID)
        if e is not None:
            self.__employee.remove(e)

    def getEmployeeList(self):
        return self.__employees

    def __str__(self):
        output = "WorkGroup: " + self.__groupName + "\n"
        output += "Supervisor: " + self.__supervisor.getLastName()
        output += ", " + self.__supervisor.getFirstName() + "\n"
        output += "WorkGroup Members:\n"
        for e in self.__employees:
            output += "\t" + e.getFirstName() + " " + e.getLastName()
            output += " (ID: " + str(e.getId()) + ")\n\n"
        return output
#####################################################
class SalariedEmployee(Employee):
    def __init__(self, firstName, lastName, hireDate, benefits, salary):
        super().__init__(firstName, lastName, hireDate, benefits)
        self.__annualSalary = salary

    def __str__(self):
        strSalary = "${:.2f}".format(self.__annualSalary)
        strPay = "${:.2f}".format(self.calcPay())
        output = super().__str__()
        output += "Annual Salary: " + strSalary + "\n"
        output += "Current Pay: " + strPay + "\n"
        return output

    def calcPay(self):
        return self.__annualSalary / 26

#####################################################
class HourlyEmployee(Employee):
    def __init__(self, firstName, lastName, hireDate, benefits, hours, rate):
        super().__init__(firstName, lastName, hireDate, benefits)
        self.__hoursWorked = hours
        self.__payRate = rate

    def __str__(self):
        strRate = "${:.2f}".format(self.__payRate)
        strPay = "${:.2f}".format(self.calcPay())
        output = super().__str__()
        output += "Hours Worked: " + str(self.__hoursWorked) + "\n"
        output += "Pay Rate: " + strRate + "\n"
        output += "Current Pay: " + strPay + "\n"
        return output

    def calcPay(self):
        return self.__hoursWorked * self.__payRate
#####################################################
class CommissionEmployee(Employee):
    def __init__(self, firstName, lastName, hireDate, benefits, sales, pct):
        super().__init__(firstName, lastName, hireDate, benefits)
        self.__salesAmt = sales
        self.__commissionPct = pct

    def __str__(self):
        strSales = "${:.2f}".format(self.__salesAmt)
        strPct = "{:.2f}%".format(self.__commissionPct * 100)
        strPay = "${:.2f}".format(self.calcPay())
        output = super().__str__() 
        output += "Sales: " + strSales + "\n"
        output += "Commission Percent: " + strPct + "\n"
        output += "Current Pay: " + strPay + "\n"
        return output

    def calcPay(self):
        return self.__salesAmt * self.__commissionPct
#####################################################
def main():
    b1 = Benefits()
    b1.setDependents(0)
    b1.setHealthInsCo("SpaceX Health Insurance")
    b1.setLifeInsAmount(35000.00)

    b2 = Benefits()
    b2.setDependents(7)
    b2.setHealthInsCo("SpaceX Health Insurance")
    b2.setLifeInsAmount(1000000.00)

    b3 = Benefits()

    e1 = SalariedEmployee("Joey", "Battista", "05/15/2021", b1, 200000)
    e2 = HourlyEmployee("Elon", "Musk", "04/14/2021", b2 , 80, 75)
    e3 = CommissionEmployee("Jeff", "Bezos", "04/29/2021", b3, 100000, 0.2)

    group = WorkGroup()
    group.setGroupName("Engineers")
    group.setSupervisor(e2)
    group.addEmployee(e1)
    group.addEmployee(e3)

    print(group)
    i1 = Invoice("SN15", 1, 70000000)
    i2 = Invoice("Flamethrower", 5, 200)

    empList = group.getEmployeeList()

    empList.append(i1)
    empList.append(i2)

    total = 0.0

    for e in empList:
        print(e)
        total += e.calcPay()
    
    print("\n\nTotal Paid Out: ${:.2f}".format(total))
    

main()