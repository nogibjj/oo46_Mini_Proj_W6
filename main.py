"""

"""
from mylib.query import query
import pandas as pd
import matplotlib.pyplot as plt


def main():
    myresults = query()

    # Prepare and plot top sales by car make chart
    fig, ax = plt.subplots(figsize=(13, 10))
    
    ax.bar(
        myresults["companyname"],
        myresults["totalpurchaseamount"],
        color="brown",
    )
    # Add annotation to bars
    for p in ax.patches:
        ax.annotate(
            str(round(p.get_height(), 2)),
            (p.get_x() * 1.005, p.get_height() * 1.005),
        )

    ax.set_title(
        "Top 10 Customers with the Highest Total Purchase Amounts",
        loc="left",
    )
    ax.set_xlabel("Total Purchase Amounts")
    ax.set_ylabel("Company Name")
    ax.set_xticklabels(myresults["companyname"], rotation=90, va="top")
    plt.savefig("top.png")
    plt.show()
    # print(myresults)

    return "Success"


if __name__ == "__main__":
    main()
