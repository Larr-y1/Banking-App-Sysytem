from datetime import datetime

from lib.cli.base_cli import BaseCLI
from lib.models import Transaction, Account

class TransactionCLI(BaseCLI):

    def menu(self):
        print("\n--- Transaction Menu ---")
        print("0. Return to main menu")
        print("1. Create transaction")
        print("2. Update transaction")
        print("3. Delete transaction")
        print("4. Display all transactions")
        print("5. Find transaction by attribute")
        print("6. View related account")

    def create(self):
        amount = self.input_int("Enter transaction amount: ")
        account_id = self.input_int("Enter account ID: ")
        account = self.session.query(Account).get(account_id)
        if not account:
            print(f"No account found with ID {account_id}. Cannot create transaction.")
            return
        new_transaction = Transaction(amount=amount, account_id=account_id)
        self.session.add(new_transaction)

        # Optionally update account balance here:
        account.balance += amount
        self.session.commit()
        print(f"Transaction created with ID: {new_transaction.id}. Account balance updated to {account.balance}.")
        
    def update(self):
        transaction_id = self.input_int("Enter transaction ID to update: ")
        transaction = self.session.query(Transaction).get(transaction_id)

        if not transaction:
            print("Transaction not found.")
            return

        print(f"Updating Transaction ID: {transaction.id}")

        amount = self.input_int("Enter new amount (leave blank to keep current): ", allow_empty=True)
        date_str = self.input_str("Enter new transaction date (YYYY-MM-DD) or leave blank: ", allow_empty=True)
        account_id = self.input_int("Enter new account ID (leave blank to keep current): ", allow_empty=True)

        if amount != "":
            transaction.amount = int(amount)

        if date_str:
            try:
                new_date = datetime.strptime(date_str, "%Y-%m-%d")
                transaction.transaction_date = new_date
            except ValueError:
                print("Invalid date format. Use YYYY-MM-DD.")
                return

        if account_id != "":
            transaction.account_id = int(account_id)

        self.session.commit()
        print(" Transaction updated successfully.")

    def delete(self):
        transaction_id = self.input_int("Enter transaction ID to delete: ")
        transaction = self.session.query(Transaction).get(transaction_id)
        if transaction:
            account = transaction.account
            account.balance -= transaction.amount  # rollback balance update
            self.session.delete(transaction)
            self.session.commit()
            print(f"Transaction ID {transaction_id} deleted and account balance updated.")
        else:
            print(f"Transaction ID {transaction_id} not found.")

    def list_all(self):
        transactions = self.session.query(Transaction).all()
        if not transactions:
            print("No transactions found.")
        else:
            for t in transactions:
                print(f"ID: {t.id} | Amount: {t.amount} | Date: {t.transcation_date} | Account ID: {t.account_id}")

    def find_by_attribute(self):
        attr = self.input_str("Find by (amount/account_id): ").lower()
        if attr not in ("amount", "account_id"):
            print("Invalid attribute.")
            return
        value = self.input_str(f"Enter {attr} to search for: ")
        try:
            value = int(value)
        except ValueError:
            print("Invalid number format.")
            return
        query = {attr: value}
        results = self.session.query(Transaction).filter_by(**query).all()
        if results:
            for t in results:
                print(f"ID: {t.id} | Amount: {t.amount} | Date: {t.transcation_date} | Account ID: {t.account_id}")
        else:
            print("No transactions matched the search.")

    def view_related(self):
        transaction_id = self.input_int("Enter transaction ID to view related account: ")
        transaction = self.session.query(Transaction).get(transaction_id)
        if not transaction:
            print("Transaction not found.")
            return
        acc = transaction.account
        print(f"Account ID: {acc.id} | Type: {acc.account_type} | Balance: {acc.balance} | Customer ID: {acc.customer_id}")
