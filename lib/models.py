# models.py
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base


class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    created_at = Column(DateTime, default=func.now())


    accounts = relationship("Account", back_populates="customer")


class Account(Base):
    __tablename__ = 'accounts'

    id = Column(Integer, primary_key=True)
    account_type = Column(String)
    balance = Column(Integer)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    created_at = Column(DateTime, default=func.now())


    customer = relationship("Customer", back_populates="accounts")
    transactions = relationship("Transaction", back_populates="account")  
    
    branches = relationship("AccountBranch", back_populates="account")


class Transaction(Base):
    __tablename__ = 'transactions'

    id = Column(Integer, primary_key=True)
    amount = Column(Integer)
    transcation_date = Column(DateTime, default=func.now())
    account_id = Column(Integer, ForeignKey('accounts.id'))
    created_at = Column(DateTime, default=func.now())
    

    account = relationship("Account", back_populates="transactions")


class Branch(Base):
    __tablename__ = 'branches'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    
    accounts = relationship("AccountBranch", back_populates="branch")


class AccountBranch(Base):
    __tablename__ = 'account_branch'

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('accounts.id'))
    branch_id = Column(Integer, ForeignKey('branches.id'))
    created_at = Column(DateTime, default=func.now())

    account = relationship("Account", back_populates="branches")
    branch = relationship("Branch", back_populates="accounts")
