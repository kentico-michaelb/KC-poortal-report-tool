import csv
import os

def get_api_counts(filename):

    # create a txt file to store the results
    report_file = open('api_totals_for_{}.txt'.format(filename),'w')
    
    # ensure that there is a .csv extension
    extension_parse = filename.split(".")

    if len(extension_parse) < 2:
        filename = filename + ".csv"

    # open the downloaded Poortal API report
    with open("poortal_reports/" + filename, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
        # skip the column headers
        next(spamreader, None)

        projects = {}

        # separate projects into dictionary data structure.  Example:
        # {12304123401234: {"ID": asdfapf92347034, "start_time": <date>, "end_time": <date>, "api_count":[20,30,40], "api_call_total: 90"}} 
        for row in spamreader:
            # ensure non-repeating, disctinct project ids
            if row[0] not in projects:
                projects[row[0]] = {"ID": row[0],"api_count":[],"api_call_total":0 }
            if row[0] == projects[row[0]]["ID"]:
                projects[row[0]]["api_count"].append(int(row[3]))
        # total the number of api calls per project and write to the report text file
        for project, values in projects.items():
            values["api_call_total"] = sum(values["api_count"])
            report_file.write("Project ID: {} | API Count Total: {} \n\n".format(values["ID"], values["api_call_total"]))
    report_file.close()            

# parse reports
#filename = input("What is the name of the API call report?")

# execute the function for each report downloaded to the local reports directory
for filename in os.listdir("poortal_reports"):
    api_counts = get_api_counts(filename)




        
            
        
