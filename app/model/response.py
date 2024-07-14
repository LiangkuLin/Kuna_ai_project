class ApiResponse: 
    def __init__(self,message,system_message):
       self.json = {"message":message,"system_message":system_message}
            