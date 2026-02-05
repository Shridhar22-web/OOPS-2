class instagram:
    def __init__(self,title,description,creator_name,location):
        self.title=title
        self.description=description
        self.creator_name=creator_name
        self.location=location
        self.likes=0
        self.comments=[]

    def display_title(self):
        print("title of the reel is:",self.title)
    
    def display_description(self):
        print("description of th reel is:",self.description)

    def display_creator_name(self):
        print("creatorof the reel is:",self.creator_name)

    def display_location(self):
        print("location is",self.location)

    def liked(self):
        self.likes+=1
    
    def disliked(self):
        if self.likes >= 1:
            self.likes-=1
    
    def display_likes(self):
        print("mumber of likes to he reel is:",self.likes)

    def display_comments(self):
        if len(self.comments)==0:
            print("no comments yet")
        else:
            print("comments are:",self.comments)   

    def add_coments(self):
        self.comments.append("shridhar")
    
    def delete_comment(self):
        temp_comment=self.comments.pop()
        print("deleted comment is:",temp_comment)
    
reel1= instagram("rolex","a gangster","shri","kunigal")
reel1.display_comments()
reel1.display_creator_name()
reel1.display_description()
reel1.display_location()
reel1.liked()
reel1.display_title()
reel1.display_likes()
reel1.add_coments()
reel1.delete_comment()
reel1.disliked()

    
