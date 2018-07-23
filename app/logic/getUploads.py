'''
Purpose Of File: To hold all of the functions for app.courses
'''
from app.allImports import *
from app.logic import databaseInterface  

class GetUploads():
  def __init__(self, file):
    self.file   = file
  
  def getAbsolutePath(self, relativePath, filename=None, makeDirs=False):
    '''Creates the AbsolutePath based off of the relative path.
    Also creates the directories in path if they are not found.
    @param {string} relaitivePath - a string of directories found in config.yaml
    @param {string} filename - the name of the file that should be in that directory
    @return {string} filepath -returns the absolute path of the directory'''
    '''TODO: ADD @PARAm for make dirs'''
    filepath = os.path.join(sys.path[0], relativePath)
    if makeDirs == True:
        try:
            os.makedirs(filepath)
        except:
            pass
    if filename != None:
        filepath = os.path.join(filepath, filename)
    return filepath

  def get_upload_path(self):
    #We need the app in the front in order to mkdir
    #upload_file_path = 'app/' + cfg['fileOperations']['dataPaths']['uploads']
    relative_path=cfg['fileOperations']['dataPaths']['uploads']
    upload_file_path=self.getAbsolutePath(relative_path)
    #previous hardcoded version: upload_file_path = '/var/www/html/bcsr-flask/app/' + cfg['fileOperations']['dataPaths']['uploads']
    app.logger.info("Upload file path: {0}".format(upload_file_path))
    return upload_file_path

  def get_course_path(self,CID):
    course_info = databaseInterface.get_course_info(CID)
    course_file_path       = (  "/" 
                                +  str(course_info.SEID.SEID) 
                                + "/" 
                                + str(course_info.PID.DID.name) 
                                + "/" 
                                + str(course_info.prefix) 
                                + "/"
                              ).replace(" ","")
    app.logger.info("Course file path: {0}".format(course_file_path))
    return course_file_path
    
  def check_path_exist(self,path):
    if not os.path.exists(path):
        try:
          app.logger.info("Trying to make directories: {0}".format(path))          
          os.makedirs(path)
          app.logger.info("Directories made: {0}".format(path))
        except OSError as e:
          print e.errno
          app.logger.error("Error making directories: {0}".format(e.errno))
          pass
    return 0
    
  def create_filename(self,CID, user_name):
    course_info = databaseInterface.get_course_info(CID)
    new_file_name          = (    'CID' 
                                + str(course_info.CID) 
                                + '-' 
                                + str(course_info.prefix) 
                                +  '-' 
                                + str(course_info.number) 
                                + '-' 
                                + str(course_info.PID.DID.name) 
                                + '-' 
                                + user_name
                                + "." 
                                + str(self.file.filename.split(".").pop())
                              ).replace(" ","")
    app.logger.info("Filename created: " + new_file_name)
    return new_file_name
  
        
    
         
    
        
    
        
    