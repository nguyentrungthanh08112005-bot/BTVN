class BankAccount:
    def __init__(self, account_number, balance=0):

        self._account_number = account_number
        self._balance = balance

    @property
    def account_number(self):
        return self._account_number

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Đã nạp: {amount:,} VND")
        else:
            print("Số tiền nạp phải lớn hơn 0!")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            print(f"Đã rút: {amount:,} VND")
        else:
            print("Số dư không đủ hoặc số tiền không hợp lệ!")


    def get_balance(self):
        return self._balance

if __name__ == "__main__":
    my_acc = BankAccount("VCB-123456", 1000000)

    print(f"Số tài khoản: {my_acc.account_number}")
    print(f"Số dư hiện tại: {my_acc.get_balance():,} VND")
    print("-" * 30)

    my_acc.deposit(500000)  
    my_acc.withdraw(200000)  
    my_acc.withdraw(2000000) 
    
    print("-" * 30)
    print(f"Số dư cuối cùng: {my_acc.get_balance():,} VND")
    print("-" * 30)

    print("Thử đổi số tài khoản sang 'NEW-ID'...")