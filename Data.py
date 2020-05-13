import csv

class Read_data:

    def __init__(self,file_name):
        self.file_name = file_name

    def read(self):
        criteria =[]
        with open(self.file_name, mode='r') as csv_file:
            file_reader = csv.reader(csv_file, delimiter=",")
            line_count = 0
            for row in file_reader: 
                rowList = []       
                for values in row:
                    rowList.append(float(values))
                criteria.append(rowList)
                line_count += 1
            # this is just to show how many lines are in the file
            print('Processed {} lines from txt file.'.format(line_count))
        return criteria      
    
