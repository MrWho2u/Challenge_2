# This function is designed to be a helper function that will download a list of loans for the user

import csv

def download_csv(save_path, qualifying_loans):
    header = ["Lender", "Max Loan", "Max LTV", "Max DTI", "Min Credit Score", "Interest Rate"]

    with open(save_path, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        csvwriter.writerow(header)

        for row in qualifying_loans:
            csvwriter.writerow(row)
    
    print("Thanks, your file has been saved")