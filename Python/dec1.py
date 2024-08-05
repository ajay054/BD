import _mysql_connector
try:
    conn = _mysql_connector.connect(user="root", password="Aj@y_054", port=5432, host="localhost")
    homeCursor = conn.cursor()
    
except Exception as e:
    print(e)
else:
    print("Database Connected.")
    
    #Create a decorator for checking user credentials.
    
    def outerFunction(originalFunction):
        def innerFunction():
            userName = input("please enter username")
            password = input("Please enter password")
            homeCursor.execute(f"SELECT gmail FROM credentials.users where username='{userName}' and password='{password}';")
            mail = homeCursor.fetchone()
            
            if mail is not None:
                return originalFunction()
            else:
                return "you have no access to get the movie details"
        return innerFunction
    

@outerFunction
def getMyData():
    homeCursor.execute(f"SELECT * FROM bulkratings_info.tutorialstution_movies_list;")
    movieData = homeCursor.fetchall()
    return movieData


movieData = getMyData()
if type(movieData).__name__ == 'tuple':
    for movie in movieData:
        print(movie)
else:
    print(movieData)