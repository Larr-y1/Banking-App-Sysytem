# lib/account_cli.py

from lib.cli.base_cli import BaseCLI
from lib.models import Account, Customer, Transaction

class AccountCLI(BaseCLI):

    def menu(self):
        print("\n--- Account Menu ---")
        print("0. Return to main menu")
        print("1. Create account")
        print("2. Update account")
        print("3. Delete account")
        print("4. Display all accounts")
        print("5. Find account by attribute")
        print("6. View related transactions and customer")

    def create(self):
        account_type = self.input_str("Enter account type: ")
        balance = self.input_int("Enter initial balance: ")
        customer_id = self.input_int("Enter customer ID for this account: ")
        customer = self.session.query(Customer).get(customer_id)
        if not customer:
            print(f"No customer found with ID {customer_id}. Cannot create account.")
            return

        new_account = Account(account_type=account_type, balance=balance, customer_id=customer_id)
        self.session.add(new_account)
        self.session.commit()
        print(f"Account created with ID: {new_account.id}")
        
    def update(self):
        account_id = self.input_int("Enter account ID to update: ")
        account = self.session.query(Account).get(account_id)
        if not account:
            print("Account not found.")
            return

        print(f"Current Type: {account.account_type} | Balance: {account.balance}")
        account_type = self.input_str("Enter new account type (press Enter to keep current): ", allow_empty=True)
        balance = self.input_str("Enter new balance (press Enter to keep current): ", allow_empty=True)
        
        if account_type:
            account.account_type = account_type
        if balance:
            try:
                account.balance = float(balance)
            except ValueError:
                print("Invalid balance format. Must be a number.")
                return

        self.session.commit()
        print("Account updated successfully.")

        

    def delete(self):
        account_id = self.input_int("Enter account ID to delete: ")
        account = self.session.query(Account).get(account_id)
        if account:
            self.session.delete(account)
            self.session.commit()
            print(f"Account ID {account_id} deleted.")
        else:
            print(f"Account ID {account_id} not found.")

    def list_all(self):
        accounts = self.session.query(Account).all()
        if not accounts:
            print("No accounts found.")
        else:
            for acc in accounts:
                print(f"ID: {acc.id} | Type: {acc.account_type} | Balance: {acc.balance} | Customer ID: {acc.customer_id}")

    def find_by_attribute(self):
        attr = self.input_str("Find by (account_type/balance/customer_id): ").lower()
        if attr not in ("account_type", "balance", "customer_id"):
            print("Invalid attribute.")
            return
        value = self.input_str(f"Enter {attr} to search for: ")
        if attr in ("balance", "customer_id"):
            try:
                value = int(value)
            except ValueError:
                print("Invalid number format.")
                return
        query = {attr: value}
        results = self.session.query(Account).filter_by(**query).all()
        if results:
            for acc in results:
                print(f"ID: {acc.id} | Type: {acc.account_type} | Balance: {acc.balance} | Customer ID: {acc.customer_id}")
        else:
            print("No accounts matched the search.")

    def view_related(self):
        account_id = self.input_int("Enter account ID to view transactions and customer: ")
        account = self.session.query(Account).get(account_id)
        if not account:
            print("Account not found.")
            return
        print(f"Account ID: {account.id} | Type: {account.account_type} | Balance: {account.balance}")
        print(f"Customer: ID {account.customer.id} | Name: {account.customer.name} | Email: {account.customer.email}")
        if account.transactions:
            print("Transactions:")
            for t in account.transactions:
                print(f"ID: {t.id} | Amount: {t.amount} | Date: {t.transcation_date}")
        else:
            print("No transactions for this account.")
