import csv

class Leaderboard:
    def __init__(self, filename="lb.csv"):
        self.filename = filename
        self.data = []

    '''
    Write the load function,
    it should read the data in the csv file,
    and append a dictionary of {name, score} in the list - data
    '''
    def load(self):
        self.data = []
        #write your code here
        file = csv.reader("/lb.csv")
        for data in file:
            dic = {data}
            data.append(dic)



    '''
    Write the save function that saves all the scores to the CSV file 
    in highest to lowest scores.
    '''
    def      save(self):
        self.data.sort(key=lambda x: x["Score"], reverse=True)
        with open  (self.filename, mode='w', newline='')      as file:
            fieldnames =    ["Name", "Score"]
            writer =    csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for entry in      self.data:
                writer.writerow(entry)


    '''
    Write the update function, 
    if the player already exists in the file then update the higher score
    else add a new row to the end of the file with name and score as columns
    '''
    def update(self, player_name, player_score):
        self.load()
        player_exists = False
        for entry in self.data:
            if entry["Name"] == player_name:
                if player_score > entry["Score"]:
                    entry["Score"] = player_score
                player_exists = True
                break
        if not player_exists:
            self.data.append({"Name": player_name, "Score": player_score})
        self.save()


    '''
    Display the scores of each and every person in the leaderboard
    '''
    def display(self):
        r = csv.reader('/lb.csv')
        for row in r:
            print(row)


