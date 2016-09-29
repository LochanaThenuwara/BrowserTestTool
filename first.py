import webbrowser

webbrowser.register('firefox', None, webbrowser.BackgroundBrowser("C:/Program Files (x86)/Mozilla Firefox/firefox.exe"))
webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"))
webbrowser.register('ie', None, webbrowser.BackgroundBrowser("C:/Program Files (x86)/Internet Explorer/iexplore.exe"))

webbrowser.get('chrome').open('frontend.html')
webbrowser.get('firefox').open('frontend.html')
webbrowser.get('ie').open('frontend.html')
        
