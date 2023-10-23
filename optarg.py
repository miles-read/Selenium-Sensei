import random, subprocess, socket, os, time

## dependancy 
class arguments():
    
    def port_used(port): 
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            return s.connect_ex(('localhost', port)) == 0
    
    def current_session(self,location=None): 
        if self.browser == "chrome":    
            if not location:
                location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
            else:
                assert not os.path.exists(location), "chrome.exe not found"
                
            port = random.randint(30000,65500)
            while arguments.port_used(int(port)) == True:
                port = str(random.randint(30000,65500))
            self.options.add_experimental_option("debuggerAddress", f"localhost:{port}")
            subprocess.Popen(rf'"C:\Program Files\Google\Chrome\Application\chrome.exe" -remote-debugging-port={port} -user-data-dir=C:\Users\readm\Desktop',shell=True)
            time.sleep(1.5)
        else:
            print("Experimental feature: current_session only supported on Chrome")
