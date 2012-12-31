from collections import namedtuple
from movie_map import get_movie_dict_other

#New Field starts Here
#Movie Manager Calculates all the WarmUp problems.
def movie_manager():

    database=get_movie_dict_other("movie.data","ratings.data")
    movies_dict=database[0]
    #rating_movie_map=database[1]
    
    #Find Most Active User.
    user_activity_map={}
    user_activity_map=database[1]#get_user_activity("ratings.data")
    most_active_user_id=get_most_active_user(user_activity_map)
    print("\n\nMost Active User id = "+str(most_active_user_id)+"\n\tTotal Activities = "+str(user_activity_map[most_active_user_id])+"\n\n")
    #Found Most Active User.
    
    #Find Highest Rated Movie
    movie_id=find_highest_rated_movie(movies_dict)
    print("\n\nHighest Rated Movie = "+ str(movies_dict[movie_id][0])+" Average Rating = "+ "\n\t"+str(movies_dict[movie_id][4])+"\n\n")
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
    #for line in movies_dict:
        #rating_movie_map[movies_dict[line][4]]=movies_dict[line]

#Find most watched genre
    most_watched_genre=get_most_watched_genre(movies_dict)
    print("\n\nMost Watched Genre is "+ str(most_watched_genre))

#Find highest rated genre
    highest_rated_genre = get_highest_rated_genre(movies_dict)
    print("\nHighest Rated Genre is : "+str(highest_rated_genre))
#Movie Manager Ends Here.

Movie = namedtuple('Movie', ['title', 'year', 'rating'])




#New Field Starts Here.
#Movie Data File Handling goes here.
def get_movie_dict():
    my_map={}
    my_map[0] = ["Toy Story",1979,31.5,7,4.5,[0,3,4,6]]
    my_map[1] = ["SpiderMan",2001,86.6,20,4.33,[3,5]]
    my_map[2] = ["Harry Potter",2006,37.8,9,4.2,[2,4,5]]
    my_map[3] = ["James Bond",1999,80,16,5.0,[4,7,8]]
    my_map[4] = ["Rush Hour",1999,99,22,4.5,[6,8]]
    my_map[5] = ["SpiderMan2",2001,186.62,43,4.34,[1,2,3,4]]
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

def get_most_watched_genre(movies_dict):
    genre_frequency_list=[0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0]
    for movie_id in movies_dict:
        for genre_id in movies_dict[movie_id][5]:
            #movies_dict[movie_id][5][genre_id]
            genre_frequency_list[genre_id]+=1
    i=0
    max_genre=0
    for genre_val in genre_frequency_list:
        if genre_val > max_genre:
            max_genre=genre_val
            max_genre_index=i
        i+=1
    return max_genre_index
    
def get_highest_rated_genre(movies_dict):
    genre_rate_list=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    highest_rate_of_genre=0
    for movie_id in movies_dict:
        for genre_id in movies_dict[movie_id][5]:
            #movies_dict[movie_id][5][genre_id]
            genre_rate_list[genre_id]+=movies_dict[movie_id][2]
    i=0
    highest_rated_genre_index=0
    for rate_value in genre_rate_list:
        print("Genre = "+str(i)+" Value = "+str(rate_value))
        if rate_value > highest_rate_of_genre:
            highest_rated_genre_index=i
            highest_rate_of_genre=rate_value
        i+=1
    return [highest_rated_genre_index, highest_rate_of_genre]
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
