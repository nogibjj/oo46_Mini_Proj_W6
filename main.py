"""
This module is the main module of the project. It calls the query function
 from the query module to get the data from the database. Then, it plots the
   data and saves the plot as a png file. Finally, it returns a string "Success"
     to indicate that the program has run successfully.
"""
from mylib.query import query
import matplotlib.pyplot as plt


def main():
    # Load data
    myresults = query()

    # Plot the data
    fig, ax = plt.subplots(figsize=(15, 10))

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

    # Set tick positions and labels
    ax.set_xticks(range(len(myresults["companyname"])))
    ax.set_xticklabels(myresults["companyname"], rotation=90, va="top")

    ax.set_title(
        "Top 10 Customers with the Highest Total Purchase Amounts",
        loc="left",
    )
    ax.set_xlabel("Company Name")
    ax.set_ylabel("Total Purchase Amounts")

    plt.savefig("top.png")
    plt.show()

    return "Success"


if __name__ == "__main__":
    main()
