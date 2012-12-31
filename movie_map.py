
def get_movie_dict_other(movie_file, rating_file):
    movies_dict={}
    fin=open(movie_file)
    for line in fin:
        tokken=line.split("|")
        name_tokken=tokken[1].split("(")
        
        year_tokken=tokken[2].split("-")
        i=0
        genre_list=[]
        for obj in tokken:
            if i > 4:
                if cmp(obj,"1"):
                    x=0
                else :
                    genre_list.append(i-5)
            i+=1
        for year in year_tokken:
            movie_year=year

        movies_dict[int(tokken[0])]=[name_tokken[0],movie_year,0,0,0,genre_list]
    fin=open(rating_file)
    user_activity_map={}
    for line in fin:
        rating_tokken=line.split("\t")
        movies_dict[int(rating_tokken[1])][2]+=int(rating_tokken[2])
        movies_dict[int(rating_tokken[1])][3]+=1
        if int(rating_tokken[0]) in user_activity_map:
            user_activity_map[int(rating_tokken[0])]+=1
        else :
            user_activity_map[int(rating_tokken[0])]=1
        
    for movie_id in movies_dict:
        if movies_dict[movie_id][3] != 0:
            movies_dict[movie_id][4]=float(movies_dict[movie_id][2])/movies_dict[movie_id][3]
        
    return (movies_dict, user_activity_map )
