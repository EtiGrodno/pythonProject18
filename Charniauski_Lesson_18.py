#ДЗ на понедельник (Ivanov_Lesson_18.py)
# Создайте класс BankAccount, который представляет банковский счет.
class BankAccount:
# У класса есть приватные свойства __account_number (номер счета) и __balance (баланс).
    __account_number = None
    __balance = 0
# Инициализатор __init__ используется для инициализации номера счета и начального баланса.
    def __init__(self, namber_acc = __account_number, elementary_bal = __balance):
        self.namber_acc = namber_acc
        self.elementary_bal = elementary_bal
# Методы get_account_number и get_balance предоставляют
# доступ к приватным свойствам __account_number и __balance соответственно.
    def get_account_number(self):
        print(f'Номер счёта: {self.namber_acc}')
    def get_balance(self):
        print(f'Баланс: {self.elementary_bal}')
# Методы deposit и withdraw позволяют пополнять и снимать деньги со счета,
# при этом проверяя валидность операции (достаточно ли средств, корректно ли введена сумма для снятия).
    def deposit(self, popolneniye):
        self.elementary_bal += popolneniye
        print(f'Получено {popolneniye} рублей. Новый счет: {self.elementary_bal}')
    def withdraw(self, snyatiye):
        if self.elementary_bal >= snyatiye:
            self.elementary_bal -= snyatiye
            print(f'Снято {snyatiye} рублей. Новый счет: {self.elementary_bal}')
        else:
            print(f'Недостаточно средств. Свертесь с балансом счёта: {self.elementary_bal}')

#В основной части кода мы создаем экземпляр класса BankAccount
# с номером счета "123456789" и начальным балансом 1000.

my_BankAccount_privat = BankAccount()
my_BankAccount_privat.get_account_number()
my_BankAccount_privat.get_balance()

my_BankAccount = BankAccount("123456789",1000)
my_BankAccount.get_account_number()
my_BankAccount.get_balance()
my_BankAccount.deposit(10000)
my_BankAccount.withdraw(100)
my_BankAccount.withdraw(100000)
# Затем мы используем методы для получения номера счета и баланса,
# а также для пополнения и снятия средств. Выводятся результаты операций.

