from database import Session, engine, Base
from models import Customer, Account, Transaction, Branch, AccountBranch

# Create all tables (if not already created)
Base.metadata.create_all(engine)

# Open a session
session = Session()

# Create branches
branch1 = Branch(name="Downtown Branch", location="123 Main St")
branch2 = Branch(name="Uptown Branch", location="456 Elm St")

# Add branches to session
session.add_all([branch1, branch2])
session.commit()

# Create customers
customer1 = Customer(name="Larry", email="larry@example.com")
customer2 = Customer(name="Jane Doe", email="jane@example.com")

session.add_all([customer1, customer2])
session.commit()

# Create accounts for customers
account1 = Account(account_type="Checking", balance=1000, customer=customer1)
account2 = Account(account_type="Savings", balance=5000, customer=customer2)

session.add_all([account1, account2])
session.commit()

 # Link accounts to branches (many-to-many via AccountBranch)
link1 = AccountBranch(account=account1, branch=branch1)
link2 = AccountBranch(account=account2, branch=branch2)

session.add_all([link1, link2])
session.commit()

# Create transactions for accounts
transaction1 = Transaction(amount=200, account=account1)
transaction2 = Transaction(amount=150, account=account2)

session.add_all([transaction1, transaction2])
session.commit()

print("Database seeded successfully!")

session.close()