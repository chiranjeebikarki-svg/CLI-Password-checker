import csv

while True:

        task = input("Enter the task: ").strip()

        if task.lower() == "quit": 
            print("bye-bye")
            break
        
        with open("clis.csv", mode = "a", newline = "") as file:
            writer = csv.writer(file)
            writer.writerow([task])

        with open("clis.csv", mode = "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row[0])

    



