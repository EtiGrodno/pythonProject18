#ДЗ на понедельник (Ivanov_Lesson_18.py)
# Создайте класс BankAccount, который представляет банковский счет.
class BankAccount:
# У класса есть приватные свойства __account_number (номер счета) и __balance (баланс).
    __account_number = None
    __balance = 0
# Инициализатор __init__ используется для инициализации номера счета и начального баланса.
    def __init__(self,__account_number, __balance):
        self.__account_number = __account_number
        self.__balance = __balance

# Методы get_account_number и get_balance предоставляют
# доступ к приватным свойствам __account_number и __balance соответственно.
    def get_account_number(self):
        print(f'Номер счёта: {self.__account_number}')
    def get_balance(self):
        print(f'Баланс: {self.__balance}')
# Методы deposit и withdraw позволяют пополнять и снимать деньги со счета,
# при этом проверяя валидность операции (достаточно ли средств, корректно ли введена сумма для снятия).
    def deposit(self, popolneniye):
        self.__balance += popolneniye
        print(f'Получено {popolneniye} рублей. Новый счет: {self.__balance}')
    def withdraw(self, snyatiye):
        if self.__balance >= snyatiye:
            self.__balance -= snyatiye
            print(f'Снято {snyatiye} рублей. Новый счет: {self.__balance}')
        else:
            print(f'Недостаточно средств. Свертесь с балансом счёта: {self.__balance}')

#В основной части кода мы создаем экземпляр класса BankAccount
# с номером счета "123456789" и начальным балансом 1000.

my_BankAccount = BankAccount("123456789",1000)
my_BankAccount.get_account_number()
my_BankAccount.get_balance()
my_BankAccount.deposit(10000)
my_BankAccount.withdraw(100)
my_BankAccount.withdraw(100000)
# Затем мы используем методы для получения номера счета и баланса,
# а также для пополнения и снятия средств. Выводятся результаты операций.

