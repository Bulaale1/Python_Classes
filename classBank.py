print('--- Welcome To Python Classes ---')
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount <= 0:
            print(f"❌ Error: Cannot deposit {amount}. Amount must be positive.")
            return
        
        self.balance += amount
        # now = datetime.datetime.now()
        self.transaction_history.append(f"+{amount}")
        print(f"✅ Deposited ${amount}. New balance: ${self.balance} ")

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Error: Withdrawal amount must be positive.")
        elif amount > self.balance:
            print(f"❌ Error: Insufficient funds! You tried to withdraw ${amount} but only have ${self.balance}.")
        else:
            self.balance -= amount
            # now = datetime.datetime.now()
            self.transaction_history.append(f"-{amount}")
            print(f"💸 Withdrew ${amount} . Remaining: ${self.balance}")

    def details(self):
        print(f"\n👤 Holder: {self.account_holder} | 💰 Balance: ${self.balance}")

    def statement(self):
        print(f'\n--- 📜 Transaction History for {self.account_holder} ---')
        if not self.transaction_history:
            print("No transactions yet.")
        for entry in self.transaction_history:
            status = 'Deposit' if entry.startswith('+') else 'Withdrawal'
            print(f' {status:12}: {entry}')


account1 = BankAccount('Budhcad',580)
account1.deposit(250)
account1.deposit(350)
account1.deposit(-250)
account1.withdraw(57)
account1.withdraw(0)
account1.details()
account1.statement()