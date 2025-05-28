# lib/account_branch_cli.py

from lib.cli.base_cli import BaseCLI
from lib.models import AccountBranch, Account, Branch

class AccountBranchCLI(BaseCLI):

    def menu(self):
        print("\n--- Account-Branch Menu ---")
        print("0. Return to main menu")
        print("1. Link account to branch")
        print("2. Unlink account from branch")
        print("3. Display all account-branch links")
        print("4. Find link by attribute")
        print("5. View related account and branch")

    def create(self):
        account_id = self.input_int("Enter account ID: ")
        branch_id = self.input_int("Enter branch ID: ")
        account = self.session.query(Account).get(account_id)
        branch = self.session.query(Branch).get(branch_id)
        if not account or not branch:
            print("Invalid account or branch ID.")
            return
        link = AccountBranch(account_id=account_id, branch_id=branch_id)
        self.session.add(link)
        self.session.commit()
        print(f"Link created with ID: {link.id}")

    def delete(self):
        link_id = self.input_int("Enter link ID to delete: ")
        link = self.session.query(AccountBranch).get(link_id)
        if link:
            self.session.delete(link)
            self.session.commit()
            print(f"Link ID {link_id} deleted.")
        else:
            print(f"Link ID {link_id} not found.")

    def list_all(self):
        links = self.session.query(AccountBranch).all()
        if not links:
            print("No links found.")
        else:
            for l in links:
                print(f"ID: {l.id} | Account ID: {l.account_id} | Branch ID: {l.branch_id}")

    def find_by_attribute(self):
        attr = self.input_str("Find by (account_id/branch_id): ").lower()
        if attr not in ("account_id", "branch_id"):
            print("Invalid attribute.")
            return
        value = self.input_str(f"Enter {attr} to search for: ")
        try:
            value = int(value)
        except ValueError:
            print("Invalid number format.")
            return
        links = self.session.query(AccountBranch).filter_by(**{attr: value}).all()
        if links:
            for l in links:
                print(f"ID: {l.id} | Account ID: {l.account_id} | Branch ID: {l.branch_id}")
        else:
            print("No links matched the search.")

    def view_related(self):
        link_id = self.input_int("Enter link ID to view related account and branch: ")
        link = self.session.query(AccountBranch).get(link_id)
        if not link:
            print("Link not found.")
            return
        account = self.session.query(Account).get(link.account_id)
        branch = self.session.query(Branch).get(link.branch_id)
        print(f"Account: ID {account.id} | Type: {account.account_type} | Balance: {account.balance}")
        print(f"Branch: ID {branch.id} | Name: {branch.name} | Location: {branch.location}")
