"""
Purpose: Generate a HTML list elements for the CySoc website.

Input: CSV file with columns named "response", "name", "affiliation", "website".
    - This should be the output of the Shared Google Sheets document.

Output: Print a string containing the HTML list elements.

Author: Matthew DeVerna
"""

import argparse
import pandas as pd


def main():
    parser = argparse.ArgumentParser(description="Create PC block HTML from CSV")
    parser.add_argument("filepath", help="Path to the CSV file containing PC data")
    args = parser.parse_args()

    df = pd.read_csv(args.filepath)

    # Filter rows where response is "Confirmed"
    confirmed_df = df[df["response"] == "Confirmed"]

    # Generate HTML list elements
    html_list_items = []
    for _, row in confirmed_df.iterrows():
        name = row["name"]
        website = (
            row["website"]
            if pd.notna(row["website"]) and row["website"] != ""
            else None
        )
        affiliation = (
            row["affiliation"]
            if pd.notna(row["affiliation"]) and row["affiliation"] != ""
            else None
        )

        # Handle potentially missing information
        if website:
            name_element = f'<a href="{website}" target="_blank">{name}</a>'
        else:
            name_element = name
        affiliation_text = f", {affiliation}" if affiliation else ""

        html_item = (
            f'<li><i class="fa fa-circle"></i> {name_element}{affiliation_text}.</li>'
        )
        html_list_items.append(html_item)

    # Combine into final HTML list
    html_output = "\n".join(html_list_items)
    print(html_output)


if __name__ == "__main__":
    main()
