""" 
    This module does the following:
    1. This module relies on the mydbconn module to connect to the Northwind 
    database.
    
    2. It then performs a complex SQL query that retrieves
    the top 10 customers with the highest total purchase amounts.
    
    3. Finally, it returns the results as a Pandas DataFrame.
 """
import pandas as pd
from mylib.mydbconn import setConn


def query():
    conn = setConn()
    sql_query = """
    WITH RankedCustomers AS (
        SELECT
            c.CustomerID,
            c.CompanyName,
            SUM(od.Quantity * od.UnitPrice) AS TotalPurchaseAmount,
            ROW_NUMBER() OVER (ORDER BY SUM(od.Quantity * od.UnitPrice) DESC) AS Rank
        FROM
            Customers c
        JOIN
            Orders o ON c.CustomerID = o.CustomerID
        JOIN
            [Order Details] od ON o.OrderID = od.OrderID
        GROUP BY
            c.CustomerID,
            c.CompanyName
    )
    SELECT
        CustomerID,
        CompanyName,
        TotalPurchaseAmount
    FROM
        RankedCustomers
    WHERE
        Rank <= 10 
    ORDER BY
        TotalPurchaseAmount DESC;

    """
    cursor = conn[0].cursor()
    cursor.execute(sql_query)
    data = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    myresults = pd.DataFrame(data, columns=columns)

    return myresults
