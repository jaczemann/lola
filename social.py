from datetime import *
from random import *
import allowedcharacters as ac


# default user, needs to be moved to users database
defaultUser = {
    "user": "Default User",
    "userID": 5000
}


posts = {
    784125685467139: {
        "time": "10/31/2020 10:15 PM",
        "user": "jacobze",
        "userID": 883749524,
        "label": "first note",
        "body": "Hello, this is first note in this list.",
        "rating": 0,
        "likees": [],
        "comments":{
            0: {
                "user": "jacobze",
                "userID": 883749524,
                "time": "10/31/2020 11:35 PM",
                "body": "Hello, this is first comment on this post!",
                "rating": 1
            }
        }
    }
}


# print full information about a post
# print(posts[0])

# print how many comments is under a post
# print(len(posts[0]["comments"]))

# add a comment to a specific post
def AddComment(postID = None, userID = defaultUser["userID"], body = None):

    ### This is testing sequence that verfies that all data required are available
    ### If the tests fail, the comment cannot be created

    # a list of errors for testing sequence
    testStatus = {
        "Error 01": None, # check if there is no post to comment on / in case no postID is available
        "Error 02": None, # check if the mother post does not exist / in case postID is available but is not valid
        "Error 03": None  # check if there is no body for the comment
    }

    # check if there is no post to comment on / in case no postID is available
    if postID == None:
        testStatus["Error 01"] = True

    # check if the mother post does not exist / in case postID is available but is not valid
    if postID not in posts:
        testStatus["Error 02"] = True
    
    # check if there is no body for the comment
    if body == None or body == "":
        testStatus["Error 03"] = True
    
    ### END

    # In case any tests fail, print error
    if testStatus["Error 01"] == True or testStatus["Error 02"] == True or testStatus["Error 03"] == True:
        failedTests = []
        for item in testStatus:
            if testStatus[item] == True:
                failedTests.append(item)

        print(testStatus)
        print("One of the Errors {} occured when creating a comment.".format(str(failedTests)))

    # If the tests pass, assemble a comment and attach it to a post
    else:

        # calculates suitable ID for the comment
        commentID = len(posts[postID]["comments"])

        # what day is it today / already nicely formatted
        timestamp = datetime.today().strftime("%m/%d/%y %H:%M")


        # assembles the comment / puts it into brackets
        comment = {"userID": userID, "time": timestamp, "body": body, "rating": 0, "likees":{}}    

        # adds the comment to the post
        posts[postID]["comments"][commentID] = comment



AddComment(784125685467139, 883749524, "very cool, cant wait for more!")
# AddComment("hello, this is first comment added by a method")
# AddComment("hi! this is another comment for fun!")




# add a post to a main page
def AddPost(userID = defaultUser["userID"], label = None, body = None):

    ### Check if data are available

    # list of errors
    testStatus = {
        "Error 01": None, # check if the user is not loged in
        "Error 02": None, # check if the label is empty
        "Error 03": None, # check if the body is empty
        "Error 04": None, # check if the characters are allowed
        "Error 05": None, # check if the input has correct length
    }

    # check if the user is not loged in / and therefor loged in as Default User
    if userID == defaultUser["userID"]:
        testStatus["Error 01"] = True    

    # check if the label is empty
    if label == None or label == "":
        testStatus["Error 02"] = True

    # check if the body is empty
    if body == None or body == "":
        testStatus["Error 03"] = True


    # check if the characters given in the body are allowed
    bodycharcheck = []
    for character in body.lower():
        if (character not in ac.ac):
            bodycharcheck.append(False)
        else:
            bodycharcheck.append(True)


    # check if the characters given in the label are allowed
    labelcharcheck = []
    for character in label.lower():
        if (character not in ac.ac):
            labelcharcheck.append(False)
        else:
            labelcharcheck.append(True)



    if False in labelcharcheck:
        testStatus["Error 04"] = True

    if False in bodycharcheck:
        testStatus["Error 04"] = True


    # check if the lenght is under the maximum allowed value
    if len(label) > 50:
        testStatus["Error 05"] = True

    if len(body) > 450:
        testStatus["Error 05"] = True 


    ### END

    # In case any tests fail, print error
    if testStatus["Error 01"] == True or testStatus["Error 02"] == True or testStatus["Error 03"] == True or testStatus["Error 04"] == True or testStatus["Error 05"] == True:
        failedTests = []
        for item in testStatus:
            if testStatus[item] == True:
                failedTests.append(item)

        print(testStatus)
        print("One of the Errors {} occured when creating a post.".format(str(failedTests)))

    else:

        """ Assign user to USER ID """
        # calculates unique ID for the post
        postIDstatus = False

        while postIDstatus == False:
            postID = randrange(100000000000, 999999999999)

            # checks if the postID is already taken;  False means TAKEN,  True means AVAILABLE
            if postID not in posts:
                postIDstatus = True

        # what day is it today / already nicely formatted
        timestamp = datetime.today().strftime("%m/%d/%y %H:%M")

        # assembles the post
        post = {"time": timestamp, "userID": userID, "user": None, "label": label,"body": body, "rating": 0, "likees": {},"comments":{}}    

        # attaches the post to posts{}
        posts[postID] = post


def LikePost(userID=defaultUser["userID"], postID=None):

    # verifies that user is logged in
    if userID == defaultUser["userID"]:

        # prints error
        print("The user must be logged in.")

    # verifies that the likee is unique
    elif userID in posts[postID]["likees"]:

        print("The user already liked this post.")

        # adds a like to the post
    else:
        posts[postID]["rating"] += 1
        posts[postID]["likees"].append(userID)


def LikeComment(userID=defaultUser["userID"], postID=None, commentID=None):

    # verifies that user is logged in
    if userID == defaultUser["userID"]:

        # prints error
        print("The user must be logged in.")

    # verifies that the likee is unique
    elif userID in posts[postID][commentID]["likees"]:

        print("The user already liked this comment.")

        # adds a like to the comment
    else:
        posts[postID][commentID]["rating"] += 1
        posts[postID][commentID]["likees"].append(userID)




def UnlikePost(userID=defaultUser["userID"], postID=None):

    # verifies that user is logged in
    if userID == defaultUser["userID"]:

        # prints error
        print("The user must be logged in.")

    # verifies that the user is in likees
    if userID not in posts[postID]["likees"]:

        pass

        # subtracts a like from the post
    else:
        posts[postID]["rating"] -= 1
        posts[postID]["likees"].remove(userID)


def UnlikeComment(userID=defaultUser["userID"], postID=None, commentID=None):

    # verifies that user is logged in
    if userID == defaultUser["userID"]:

        # prints error
        print("The user must be logged in.")

    # verifies that the user is in likees
    if userID not in posts[postID][commentID]["likees"]:

        pass

        # subtracts a like from the comment
    else:
        posts[postID][commentID]["rating"] -= 1
        posts[postID][commentID]["likees"].remove(userID)

AddPost(userID=883749524, label="ssssssssssssssssss", body="fff")