from collections import namedtuple

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
    for line in highest_rated_movie_by_year:
        print("Highest Rated Movie Of Year "+str(line)+" : "+str(movies_dict[highest_rated_movie_by_year[line]]))
    #Found Highest Rated Movie By Year

#Find Most Watched Movie
    most_watched_movie_id=find_most_watched_movie(movies_dict)
    print("\n\nMost Watched Movie : "+ str(movies_dict[most_watched_movie_id])+"\n\n")
#Found Most Watched Movie
    #for line in movies_dict:
    #   for i in movies_dict[line]:
    #       print(i)
    for line in movies_dict:
        rating_movie_map[movies_dict[line][4]]=movies_dict[line]
    for line in rating_movie_map:
        print(str(line)+" : "+str(rating_movie_map[line]))
#Movie Manager Ends Here.

Movie = namedtuple('Movie', ['title', 'year', 'rating'])
#New Field Starts Here.
#Movie Data File Handling goes here.
def get_movie_dict():
    my_map={}
    my_map[0] = ["Toy Story",1979,31.5,7,4.5]
    my_map[1] = ["SpiderMan",2001,86.6,20,4.33]
    my_map[2] = ["Harry Potter",2006,37.8,9,4.2]
    my_map[3] = ["James Bond",1999,80,16,5.0]
    my_map[4] = ["Rush Hour",1999,99,22,4.5]
    my_map[5] = ["SpiderMan2",2001,186.62,43,4.34]
    return my_map

def find_highest_rated_movie(movies_dict):
    highest_rated_movie_id=0
    highest_rating=0
    
    for movieid in movies_dict:
        if movies_dict[movieid][4] > highest_rating:
            highest_rating = movies_dict[movieid][4]
            highest_rated_movie_id = movieid
    return highest_rated_movie_id

def find_highest_rated_movie_by_year(movies_dict):
    rating_by_year_map={}
    
    for line in movies_dict:
        if movies_dict[line][1] in rating_by_year_map:
            if movies_dict[line][2] > movies_dict[rating_by_year_map[movies_dict[line][1]] ][2]:
                rating_by_year_map[movies_dict[line][1]] = line
        else :
            rating_by_year_map[movies_dict[line][1]]=line
    return rating_by_year_map

def find_most_watched_movie(movies_dict):
    most_watched_movie_id=0
    watching_frequency=0
    for movie_id in movies_dict:
        if movies_dict[movie_id][3]>watching_frequency:
            watching_frequency=movies_dict[movie_id][3]
            most_watched_movie_id=movie_id
    return most_watched_movie_id
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
