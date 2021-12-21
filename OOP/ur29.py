class Account:
    rate_usd = 0.013
    rate_euro = 0.011
    suffix = 'RUB'
    suffix1 = 'USD'
    suffix2 = 'EUR'

    def __init__(self, surname, num, percent, value=0):
        self.surname = surname  # Фамилия
        self.num = num  # номер счета
        self.percent = percent  # процент начисления
        self.value = value  # сумма в рублях
        print(f'Счет #{num} принадлежащий {surname} был открыт.')
        print('*' * 50)

    def __del__(self):
        print('*' * 50)
        print(f'Счет #{self.num} принадлежащий {self.surname} был закрыт.')

    @staticmethod
    def convert(value, rate):
        return value * rate

    @staticmethod
    def set_usd_rate(cls, rate):
        """редактирование курса рубля по отношению к доллару"""
        cls.rate_usd = rate

    @staticmethod
    def set_eur_rate(cls, rate):
        """редактирование курса рубля по отношению к евро"""
        Account.rate_eur = rate

    def edit_owner(self, surname):
        self.surname = surname

    def print_balance(self):
        print(f'Текущий баланс: {self.value} {Account.suffix}')

    def print_info(self):
        """Вывод информации о счете"""
        print('Информация о счете')
        print('-' * 25)
        print(f'Владелец: #{self.num}\n'
              f'Владелец: {self.surname}')
        self.print_balance()
        print(f'Проценты: {self.percent:.0%}')
        print('-' * 25)

    def convert_to_usd(self):
        """Перевод в доллары"""
        usd_val = Account.convert(self.value, Account.rate_usd)
        print(f'Состояние счета: {usd_val} {Account.suffix1}.')

    def convert_to_euro(self):
        """Перевод в евро"""
        eur_val = Account.convert(self.value, Account.rate_euro)
        print(f'Состояние счета: {eur_val} {Account.suffix2}.')

    def add_persents(self):
        self.value += self.value * self.percent
        print(f'Проценты успешно начислены!')
        self.print_balance()

    def withdraw_money(self, val):
        """Снятие заданной суммы"""
        if val > self.value:
            print(f'К сожелению у Вас нет {val} {Account.suffix}')
        else:
            self.value -= val
            print(f'{val} {Account.suffix} было успешно снято!')
        self.print_balance()

    def add_maney(self, val):
        self.value += val
        print(f'{val} {Account.suffix} было успешно добавлено!')
        self.print_balance()


acc = Account('Долгих', 12345, 0.03, 1000)
acc.print_info()
acc.convert_to_usd()
acc.convert_to_euro()
print()
acc.set_usd_rate()
acc.convert_to_usd()
acc.set_eur_rate()
acc.convert_to_euro()
print()
acc.edit_owner("Дюма")
acc.print_info()
print()
acc.add_persents()
print()
acc.withdraw_money(3000)
acc.withdraw_money(100)
print()
acc.add_maney(5000)
print()
acc.withdraw_money(3000)
print()
