from sqlalchemy.orm import sessionmaker
from lib.database import engine, Base
from lib.cli.customer_cli import CustomerCLI
from lib.cli.account_cli import AccountCLI
from lib.cli.transcation_cli import TransactionCLI
from lib.cli.branch_cli import BranchCLI
from lib.cli.account_branch_cli import AccountBranchCLI

Base.metadata.create_all(engine)

# import other CLIs similarly

def main():
    Session = sessionmaker(bind=engine)
    session = Session()

    while True:
        print("\n--- Main Menu ---")
        print("0. Exit")
        print("1. Manage Customers")
        print("2. Manage Accounts")
        print("3. Manage Transactions")
        print("4. Manage Branches")
        print("5. Manage Account-Branches")
        
        choice = input("> ").strip()
        if choice == "0":
            print("Goodbye!")
            break
        elif choice == "1":
            CustomerCLI(session).run()
        elif choice == "2":
            AccountCLI(session).run()
            pass
        elif choice == "3":
            TransactionCLI(session).run()
            pass
        elif choice == "4":
            BranchCLI(session).run()
            pass
        elif choice == "5":
            AccountBranchCLI(session).run()
            pass
        else:
            print("Invalid choice.")

    session.close()

if __name__ == "__main__":
    main()
