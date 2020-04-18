import random
import time
import threading

PARKOMAT_PRICE = 50000
SERVICE_PRICE = 100
SALARY = 50
MAX_DEBT = -90000
MONTH = 60
RENT_TICK = 20
global gameStatus


class Model:
    
    def __init__(self):
        self.__availableParcomats = 0
        self.__rentedParkomat = 0
        self.__staffAmount = 0
        self.__budget = 500000
        self.__price = 700
        
    def buyParkomats(self, num = 1):
        if (PARKOMAT_PRICE*num) > self.__budget:
            print("\nУ Вас не хватает денег")
        elif (self.__rentedParkomat + self.__availableParcomats + 1)//10 >= self.__staffAmount:
            print("\nУ Вас недостаточно сотрудников")
        else:
            self.__budget -= (PARKOMAT_PRICE*num)
            self.__availableParcomats += num
    
    def rentParkomat(self, num=1):
        if self.__availableParcomats < num:
            print('\nУ Вас недостаточно паркоматов')
        else:
            self.__rentedParkomat += num
            self.__availableParcomats -= num
            
    def getAvailableParkomats(self):
        return self.__availableParcomats
    
    def hireStaff(self, num=1):
        self.__staffAmount += num
    
    def calculateProfit(self):
        income = self.__getIncome()
        print(f"\nДоход: {income}")
        expenses = self.__calculateExpenses()
        print(f"\nРасход: {expenses}")
        profit = income - expenses
        print(f"\nПрибыль: {profit}")
        self.__budget += profit
    
    
    def getBuget(self):
        return self.__budget
        
    
    def __getIncome(self):
        return self.__rentedParkomat*self.__price
        
    def __calculateExpenses(self):
        temp = .5 * self.__availableParcomats + .8 * self.__rentedParkomat 
        temp += SALARY * self.__staffAmount
        return temp
    
    def setPrice(self, price):
        self.__price = price


def generateClient(model):
    time.sleep(RENT_TICK)
    while gameStatus:
        clients = random.randint(0, model.getAvailableParkomats())
        model.rentParkomat(num=clients)
        print(f"\nПришло клиентов: {clients}")
        time.sleep(RENT_TICK)
    
def environment(model):
    time.sleep(MONTH)
    while model.getBuget() > MAX_DEBT:
        model.calculateProfit()
        time.sleep(MONTH)
    gameStatus = False

if __name__ == '__main__':
    model = Model()
    gameStatus = True
    threads = list()
    threads.append(threading.Thread(target=generateClient, args=(model, )))
    threads.append(threading.Thread(target=environment, args=(model, )))
    [t.start() for t in threads]
    states = {'1': model.buyParkomats, 
              '2': model.hireStaff}
    while gameStatus:
        do = input('\n1:Купить паркомат. 2: Нанять сотрудников')
        if 'q' == do:
            gameStatus = False
            exit()
        col = input('\nКоличество: ')
        action = states.get(do, None)
        if action is None:
            print("\nНет такого действия")
            continue
        action(num=int(col))
    [t.join() for t in threads]
    print("\nКонец игры!")