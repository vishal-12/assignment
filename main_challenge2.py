
'''
        SECOND CHALLENGE
        This is the data driven script which will call all REST Methods [PUT,PATCH,DELETE,GET]
        Website https://gorest.co.in/   does not have API for refreshing or creating the tokens so add token in the config file directly

        This will create the log file in the log directory with latest date and time
'''
from logger.logger import logging
import os
from challenge2.challenge2 import Challenge2

############## Logging################
logging = logging()
logging.set_log_file("")
current_dir = os.path.dirname(os.path.abspath(__file__))
config_file = os.path.join(current_dir, "config", "test.json")

if __name__=='__main__':

    obj = Challenge2(config=config_file)

    #Authenticate a user by obtaining an authentication token using valid credentials.
    #Verify that the authentication is succcessful by checking the response st+atus and extracting the token.
    baseUrl = obj.getBaseUrl()
    name = obj.body.get("name")
    if obj.getPk(baseUrl) == -1:
        logging.info(f"User {name} NOT_FOUND Going to create user")
        if obj.runAllApiMethods(url=baseUrl,method='POST',body=obj.getbody())!=-1:
            logging.info(f"User {name} CREATED")
        else:
            logging.error("EXIT",100,ex=True)

    #Get Primary Key
    logging.info(f"GET Primary Key")
    pk = obj.getPk(baseUrl)
    if pk == -1:
        logging.error("Either User Does not exist r check User Once again, Ok can't be None", 100, ex=True)
    logging.info(f"GET Primary Key Block Completed")

    #Use the obtained token to make requests to retrieve and validate user profile information.
    logging.info(f"CONCAT PK - {pk}")
    obj.concatInBaseUrl(pk)
    newUrl = obj.getNewUrl()
    logging.info(f"NEW URL- {pk}")

    logging.info("RETRIVE Profile Information")
    if obj.runAllApiMethods(url=newUrl)==-1:
        logging.error("EXIT", 100, ex=True)


    #Update the user's profile information (e.g., change the display name).
    logging.info("Calling PUT Method")
    putBbody = obj._vConfig["putCall"]
    obj.patchBody(putBbody)
    if newUrl is None:
        logging.error("Error in concat the pk in new url, Hint self.__vConfig[newUrl]",100,ex=True)
    if obj.runAllApiMethods(url=newUrl, method='PUT', body=obj.getbody())==-1:
        logging.error("EXIT", 100, ex=True)
    logging.info("Calling PUT Completed")

    logging.info("RETRIVE Profile Information")
    if obj.runAllApiMethods(url=newUrl)==-1:
        logging.error("EXIT", 100, ex=True)

    #Update the user's profile information (e.g., change the display name).
    logging.info("Calling Patch Method")
    patchBbody = obj._vConfig["patchCall"]
    obj.patchBody(patchBbody)
    if newUrl is None:
        logging.error("Error in concat the pk in new url, Hint self.__vConfig[newUrl]",100,ex=True)
    if obj.runAllApiMethods(url=newUrl, method='PATCH', body=obj.getbody())==-1:
        logging.error("EXIT", 100, ex=True)
    logging.info("Calling Patch Completed")

    logging.info("RETRIVE Profile Information")
    if obj.runAllApiMethods(url=newUrl)==-1:
        logging.error("EXIT", 100, ex=True)

    #delete
    logging.info("Deleting USER")
    if obj.runAllApiMethods(url=newUrl,method="DELETE")==-1:
        logging.error("EXIT", 100, ex=True)

    logging.exit_log()