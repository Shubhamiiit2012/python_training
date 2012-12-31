def main():
    print("Hello World!!")    
    get_movie_dict_other("")

def get_movie_dict_other(movie_file):
    movies_dict={}
    fin=open("movie.data")
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
        
        #print(tokken[4])
        movies_dict[int(tokken[0])]=[name_tokken[0],movie_year,0,0,0,genre_list]
    fin=open("ratings.data")
    user_activity_map={}
    for line in fin:
        rating_tokken=line.split("\t")
        movies_dict[int(rating_tokken[1])][2]+=int(rating_tokken[2])
        movies_dict[int(rating_tokken[1])][3]+=1
        
    for movie_id in movies_dict:
        if movies_dict[movie_id][3] != 0:
            movies_dict[movie_id][4]=float(movies_dict[movie_id][2])/movies_dict[movie_id][3]
        print(movies_dict[movie_id])
if __name__ == "__main__":
    main()
