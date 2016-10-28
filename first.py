import webbrowser

f = open('features.txt', 'r')
features = [line.rstrip('\n') for line in f]
print features;

  
webbrowser.register('firefox', None, webbrowser.BackgroundBrowser("C:/Program Files (x86)/Mozilla Firefox/firefox.exe"))
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"))
webbrowser.register('ie', None, webbrowser.BackgroundBrowser("C:/Program Files (x86)/Internet Explorer/iexplore.exe"))

for feature in features:
    fileName=feature+".html"
    
    webbrowser.get('chrome').open(fileName)
    webbrowser.get('firefox').open(fileName)

#webbrowser.get('ie').open('frontend.html')
        
