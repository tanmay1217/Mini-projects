import webbrowser
url=input('enter the youtube video link:\t')
download=url[:12] + 'ss' +url[12:]
webbrowser.open(download)
