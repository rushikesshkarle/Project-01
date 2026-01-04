import os 
import json 
import argparse
import csv



def parse_json(file_path):
     with open(file_path,"r") as f:
       data=json.load(f)
       return data



def parse_csv(file_path):
    with open(file_path,"r") as f:
       reader=csv.reader(f)
       data=[]
       for row in reader:
          data.append(row)
    return data




def parse_txt(file_path):
    with open(file_path,"r") as f:
     data=f.read()
     return data
     

def main():
     parser = argparse.ArgumentParser(
        description="File Parser CLI Tool"
    )
     parser.add_argument("file", help="Path to the file")

     args = parser.parse_args()

     file_path = args.file
     
     if not os.path.exists(file_path):
        print("File not found") 

     ext=os.path.splitext(file_path)[1].lower()

     if ext==".json":
        result=parse_json(file_path)
     elif ext==".csv":
        result=parse_csv(file_path)
     elif ext==".txt":
        result=parse_txt(file_path)
     else:
        print("Invalid extenstion")
        return 
    
     print("Parsing done successfully")
     print("Parsed data : ",result)

   
if __name__=="__main__":
    main()