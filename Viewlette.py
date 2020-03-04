import random

def Viewlette(Movielist,newmovieinput):

    with open(Movielist) as file:
        movieliststring = file.read()
        
    movielist = movieliststring.splitlines()

    #print("movielist is", movielist)

    if newmovieinput== "":
        newmovielist = movielist
    else:
        movielist.append(newmovieinput)
        newmovielist = movielist
    randommovie = random.choice(newmovielist)
    print(randommovie)

    print("Have you seen this movie? Yes or No?")
    watched = input()

    
    if watched == "yes":
        newmovielist.remove(randommovie)
        print(randommovie, "removed from list")
    else:
        print("list remains unchanged")
    
    nonduplicatenewmovielist = list(dict.fromkeys(newmovielist)) #checkforduplicates

    movielistfile = open(Movielist,"w")
    for element in nonduplicatenewmovielist:
        movielistfile.write(element)
        movielistfile.write('\n')
    movielistfile.close()

    


Viewlette("movieslist.txt","borno")

