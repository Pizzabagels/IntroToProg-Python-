#csv and pickle module import
import csv, pickle
#definition of readcsv function that takes CSV's and processes information back to the user as variable a
###ONLY WORKS WHEN FILES ARE FORMATED AS CSV'S!!!
def readcsv(filename):
    try:
        ###opens passed parameter filename and sorts using comma separation
        ifile = open(filename, "r")
        reader = csv.reader(ifile, delimiter=",")
        next(reader)
        a = []
        ###loop that iterates over rows in CSV
        for row in reader:
            unit_request = {
                "PO": row[0],
                "Serial Number": row[1],
                "Asset": row[2],
                "Manufacturer": row[3],
                "Platform": row[4],
                "Site": row[5],
                "Floor": row[6],
                "Role": row[7],
                "name": row[8]
            }
            ###adds unit request dictionaries to list a
            a.append(unit_request)
        ifile.close()
        ###file is closed and variable is returned to the program
        return a
    ###error checking for common errors
    except FileNotFoundError:
        print("file not found please check tracking.csv location and try again")
    except IndexError:
        print("please ensure that CSV consists of 9 columns")
def output_check():
    try:
        x = pickle.load(open("tommy_pickles.p", "rb"))
        print("saved pickle output : " + str(x))
    except FileNotFoundError:
        print("File not found please make sure tommy_pickles is in the right directory")
###imported file input
file = "tracking.csv"
###returned csv output as pickle_output
pickle_output = readcsv(file)
###start of pickle.dump method to take the processed output from the readcsv function and save it as a pickle
pickle.dump(pickle_output, open("tommy_pickles.p", "wb"))
#checking output for user
output_check()