import requests

def redcap_survey(record_id):

    URL = 'https://redcap.sydney.edu.au/api/'

    data = {
        'token': 'F6CF0866B9B26D6B44661F25D09F51E5',
        'content': 'report',
        'format': 'csv',
        'report_id': '5815',
        'rawOrLabel': 'raw',
        'rawOrLabelHeaders': 'raw',
        'exportCheckboxLabel': 'false',
        'returnFormat': 'csv'
    }

    r = requests.post(URL, data=data)
    buf = r.content

    # Split the csv file, remove last line
    splitter = buf[:-1].split(b'\n')

    # For storing each record
    record = []

    # Remove the labels of report
    splitter.pop(0)

    # Based off the .docx file
    labels = ["Trainability",
              "Rideability",
              "Boldness",
              "Handling compliance",
              "Working compliance",
              "Easy to stop",
              "Forward going",
              "Human social confidence",
              "Non-human social confidence",
              "Novel object confidence",
              "Touch sensitivity",
              "Easy to load",
              "Independence",
              "Repetitive behaviours"]

    # Take the integer values determined by survey
    # Autofill empty values with Zero (0)
    for entry in splitter:
        # convert entry to regular string
        entr = entry.decode("utf-8")
        tmp_split = entr.split(",")
        final = []
        for i in range(3,23):
            try:
                final.append(int(tmp_split[i]))
            except ValueError:
                final.append(0)
        for i in range(24,len(tmp_split)):
            try:
                final.append(int(tmp_split[i]))
            except ValueError:
                final.append(0)

        record.append(final)

    # Our specified record
    chosen_survey = record.pop(record_id - 1)
    totals = []
    mean_totals = []

    # Here we go through and sort by groupings
    # Determined by the .docx file
    # 1 0-4
    first = chosen_survey[0:5]
    totals.append(sum(first))
    tmp_mean = 0
    for each in record:
        tmp_mean += sum(each[0:5])
    mean_totals.append(tmp_mean/len(record))

    # 2 5-17
    second = chosen_survey[5:18]
    totals.append(sum(second))
    tmp_mean = 0
    for each in record:
        tmp_mean += sum(each[5:18])
    mean_totals.append(tmp_mean/len(record))

    # 3 18-24
    third = chosen_survey[18:25]
    totals.append(sum(third))
    tmp_mean = 0
    for each in record:
        tmp_mean += sum(each[18:25])
    mean_totals.append(tmp_mean/len(record))

    # 4 25-34
    fourth = chosen_survey[25:35]
    totals.append(sum(fourth))
    tmp_mean = 0
    for each in record:
        tmp_mean += sum(each[25:35])
    mean_totals.append(tmp_mean/len(record))

    # 5 35-42
    fifth = chosen_survey[35:43]
    totals.append(sum(fifth))
    tmp_mean = 0
    for each in record:
        tmp_mean += sum(each[35:43])
    mean_totals.append(tmp_mean/len(record))

    # 6 43-50
    sixth = chosen_survey[43:51]
    totals.append(sum(sixth))
    tmp_mean = 0
    for each in record:
        tmp_mean += sum(each[43:51])
    mean_totals.append(tmp_mean/len(record))

    # 7 51-57
    seventh = chosen_survey[51:58]
    totals.append(sum(seventh))
    tmp_mean = 0
    for each in record:
        tmp_mean += sum(each[51:58])
    mean_totals.append(tmp_mean/len(record))

    # 8 58-60
    eighth = chosen_survey[58:61]
    totals.append(sum(eighth))
    tmp_mean = 0
    for each in record:
        tmp_mean += sum(each[58:61])
    mean_totals.append(tmp_mean/len(record))

    # 9 61-76
    ninth = chosen_survey[61:77]
    totals.append(sum(ninth))
    tmp_mean = 0
    for each in record:
        tmp_mean += sum(each[61:77])
    mean_totals.append(tmp_mean/len(record))

    # 10 77-86
    tenth = chosen_survey[77:87]
    totals.append(sum(tenth))
    tmp_mean = 0
    for each in record:
        tmp_mean += sum(each[77:87])
    mean_totals.append(tmp_mean/len(record))

    # 11 87-89
    eleventh = chosen_survey[87:90]
    totals.append(sum(eleventh))
    tmp_mean = 0
    for each in record:
        tmp_mean += sum(each[87:90])
    mean_totals.append(tmp_mean/len(record))

    # 12 90-94
    twelfth = chosen_survey[90:95]
    totals.append(sum(twelfth))
    tmp_mean = 0
    for each in record:
        tmp_mean += sum(each[90:95])
    mean_totals.append(tmp_mean/len(record))

    # 13 95-104
    thirteenth = chosen_survey[95:105]
    totals.append(sum(thirteenth))
    tmp_mean = 0
    for each in record:
        tmp_mean += sum(each[95:105])
    mean_totals.append(tmp_mean/len(record))

    # 14 105-114
    fourteenth = chosen_survey[105:115]
    totals.append(sum(fourteenth))
    tmp_mean = 0
    for each in record:
        tmp_mean += sum(each[105:115])
    mean_totals.append(tmp_mean/len(record))

    # We have totals (specific) and mean_totals (avg plot)
    return totals, mean_totals

    # # Now let's draw the side-by-side
    # import matplotlib.pyplot as plt
    # import numpy as np
    #
    # # Used for the x-axis
    # N = 14
    # width = 0.4
    # ind = np.arange(N)
    #
    # # Create the side-by-side plots
    # fig, ax = plt.subplots()
    # plot1 = ax.bar(ind, totals, width)
    # plot2 = ax.bar(ind+width, mean_totals, width)
    #
    # # Customisation of the plots
    # ax.set_title("Your horse against the average")
    # ax.set_xticks(range(1,15))
    # ax.set_xticklabels(labels, rotation=45, size=6)
    # ax.legend((plot1[0], plot2[0]),('Your horse','The average'))
    # plt.show()
    #
    # Previous version but less clear
    # plot1 = plt.bar(range(1,15), totals)
    # plot2 = plt.bar(range(1,15), mean_totals)
    #
    # plt.title("Your horse against the average")
    # plt.xlabel("Groupings")
    # plt.xticks(range(1,15), labels, rotation=45, size=6)
    # plt.legend((plot1[0], plot2[0]), ('Your horse','The average'))
    # plt.show()
