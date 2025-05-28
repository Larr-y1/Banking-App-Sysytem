## 🏦 Banking System CLI Application

## 🔍 Overview
This is a simple banking system implemented as a Command-Line Interface (CLI) application using Python, SQLAlchemy ORM, and Alembic for database migrations. The system manages customers, accounts, transactions, branches, and their relationships, providing CRUD operations and linkage between accounts and branches.

The project follows a modular architecture with a clear separation of concerns between models, CLI interfaces, database setup, and migration scripts.

## ⚙️ Features
- Manage Customers: Create, update, delete, and list customers.
- Manage Accounts: Create accounts linked to customers with types and balances.
- Manage Transactions: Record deposits, withdrawals, and track transaction history per account.
- Manage Branches: Define bank branches with name and location.
- Manage Account-Branch Links: Link and unlink accounts with branches (many-to-many relationship).
- View detailed information including related records.
- Data persistence using SQLite database.
- Database schema management with Alembic migrations.
- Seed script to populate initial data for testing.
- Interactive CLI menus for all operations.

## 📁 Project Structure
lib/
├── cli/
│   ├── base_cli.py           # Base CLI class for common input methods
│   ├── cli.py                # Main CLI application entry point
│   ├── customer_cli.py       # Customer-related CLI operations
│   ├── account_cli.py        # Account-related CLI operations
│   ├── transaction_cli.py    # Transaction-related CLI operations
│   ├── branch_cli.py         # Branch-related CLI operations
│   └── account_branch_cli.py # Account-Branch linking CLI operations
│
├── migration/
│   ├── env.py                # Alembic environment config
│   ├── script.py.mako        # Alembic migration template
│   └── versions/
│       └── 676100088ae4_create_tables.py # Migration script to create tables
│
├── database.py               # Database setup (engine, session, Base)
├── models.py                 # SQLAlchemy ORM models
├── seed.py                   # Script to populate sample data
└── __init__.py

## 📋 Prerequisites
- Python 3.8+
- SQLAlchemy ORM for database interaction
- SQLite as the lightweight database engine
- Alembic for managing database migrations
- Command-Line Interface (CLI) for user interaction

## 🛠 Installation
### 1.Clone the repository:
```bash
git clone https://github.com/Larr-y1/Banking-App-Sysytem
cd Banking-App-System
```
### 2.Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate    # macOS/Linux
venv\Scripts\activate    # Windows
```

### 3.Install dependencies using Pipenv (recommended):
```bash
pip install pipenv
pipenv install
```

## 🚀 Usage
### Run the CLI (from the project root)
```bash
python -m lib.cli.cli
```

**Don’t run it like this:**  
```bash
python lib/cli/cli.py  #  Will fail with ModuleNotFoundError
```

- Using `-m` tells Python to treat `lib` as a package so all internal imports work properly.

---
You will be presented with the main menu options:
- Manage Customers
- Manage Accounts
- Manage Transactions
- Manage Branches
- Manage Account-Branches
- Exit
Navigate menus by typing the option number and following prompts.

## Example Workflow
- Add a new customer.
- Create an account linked to that customer.
- Add a new branch.
- Link the account to a branch.
- Make transactions on the account.
- Query linked accounts and branches.

## 🤝 Development & Contribution
- Fork the repository and create feature branches.
- Use Alembic for database migrations when modifying models.
- Add corresponding CLI modules for new features.
- Write clear commit messages.
- Run and test your changes locally.

## 📄 License
This project is open source and available under the MIT License.

Happy coding, and let’s build powerful CLI together! 🚀

