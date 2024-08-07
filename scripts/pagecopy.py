from pywebcopy import save_webpage

url = 'http://test.com'
download_folder = './download/'    

kwargs = {'bypass_robots': True, 'project_name': 'test'}

save_webpage(url, download_folder, **kwargs)