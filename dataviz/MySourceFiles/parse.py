from collections import Counter

import csv
import matplotlib.pyplot as plt
import numpy as np

MY_FILE = "../data/sample_sfpd_incident_all.csv"
def parse(raw_file, delimiter):
    """Parses a raw CSV file to a JSON-line object."""
  
    # Create parse_data holder
    parsed_data = []
 
    # Open CSV file
    with open(raw_file) as opened_file: 
        # Read CSV file
        csv_data = csv.reader(opened_file, delimiter=delimiter)
        
        # Skip over the first line of the file for the headers
        fields = next(csv_data)

        # Iterate over each row of the csv file, zip together field -> value
        for row in csv_data:
            parsed_data.append(dict(zip(fields, row)))

    # Close CSV file
    opened_file.closed

    # Build a data structure to return parsed_data
    return parsed_data

def visualize_days():
    """Visualize data by day of week"""
    
    # grab our parsed data that we parsed earlier
    data_file = parse(MY_FILE, ",")
    
    # make a new variable, 'counter', from iterating through each
    # line of data in the parsed data, and count how many incidents
    # happen on each day of the week
    counter = Counter(item["DayOfWeek"] for item in data_file)

    # separate the x-axis data (the days of the week) from the
    # 'counter variable from the y-axis data (the number of
    # incidents for each day)
    data_list = [
                    counter["Monday"],
                    counter["Tuesday"],
                    counter["Wednesday"],
                    counter["Thursday"],
                    counter["Friday"],
                    counter["Saturday"],
                    counter["Sunday"]
                    ]
    day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    # with that y-axis data, assign it to a matplotlib plot instance
    plt.plot(data_list)

    # create the amount of ticks needed for our x-axis, and assign
    # the labels
    plt.xticks(range(len(day_tuple)), day_tuple)

    # save the plot!
    plt.savefig("Days.png")

    # cloase plot file
    plt.clf()

def visualize_type():
    """Visualize data by category in a bar graph."""
    data_file = parse(MY_FILE, ",")
    counter = Counter(item["Category"] for item in data_file)
    labels = tuple(counter.keys())
    # Set where the labels hit the x-axis
    xlocations = np.arange(len(labels)) + 0.5
    # Assign labels and tick location to x-axis
    width = 0.5
    plt.bar(xlocations, counter.values(), width=width)
    plt.xticks(xlocations + width / 2, labels, rotation=90)
    # Give some more room so the labels aren't cut off in the graph
    plt.subplots_adjust(bottom=0.4)
    # Make the overall graph/figure larger
    plt.rcParams['figure.figsize'] = 12, 8
    # Save and close
    plt.savefig("Type.png")
    plt.clf()

def main():
    # Call our parse function and give it the needed parameters
    visualize_days()
    visualize_type()
    # Let's see what the data looks like!

if __name__ == "__main__":
    main()
