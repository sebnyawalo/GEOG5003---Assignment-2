import csv

class Read_data:
    """
    A class used to read data into the model
    requires csv library to run.
    ...

    Attributes
    ----------
    file_name : str
        a formatted string that represent the file name.

    Methods
    -------
    read()
        use the csv library to read data from a file;
    """
    def __init__(self,file_name):
        """
        Parameters
        ----------
        name : str
            the name of the file
        """
        self.file_name = file_name

    def read(self):
        """
        reads and returns a list of the content of the file name passed.
        """
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
    
