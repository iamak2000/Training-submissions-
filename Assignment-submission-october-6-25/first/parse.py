import csv

def parse_csv(file_path):
    try:
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)  
            print("CSV Headers:", csv_reader.fieldnames)
            print("-" * 40)
            
            for row in csv_reader:
                print(row)  
          
    
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    file_path = "data.csv"
    parse_csv(file_path)