import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py

from logic_bank.logic_bank import Rule

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# Define the base class
Base = declarative_base()

# Example table model with description and SQLAlchemy attributes
class Customer(Base):
    """
    description: The Customer table holds information about the customers.
    """
    __tablename__ = 'customers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    join_date = Column(DateTime, default=datetime.datetime.utcnow)

class Order(Base):
    """
    description: The Order table holds information about customer orders.
    """
    __tablename__ = 'orders'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    order_date = Column(DateTime, default=datetime.datetime.utcnow)
    total_amount = Column(Float, nullable=False, default=0.0)

class Product(Base):
    """
    description: The Product table contains product information.
    """
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False, default=0.0)
    quantity_in_stock = Column(Integer, nullable=False, default=0)

class OrderDetail(Base):
    """
    description: The OrderDetail table holds information about specific products in an order.
    """
    __tablename__ = 'order_details'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    unit_price = Column(Float, nullable=False, default=0.0)

class Supplier(Base):
    """
    description: The Supplier table holds information about suppliers.
    """
    __tablename__ = 'suppliers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    contact_email = Column(String, nullable=True)

class ProductSupplier(Base):
    """
    description: The ProductSupplier table maps products to suppliers.
    """
    __tablename__ = 'product_suppliers'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    supplier_id = Column(Integer, ForeignKey('suppliers.id'), nullable=False)

class Category(Base):
    """
    description: The Category table contains product category information.
    """
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)

class ProductCategory(Base):
    """
    description: The ProductCategory table assigns categories to products.
    """
    __tablename__ = 'product_categories'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)

class Employee(Base):
    """
    description: The Employee table holds employee information.
    """
    __tablename__ = 'employees'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    hire_date = Column(DateTime, default=datetime.datetime.utcnow)

class Department(Base):
    """
    description: The Department table contains information on company departments.
    """
    __tablename__ = 'departments'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=True)

class EmployeeDepartment(Base):
    """
    description: The EmployeeDepartment table associates employees with departments.
    """
    __tablename__ = 'employee_departments'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey('employees.id'), nullable=False)
    department_id = Column(Integer, ForeignKey('departments.id'), nullable=False)

class Country(Base):
    """
    description: The Country table contains information about countries.
    """
    __tablename__ = 'countries'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)


# Create the SQLite database
engine = create_engine('sqlite:///system/genai/temp/create_db_models.sqlite')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

# Add some sample data to the tables
session.add_all([
    Customer(name='Alice', email='alice@example.com'),
    Customer(name='Bob', email='bob@example.com'),
    Order(customer_id=1, total_amount=100.0),
    Order(customer_id=2, total_amount=250.0),
    Product(name='Laptop', price=1200.0, quantity_in_stock=10),
    Product(name='Mouse', price=25.0, quantity_in_stock=200),
    OrderDetail(order_id=1, product_id=1, quantity=1, unit_price=1200.0),
    OrderDetail(order_id=2, product_id=2, quantity=2, unit_price=25.0),
    Supplier(name='ABC Corp', contact_email='contact@abccorp.com'),
    Supplier(name='Best Supplies', contact_email='info@bestsupplies.com'),
    ProductSupplier(product_id=1, supplier_id=1),
    ProductSupplier(product_id=2, supplier_id=2),
    Category(name='Electronics'),
    Category(name='Accessories'),
    ProductCategory(product_id=1, category_id=1),
    ProductCategory(product_id=2, category_id=2),
    Employee(name='Charlie', hire_date=datetime.datetime(2021, 1, 15)),
    Employee(name='Dana', hire_date=datetime.datetime(2022, 5, 20)),
    Department(name='Sales', location='New York'),
    Department(name='IT', location='San Francisco'),
    EmployeeDepartment(employee_id=1, department_id=1),
    EmployeeDepartment(employee_id=2, department_id=2),
    Country(name='USA'),
    Country(name='Canada')
])

# Commit the changes
session.commit()
session.close()
