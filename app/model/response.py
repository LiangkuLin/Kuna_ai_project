class ApiResponse: 
    def __init__(self,message:str,system_message:Exception = None):
       self.json = {"message":message,"system_message":str(system_message)}
            