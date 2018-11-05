import requests
import numpy as np
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
    records = []

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
        for i in range(3,24):
            try:
                final.append(int(tmp_split[i]))
            except ValueError:
                final.append(5)
        for i in range(25,len(tmp_split)):
            try:
                final.append(int(tmp_split[i]))
            except ValueError:
                final.append(5)

        records.append(final)

    # Convert all record values here:
    record = np.array(records)
    record = np.delete(record,np.s_[20],axis=1)
    record = np.delete(record,np.s_[3],axis=1)
    record = np.delete(record,np.s_[2],axis=1)
    record = np.delete(record,np.s_[1],axis=1)
    record = np.delete(record,np.s_[0],axis=1)

    for x in record:
        for y in range(0,len(x)):
            if x[y] <= 0 or x[y] >= 6:
                x[y] = 0
            else:
                x[y] = 5 - x[y]
        print(x)

    # Our specified record
    chosen_survey = record[record_id - 1]
    totals = []
    mean_totals = []

    # Here we go through and sort by groupings
    # Must account for the negative attributes/scores
    # Determined by the .docx file
    # 1 0-5 (All positive)
    first = chosen_survey[0:5]
    # Recalculate totals
    tmp_total = 0
    for x in first:
        tmp_total += x
    totals.append(tmp_total)
    tmp_mean = 0
    for each in record:
        tmp_mean += sum(each[0:5])
    mean_totals.append(tmp_mean/len(record))

    # 2 5-15 (first 4 positive, rest negative)
    second = chosen_survey[5:15]
    # Recalculate totals
    tmp_total = 0
    for x in second:
        tmp_total += x
    totals.append(tmp_total)
    tmp_mean = 0
    for each in record:
        tmp_mean += sum(each[5:15])
    mean_totals.append(tmp_mean/len(record))

    # 3 15-21 (all negative)
    third = chosen_survey[15:23]
    # Recalculate totals
    tmp_total = 0
    for x in third:
        tmp_total += x
    totals.append(tmp_total)
    tmp_mean = 0
    for each in record:
        tmp_mean += sum(each[15:23])
    mean_totals.append(tmp_mean/len(record))

    # 4 21-31 (5 positive, 3 negative, 1 positive, 1 negative)
    fourth = chosen_survey[23:43]
    # Recalculate totals
    tmp_total = 0
    for x in fourth:
        tmp_total += x
    totals.append(tmp_total)
    tmp_mean = 0
    for each in record:
        tmp_mean += sum(each[23:43])
    mean_totals.append(tmp_mean/len(record))

    # 5 31-49 (all negative)
    fifth = chosen_survey[43:57]
    # Recalculate totals
    tmp_total = 0
    for x in fifth:
        tmp_total += x
    totals.append(tmp_total)
    tmp_mean = 0
    for each in record:
        tmp_mean += sum(each[43:57])
    mean_totals.append(tmp_mean/len(record))

    # 6 49-57 (6 negative, 2 positive)
    sixth = chosen_survey[57:69]
    # Recalculate totals
    tmp_total = 0
    for x in sixth:
        tmp_total += x
    totals.append(tmp_total)
    tmp_mean = 0
    for each in record:
        tmp_mean += sum(each[57:69])
    mean_totals.append(tmp_mean/len(record))

    # 7 57-63 (all negative)
    seventh = chosen_survey[69:79]
    # Recalculate totals
    tmp_total = 0
    for x in seventh:
        tmp_total += x
    totals.append(tmp_total)
    tmp_mean = 0
    for each in record:
        tmp_mean += sum(each[69:79])
    mean_totals.append(tmp_mean/len(record))

    # 8 63-66 (all negative)
    eighth = chosen_survey[79:85]
    # Recalculate totals
    tmp_total = 0
    for x in eighth:
        tmp_total += x
    totals.append(tmp_total)
    tmp_mean = 0
    for each in record:
        tmp_mean += sum(each[79:85])
    mean_totals.append(tmp_mean/len(record))

    # 9 66-78 (all negative)
    ninth = chosen_survey[85:105]
    # Recalculate totals
    tmp_total = 0
    for x in ninth:
        tmp_total += x
    totals.append(tmp_total)
    tmp_mean = 0
    for each in record:
        tmp_mean += sum(each[85:105])
    mean_totals.append(tmp_mean/len(record))

    # 10 78-83 (all negative)
    tenth = chosen_survey[105:115]
    # Recalculate totals
    tmp_total = 0
    for x in tenth:
        tmp_total += x
    totals.append(tmp_total)
    tmp_mean = 0
    for each in record:
        tmp_mean += sum(each[105:115])
    mean_totals.append(tmp_mean/len(record))

    # 11 83-86 (negative)
    eleventh = chosen_survey[115:121]
    # Recalculate totals
    tmp_total = 0
    for x in eleventh:
        tmp_total += x
    totals.append(tmp_total)
    tmp_mean = 0
    for each in record:
        tmp_mean += sum(each[115:121])
    mean_totals.append(tmp_mean/len(record))

    # 12 86-91 (3 positive, 1 negative, 1 positive)
    twelfth = chosen_survey[121:131]
    # Recalculate totals
    tmp_total = 0
    for x in twelfth:
        tmp_total += x
    totals.append(tmp_total)
    tmp_mean = 0
    for each in record:
        tmp_mean += sum(each[121:131])
    mean_totals.append(tmp_mean/len(record))

    # 13 91-100 (negative)
    thirteenth = chosen_survey[131:149]
    # Recalculate totals
    tmp_total = 0
    for x in thirteenth:
        tmp_total += x
    totals.append(tmp_total)
    tmp_mean = 0
    for each in record:
        tmp_mean += sum(each[131:149])
    mean_totals.append(tmp_mean/len(record))

    # 14 100-111 (negative)
    fourteenth = chosen_survey[149:len(record)]
    # Recalculate totals
    tmp_total = 0
    for x in fourteenth:
        tmp_total += x
    totals.append(tmp_total)
    tmp_mean = 0
    for each in record:
        tmp_mean += sum(each[149:len(record)])
    mean_totals.append(tmp_mean/len(record))

    # We have totals (specific) and mean_totals (avg plot)
    return totals, mean_totals
