# Abstract DataSource and concrete implementations for CSV, Excel, and SQL data loading.
"""
DataSource abstractions and concrete implementations for CSV, Excel, and SQL.

This module defines an abstract DataSource interface and three concrete
implementations that load data into pandas DataFrame objects:

- DataSource: Abstract base class with a .load() method that all
  concrete sources must implement.
- CSVDataSource: Loads CSV files using pandas.read_csv. Accepts any kwargs
  that pandas.read_csv supports.
- ExcelDataSource: Loads Excel files using pandas.read_excel. Supports
  selecting a sheet and additional pandas.read_excel kwargs.
- SQLDataSource: Executes a SQL query using SQLAlchemy and returns a
  DataFrame via pandas.read_sql.

Utility:
- run_pipeline(source: DataSource) -> pd.DataFrame : A simple example pipeline
  that delegates loading to a DataSource. Intended as an example of
  dependency inversion / delegation.

Usage examples:
    csv_src = CSVDataSource("data/file.csv", sep=",")
    df = run_pipeline(csv_src)

    excel_src = ExcelDataSource("data/file.xlsx", sheet_name="Sheet1")
    df = run_pipeline(excel_src)

    sql_src = SQLDataSource("sqlite:///my.db", "SELECT * FROM table")
    df = run_pipeline(sql_src)

Notes:
- pandas and SQLAlchemy are runtime dependencies.
- SQLDataSource requires a valid SQLAlchemy connection string and a database
  accessible at runtime.

This file is intentionally small and focused on demonstrating how to design a
simple extensible data-loading interface suitable for testing and small ETL
workflows.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any
import pandas as pd
import sqlalchemy as sa


class DataSource(ABC):
    """Abstract idea of something that can load data."""

    @abstractmethod
    def load(self) -> Any:
        """Load data from somewhere."""
        raise NotImplementedError("Subclasses must implement 'load'")


class CSVDataSource(DataSource):
  
from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any
import pandas as pd
import sqlalchemy as sa


class DataSource(ABC):
    """Abstract idea of something that can load data."""

    @abstractmethod
    def load(self) -> Any:
        """Load data from somewhere."""
        raise NotImplementedError("Subclasses must implement 'load'")


class CSVDataSource(DataSource):
    """Concrete data source that loads data from a CSV file."""

    def __init__(self, path: str, **read_csv_kwargs):
        # Store path and any additional arguments for pandas.read_csv
        self.path = path
        self.read_csv_kwargs = read_csv_kwargs

    def load(self) -> pd.DataFrame:
        """Load data from a CSV file into a DataFrame."""
        return pd.read_csv(self.path, **self.read_csv_kwargs)


class ExcelDataSource(DataSource):
    """Concrete data source that loads data from an Excel file."""

    def __init__(self, path: str, sheet_name: str | int = 0, **read_excel_kwargs):
        # Store path, sheet_name and any additional arguments for pandas.read_excel
        self.path = path
        self.sheet_name = sheet_name
        self.read_excel_kwargs = read_excel_kwargs

    def load(self) -> pd.DataFrame:
        """Load data from an Excel file into a DataFrame."""
        return pd.read_excel(
            self.path,
            sheet_name=self.sheet_name,
            **self.read_excel_kwargs,
        )


class SQLDataSource(DataSource):
    """Concrete data source that loads data from a SQL database."""

    def __init__(self, connection_string: str, query: str):
        # Store connection string and query
        self.connection_string = connection_string
        self.query = query

    def load(self) -> pd.DataFrame:
        """Execute query on a database and return results as a DataFrame."""
        engine = sa.create_engine(self.connection_string)
        with engine.connect() as conn:
            return pd.read_sql(self.query, conn)


def run_pipeline(source: DataSource) -> pd.DataFrame:
    """Example pipeline that delegates data loading to a DataSource."""
    # Delegation: pipeline does not know HOW data is loaded,
    # it only knows that 'source' has a .load() method.
    data = source.load()
    # Here you could add cleaning, transformations, etc.
    return data


def main() -> None:
    # Example 1: load from CSV
    csv_source = CSVDataSource("data/customers.csv")
    df_csv = run_pipeline(csv_source)
    print("CSV data:")
    print(df_csv.head())

    # Example 2: load from Excel
    excel_source = ExcelDataSource("data/customers.xlsx", sheet_name="Sheet1")
    df_excel = run_pipeline(excel_source)
    print("\nExcel data:")
    print(df_excel.head())

    # Example 3: load from SQL (requires a valid connection string and database)
    # Uncomment and adjust the connection string and query before using.
    #
    # sql_source = SQLDataSource(
    #     "postgresql+psycopg2://user:password@host:5432/dbname",
    #     "SELECT * FROM customers",
    # )
    # df_sql = run_pipeline(sql_source)
    # print("\nSQL data:")
    # print(df_sql.head())


if __name__ == "__main__":
    main()
