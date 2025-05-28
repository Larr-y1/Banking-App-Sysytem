from lib.cli.base_cli import BaseCLI
from lib.models import Customer

class CustomerCLI(BaseCLI):

    def menu(self):
        print("\n--- Customer Menu ---")
        print("0. Return to main menu")
        print("1. Create customer")
        print("2. Delete customer")
        print("3. Display all customers")
        print("4. Find customer by attribute")
        print("5. View related accounts")

    def create(self):
        name = self.input_str("Enter customer name: ")
        email = self.input_str("Enter customer email: ")
        new_customer = Customer(name=name, email=email)
        self.session.add(new_customer)
        self.session.commit()
        print(f"Customer created with ID: {new_customer.id}")

    def delete(self):
        customer_id = self.input_int("Enter customer ID to delete: ")
        customer = self.session.query(Customer).get(customer_id)
        if customer:
            self.session.delete(customer)
            self.session.commit()
            print(f"Customer ID {customer_id} deleted.")
        else:
            print(f"Customer ID {customer_id} not found.")

    def list_all(self):
        customers = self.session.query(Customer).all()
        if not customers:
            print("No customers found.")
        else:
            for c in customers:
                print(f"ID: {c.id} | Name: {c.name} | Email: {c.email}")

    def find_by_attribute(self):
        attr = self.input_str("Find by (name/email): ").lower()

        if attr not in ("name", "email"):
            print("Invalid attribute. Must be 'name' or 'email'.")
            return

        value = self.input_str(f"Enter {attr} to search for: ").strip()
        query = {attr: value}

        customers = self.session.query(Customer).filter_by(**query).all()
        
        if customers:
            for c in customers:
                print(f"ID: {c.id} | Name: {c.name} | Email: {c.email}")
        else:
            print("No customers matched the search.")




    def view_related(self):
        customer_id = self.input_int("Enter customer ID to view accounts: ")
        customer = self.session.query(Customer).get(customer_id)
        if customer:
            if customer.accounts:
                print(f"Accounts for {customer.name}:")
                for account in customer.accounts:
                    print(f"ID: {account.id} | Type: {account.account_type} | Balance: {account.balance}")
            else:
                print("This customer has no accounts.")
        else:
            print("Customer not found.")
