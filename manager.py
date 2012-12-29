#New Field starts Here
#Movie Manager Calculates all the WarmUp problems.
def movie_manager():

    movies_dict={}
    movies_dict=get_movie_dict()
    rating_movie_map={}
    
    #Find Most Active User.
    user_activity_map={}
    user_activity_map=get_user_activity("ratings.data")
    most_active_user_id=get_most_active_user(user_activity_map)
    print("\n\nMost Active User id = "+str(most_active_user_id)+"\n\tTotal Activities = "+str(user_activity_map[most_active_user_id])+"\n\n")
    #Found Most Active User.
    
    #Find Highest Rated Movie
    movie_id=find_highest_rated_movie(movies_dict)
    print("\n\nHighest Rated Movie = "+ str(movies_dict[movie_id])+"\n\n")
    #Found Highest RatedMovie
    
    #Find Highest Rated Movie By Year
    highest_rated_movie_by_year=find_highest_rated_movie_by_year(movies_dict)
    #Found Highest Rated Movie By Year

    #for line in movies_dict:
    #   for i in movies_dict[line]:
    #       print(i)
    for line in movies_dict:
        rating_movie_map[movies_dict[line][2]]=movies_dict[line]
    for line in rating_movie_map:
        print(str(line)+" : "+str(rating_movie_map[line]))
#Movie Manager Ends Here.    

#New Field Starts Here.
#Movie Data File Handling goes here.
def get_movie_dict():
    my_map={}
    my_map[0]=("Toy Story",1979,4.5)
    my_map[1]=("SpiderMan",2001,4.33)
    my_map[2]=("Harry Potter",2006,4.2)
    my_map[3]=("James Bond",1999,5.0)
    my_map[4]=("Rush Hour",1999,4.5)
    return my_map

def find_highest_rated_movie(movies_dict):
    movie_id=0
    highest_rating=0
    
    for line in movies_dict:
        if movies_dict[line][2]>highest_rating:
            highest_rating=movies_dict[line][2]
            movie_id = line
    return movie_id

def find_highest_rated_movie_by_year(movies_dict):
    rated_by_year_map={}
    

#Movie Data File Handling ends here.

#New Field Starts Here.
#user Activity Related

def get_user_activity(rating_file):

    user_activity_map={}
    user_activity_map[0]=7
    user_activity_map[1]=22
    user_activity_map[2]=4
    user_activity_map[3]=55
    user_activity_map[4]=8
    return user_activity_map

def get_most_active_user(user_activity_map):
    user_id=0
    highest_rating=0
    for line in user_activity_map:
        if user_activity_map[line] > highest_rating:
            user_id=line
            highest_rating=user_activity_map[line]
    return user_id

#User Activities Related
