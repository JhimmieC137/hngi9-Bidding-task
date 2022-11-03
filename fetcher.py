import csv
import json 
from hasher import encryption  #imports the SHA-256 encryption function from hasher.py file


'''
The jsonifier function converts a csv file to a json file by reading 
through each row of the csv file and hashes the json output of each row.
Then it creates a new csv file containing records from the previous csv 
file and a new column of the hashed json files.
'''

def jsonifier(csvPath):
    big_data = []   #The list to contain smaller list of data from each row of the csv file 
    hashes = []    #The list to contain all hashed json files
    
    with open(csvPath, encoding='utf-8') as csvf: 
        csvReader = csv.DictReader(csvf)  # Opens and reads through the csv file
        
        '''
        The loop runs through the csv file for as many rows exists in the csv file
        '''
        for row in csvReader:
            data = {}
            key = row['Series Number']
            data[key] = row
            
            filename = 'row_for_{}.json'.format(row['Filename'])
            with open( filename, 'w', encoding='utf-8') as jsonf:
                jsonf.write(json.dumps(data, indent=4))     #Json files are created per row with different names 
                
                
            with open(filename,'rb') as f: #Each json file is opened and hashed
                data = f.read()
            hash = encryption(data)
            hashes.append(hash)
            
            row.update({'SHA-256': hash})  #Each row is then updated with the respective hashed json  
            
            small_data = []   #A small list to contain each rows data
            for value in row.values(): 
                small_data.append(value)   #Each row append to a small list
            big_data.append(small_data)   #Each small list is appended to the big list 
            
    
        
    header = ['Series Number','Filename','Description','Gender','UUID','Hash','SHA-256'] #The header for the new csv file.
    
    with open('filename.output.csv', 'w') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(header)
        for data in big_data:
            writer.writerow(data)   #Csv file is written row by row, small list by small list, from the big list of data.

        
jsonifier('Team_Bevel.csv')  #function is called here