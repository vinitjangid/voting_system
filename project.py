nom_1 = input("enter the nominee 1 name : ")
nom_2 = input("enter the nominee 2 name : ")

nom_1_votes = 0
nom_2_votes = 0

voter_id = [1,2,3]
num_of_voter = len(voter_id)

while True:
    if voter_id == []:
        print("voting session over")
        if nom_1_votes>nom_2_votes:
            percent = (float(nom_1_votes)/num_of_voter)*100
            print(str(nom_1) + " has won by " + str(percent) + "% votes")
            break
        elif nom_2_votes>nom_1_votes:
            percent = (float(nom_2_votes)/num_of_voter)*100
            print(str(nom_2) + " has won by " + str(percent) + "% votes")
            break
        else:
            print("no one wins, both gets 50% voting")
    else:
        voter = int(input("enter your voter id number :"))
        if voter in voter_id:
            print("you are a voter ")
            voter_id.remove(voter)
            vote = int(input("enter your vote for nominee 1 or 2 :"))
            if vote == 1:
                nom_1_votes+=1
                print("thanks for casting your vote")
            elif vote == 2:
                nom_2_votes+=1
                print("thanks for casting your vote")
        else:
            print("you are not a voter or you alredy voted")
