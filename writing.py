'''
Writing in python
'''

import os
import csv

output_path = os.path.join('.','new.csv')

with open(output_path,'w') as my_file:
    my_writer = csv.writer(my_file) # Delimiter?

    my_writer.write(['id','name','SSN'])
    my_writer.write(['1','Jose','5678'])