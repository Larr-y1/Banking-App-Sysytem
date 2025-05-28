# lib/branch_cli.py

from lib.cli.base_cli import BaseCLI
from lib.models import Branch, AccountBranch, Account

class BranchCLI(BaseCLI):

    def menu(self):
        print("\n--- Branch Menu ---")
        print("0. Return to main menu")
        print("1. Create branch")
        print("2. Delete branch")
        print("3. Display all branches")
        print("4. Find branch by attribute")
        print("5. View related accounts")

    def create(self):
        name = self.input_str("Enter branch name: ")
        location = self.input_str("Enter branch location: ")
        branch = Branch(name=name, location=location)
        self.session.add(branch)
        self.session.commit()
        print(f"Branch created with ID: {branch.id}")

    def delete(self):
        branch_id = self.input_int("Enter branch ID to delete: ")
        branch = self.session.query(Branch).get(branch_id)
        if branch:
            self.session.delete(branch)
            self.session.commit()
            print(f"Branch ID {branch_id} deleted.")
        else:
            print(f"Branch ID {branch_id} not found.")

    def list_all(self):
        branches = self.session.query(Branch).all()
        if not branches:
            print("No branches found.")
        else:
            for b in branches:
                print(f"ID: {b.id} | Name: {b.name} | Location: {b.location}")

    def find_by_attribute(self):
        attr = self.input_str("Find by (name/location): ").lower()
        if attr not in ("name", "location"):
            print("Invalid attribute.")
            return
        value = self.input_str(f"Enter {attr} to search for: ")
        query = {attr: value}
        branches = self.session.query(Branch).filter_by(**query).all()
        if branches:
            for b in branches:
                print(f"ID: {b.id} | Name: {b.name} | Location: {b.location}")
        else:
            print("No branches matched the search.")

    def view_related(self):
        branch_id = self.input_int("Enter branch ID to view related accounts: ")
        # You need to query AccountBranch for this relation
        relations = self.session.query(AccountBranch).filter_by(branch_id=branch_id).all()
        if not relations:
            print("No accounts related to this branch.")
            return
        print(f"Accounts in Branch ID {branch_id}:")
        for rel in relations:
            account = self.session.query(Account).get(rel.account_id)
            print(f"Account ID: {account.id} | Type: {account.account_type} | Balance: {account.balance}")
