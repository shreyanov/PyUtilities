# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 12:31:59 2021

@author: Vivek Srivastava
"""
import os, sys, io
class CustomLogger:
    
    '''
    target_dir  = Where would you like your log  file to be generated ?
    file_name   = What is the name you would like to give your log file ?
    delete_file = Would you like your log file to be generated in the end ?
    Logger_Object = CustomLogger(target_dir = os.getcwd(), file_name = 'Hello World.txt', delete_file = 'No')
    print("This is a custom Logger?\n")
    print("Use it to Log Python Output in a file")
    Logger_Object.Exit_Logger()

    '''
    
    def __init__(self, target_dir = os.getcwd() , file_name = 'Process_Log.txt', delete_file = 'No'):
        
        '''Check if the log file needs to be deleted after Logger Exits'''
        self.DELETE_FILE    = delete_file
        self.TARGET_DIR     = target_dir
        self.FILE_NAME      = file_name
        self.INITIAL_STDOUT = sys.stdout
        self.FILE_PATH      = os.path.join(self.TARGET_DIR, self.FILE_NAME)
        self.Start_Logger()
       
    def Start_Logger(self):
        self.Get_Rid_Of_Existing_Log()
        print('\n' + '/'*60 + '\n')
        print(f'Starting to Log Data in {self.FILE_PATH}')
        self.LOGFILE        = open(self.FILE_PATH, 'w+')
        sys.stdout          = self.LOGFILE 
        self.NEW_STDOUT     = sys.stdout
    
    def write(self, message):
        self.LOGFILE.write(message)
        self.INITIAL_STDOUT.write(message)
        self.INITIAL_STDOUT.flush()
        self.LOGFILE.flush()
        return self
    
    def flush(self):
        self.INITIAL_STDOUT.flush()
        self.LOGFILE.flush()
        pass
    
    def Get_Rid_Of_Log(self):
        if self.DELETE_FILE == 'Yes':
            if os.path.exists(self.FILE_PATH):
                try:
                    self.LOGFILE.close() if self.LOGFILE is not None else ''
                    os.remove(self.FILE_PATH)
                    self.LOG_EXISTS = 'No'
                    print('\n' + '/'*60 + '\n')
                    print(f'{self.FILE_PATH} has been deleted.')
                except:
                    print(f'Could not delete {self.FILE_PATH}.')
                    print('\n' + '/'*60 + '\n')
        else:
            self.LOGFILE.close() if self.LOGFILE is not None else ''
            print('\n' + '/'*60 + '\n')
            print(f'File {self.FILE_PATH} will not be deleted as per argument passed. In order to delete it after script completion, please use delete_file = \'Yes\'')
            print('\n' + '/'*60 + '\n')
            print('Log can be used for further manipulation.')
    
    def Get_Rid_Of_Existing_Log(self):
        if os.path.exists(self.FILE_PATH):
                try:
                    os.remove(self.FILE_PATH)
                    self.LOG_EXISTS = 'No'
                    print('\n' + '/'*60 + '\n')
                    print(f'{self.FILE_PATH} existed before being created and will be deleted now.')
                except:
                    print('\n' + '/'*60 + '\n')
                    print(f'Existing {self.FILE_PATH} Could not be deleted.')
        else:
            pass
    
    def Temp_Std_IO(self):
        sys.stdout.flush()
        sys.stdout = self.INITIAL_STDOUT
    
    def Revert_File_IO(self):
        sys.stdout.flush()
        sys.stdout = self.NEW_STDOUT
        
    def Exit_Logger(self):
        sys.stdout = self.INITIAL_STDOUT  
        self.Get_Rid_Of_Log()
        print('\n' + '/'*60 + '\n')
        print('Reverting to old Standard Output')
        print('\n' + '/'*60 + '\n')
        print('I/O has been reverted to Standard Python I/O.')
        print('\n' + '/'*60 + '\n')
