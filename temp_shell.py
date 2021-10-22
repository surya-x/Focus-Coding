Python 3.9.5 (v3.9.5:0a7dcbdb13, May  3 2021, 13:17:02) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pafy
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pafy/pafy.py", line 48, in <module>
    import youtube_dl
ModuleNotFoundError: No module named 'youtube_dl'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import pafy
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pafy/__init__.py", line 7, in <module>
    from .pafy import new
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pafy/pafy.py", line 51, in <module>
    raise ImportError(
ImportError: pafy: youtube-dl not found; you can use the internal backend by setting the environmental variable PAFY_BACKEND to "internal". It is not enabled by default because it is not as well maintained as the youtube-dl backend.
>>> import pafy
>>> url = "https://www.youtube.com/watch?v=PY8f1Z3nARo"
>>> video = pafy.new(url)
[0;31mERROR:[0m Unable to download API page: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)> (caused by URLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)')))
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 1346, in do_open
    h.request(req.get_method(), req.selector, req.data, headers,
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/http/client.py", line 1253, in request
    self._send_request(method, url, body, headers, encode_chunked)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/http/client.py", line 1299, in _send_request
    self.endheaders(body, encode_chunked=encode_chunked)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/http/client.py", line 1248, in endheaders
    self._send_output(message_body, encode_chunked=encode_chunked)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/http/client.py", line 1008, in _send_output
    self.send(msg)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/http/client.py", line 948, in send
    self.connect()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/http/client.py", line 1422, in connect
    self.sock = self._context.wrap_socket(self.sock,
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/ssl.py", line 500, in wrap_socket
    return self.sslsocket_class._create(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/ssl.py", line 1040, in _create
    self.do_handshake()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/ssl.py", line 1309, in do_handshake
    self._sslobj.do_handshake()
ssl.SSLCertVerificationError: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/youtube_dl/extractor/common.py", line 634, in _request_webpage
    return self._downloader.urlopen(url_or_request)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/youtube_dl/YoutubeDL.py", line 2288, in urlopen
    return self._opener.open(req, timeout=self._socket_timeout)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 517, in open
    response = self._open(req, data)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 534, in _open
    result = self._call_chain(self.handle_open, protocol, protocol +
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 494, in _call_chain
    result = func(*args)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/youtube_dl/utils.py", line 2735, in https_open
    return self.do_open(functools.partial(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/urllib/request.py", line 1349, in do_open
    raise URLError(err)
urllib.error.URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)>

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/youtube_dl/YoutubeDL.py", line 815, in wrapper
    return func(self, *args, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/youtube_dl/YoutubeDL.py", line 836, in __extract_info
    ie_result = ie.extract(url)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/youtube_dl/extractor/common.py", line 534, in extract
    ie_result = self._real_extract(url)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/youtube_dl/extractor/youtube.py", line 1490, in _real_extract
    player_response = self._call_api(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/youtube_dl/extractor/youtube.py", line 290, in _call_api
    return self._download_json(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/youtube_dl/extractor/common.py", line 895, in _download_json
    res = self._download_json_handle(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/youtube_dl/extractor/common.py", line 874, in _download_json_handle
    res = self._download_webpage_handle(
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/youtube_dl/extractor/common.py", line 667, in _download_webpage_handle
    urlh = self._request_webpage(url_or_request, video_id, note, errnote, fatal, data=data, headers=headers, query=query, expected_status=expected_status)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/youtube_dl/extractor/common.py", line 652, in _request_webpage
    raise ExtractorError(errmsg, sys.exc_info()[2], cause=err)
youtube_dl.utils.ExtractorError: Unable to download API page: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)> (caused by URLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)')))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pafy/backend_youtube_dl.py", line 40, in _fetch_basic
    self._ydl_info = ydl.extract_info(self.videoid, download=False)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/youtube_dl/YoutubeDL.py", line 808, in extract_info
    return self.__extract_info(url, ie, download, extra_info, process)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/youtube_dl/YoutubeDL.py", line 824, in wrapper
    self.report_error(compat_str(e), e.format_traceback())
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/youtube_dl/YoutubeDL.py", line 628, in report_error
    self.trouble(error_message, tb)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/youtube_dl/YoutubeDL.py", line 598, in trouble
    raise DownloadError(message, exc_info)
youtube_dl.utils.DownloadError: [0;31mERROR:[0m Unable to download API page: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)> (caused by URLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)')))

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    video = pafy.new(url)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pafy/pafy.py", line 124, in new
    return Pafy(url, basic, gdata, size, callback, ydl_opts=ydl_opts)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pafy/backend_youtube_dl.py", line 31, in __init__
    super(YtdlPafy, self).__init__(*args, **kwargs)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pafy/backend_shared.py", line 97, in __init__
    self._fetch_basic()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/pafy/backend_youtube_dl.py", line 43, in _fetch_basic
    raise IOError(str(e).replace('YouTube said', 'Youtube says'))
OSError: [0;31mERROR:[0m Unable to download API page: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)> (caused by URLError(SSLCertVerificationError(1, '[SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1129)')))
>>> video = pafy.new(url)
>>> video.author
'Joma Tech'
>>> video.category
'Education'
>>> streams = video.streams
>>> for s in streams:
	print(s)

	
normal:mp4@256x144
normal:mp4@426x240
normal:mp4@640x360
normal:mp4@854x480
normal:mp4@1280x720
normal:mp4@1920x1080
>>> audiostreams = video.audiostreams
>>> for a in audiostreams:
	print(a)

	
>>> for a in audiostreams:
	print(a.bitrate, a.extension)

	
>>> audiostreams.length()
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    audiostreams.length()
AttributeError: 'list' object has no attribute 'length'
>>> len(audiostreams)
0
>>> len(streams)
6
>>> video = pafy.new("https://www.youtube.com/watch?v=sca4VG9b0NY")
>>> a_s = video.audiostreams
>>> len(a_s)
4
>>> for a in a_s:
	print(a)

	
audio:webm@52.41k
audio:webm@69.458k
audio:m4a@129.472k
audio:webm@139.741k
>>> bestaudio = video.getbestaudio()
>>> bestaudio
audio:webm@139.741k
>>> type(bestaudio)
<class 'pafy.backend_youtube_dl.YtdlStream'>
>>> bestaudio.url
'https://r8---sn-524pcxgpo-8u1s.googlevideo.com/videoplayback?expire=1634934512&ei=kMpyYfjHBoyJz7sPuqmaqA8&ip=160.238.75.115&id=o-ACwRdbXIzvCSLorbAWcWLn8AdpIfwiknJ_MWZj87mqn6&itag=251&source=youtube&requiressl=yes&mh=RY&mm=31%2C29&mn=sn-524pcxgpo-8u1s%2Csn-cvh7knze&ms=au%2Crdu&mv=m&mvi=8&pl=24&initcwndbps=506250&vprv=1&mime=audio%2Fwebm&ns=4NXFl3OpDJZcdGnkBvz9yRUG&gir=yes&clen=117725199&dur=6739.581&lmt=1622655028911302&mt=1634912243&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=5532434&n=Cb_QeLS7O0TObE8eV17&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAMRg29alzVCeIkjv_pF0WIE3ceBSy4C9fljgq7zwZFSuAiBWCGRZKm03VLreUG9rOME14ZryfDiEePuyOt_c7FMQsA%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJIXI7XEPqlrqxDDBIYhY1KxH_gPlaaYGqOLDgGLbN3qAiEApmA4G_cWpLVWtLElCL6wUROgOKFlXTKiHldbv6V85-k%3D'
>>> import vlc
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    import vlc
ModuleNotFoundError: No module named 'vlc'
>>> import vlc
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    import vlc
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/vlc.py", line 210, in <module>
    dll, plugin_path  = find_lib()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/vlc.py", line 182, in find_lib
    ctypes.CDLL(c)
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/ctypes/__init__.py", line 374, in __init__
    self._handle = _dlopen(self._name, mode)
OSError: dlopen(/Applications/VLC.app/Contents/MacOS/lib/libvlccore.dylib, 0x0006): tried: '/Applications/Python 3.9/IDLE.app/Contents/Frameworks/libvlccore.dylib' (no such file), '/Applications/VLC.app/Contents/MacOS/lib/libvlccore.dylib' (mach-o file, but is an incompatible architecture (have 'arm64', need 'x86_64')), '/usr/lib/libvlccore.dylib' (no such file), '/Applications/Python 3.9/IDLE.app/Contents/Frameworks/libvlccore.9.dylib' (no such file), '/Applications/VLC.app/Contents/MacOS/lib/libvlccore.9.dylib' (mach-o file, but is an incompatible architecture (have 'arm64', need 'x86_64')), '/usr/lib/libvlccore.9.dylib' (no such file)
>>> import urllib
>>> urllib.open("https://r8---sn-524pcxgpo-8u1s.googlevideo.com/videoplayback?expire=1634934512&ei=kMpyYfjHBoyJz7sPuqmaqA8&ip=160.238.75.115&id=o-ACwRdbXIzvCSLorbAWcWLn8AdpIfwiknJ_MWZj87mqn6&itag=251&source=youtube&requiressl=yes&mh=RY&mm=31%2C29&mn=sn-524pcxgpo-8u1s%2Csn-cvh7knze&ms=au%2Crdu&mv=m&mvi=8&pl=24&initcwndbps=506250&vprv=1&mime=audio%2Fwebm&ns=4NXFl3OpDJZcdGnkBvz9yRUG&gir=yes&clen=117725199&dur=6739.581&lmt=1622655028911302&mt=1634912243&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=5532434&n=Cb_QeLS7O0TObE8eV17&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAMRg29alzVCeIkjv_pF0WIE3ceBSy4C9fljgq7zwZFSuAiBWCGRZKm03VLreUG9rOME14ZryfDiEePuyOt_c7FMQsA%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJIXI7XEPqlrqxDDBIYhY1KxH_gPlaaYGqOLDgGLbN3qAiEApmA4G_cWpLVWtLElCL6wUROgOKFlXTKiHldbv6V85-k%3D")
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    urllib.open("https://r8---sn-524pcxgpo-8u1s.googlevideo.com/videoplayback?expire=1634934512&ei=kMpyYfjHBoyJz7sPuqmaqA8&ip=160.238.75.115&id=o-ACwRdbXIzvCSLorbAWcWLn8AdpIfwiknJ_MWZj87mqn6&itag=251&source=youtube&requiressl=yes&mh=RY&mm=31%2C29&mn=sn-524pcxgpo-8u1s%2Csn-cvh7knze&ms=au%2Crdu&mv=m&mvi=8&pl=24&initcwndbps=506250&vprv=1&mime=audio%2Fwebm&ns=4NXFl3OpDJZcdGnkBvz9yRUG&gir=yes&clen=117725199&dur=6739.581&lmt=1622655028911302&mt=1634912243&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=5532434&n=Cb_QeLS7O0TObE8eV17&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAMRg29alzVCeIkjv_pF0WIE3ceBSy4C9fljgq7zwZFSuAiBWCGRZKm03VLreUG9rOME14ZryfDiEePuyOt_c7FMQsA%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJIXI7XEPqlrqxDDBIYhY1KxH_gPlaaYGqOLDgGLbN3qAiEApmA4G_cWpLVWtLElCL6wUROgOKFlXTKiHldbv6V85-k%3D")
AttributeError: module 'urllib' has no attribute 'open'
>>> urllib.urlopen("https://r8---sn-524pcxgpo-8u1s.googlevideo.com/videoplayback?expire=1634934512&ei=kMpyYfjHBoyJz7sPuqmaqA8&ip=160.238.75.115&id=o-ACwRdbXIzvCSLorbAWcWLn8AdpIfwiknJ_MWZj87mqn6&itag=251&source=youtube&requiressl=yes&mh=RY&mm=31%2C29&mn=sn-524pcxgpo-8u1s%2Csn-cvh7knze&ms=au%2Crdu&mv=m&mvi=8&pl=24&initcwndbps=506250&vprv=1&mime=audio%2Fwebm&ns=4NXFl3OpDJZcdGnkBvz9yRUG&gir=yes&clen=117725199&dur=6739.581&lmt=1622655028911302&mt=1634912243&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=5532434&n=Cb_QeLS7O0TObE8eV17&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAMRg29alzVCeIkjv_pF0WIE3ceBSy4C9fljgq7zwZFSuAiBWCGRZKm03VLreUG9rOME14ZryfDiEePuyOt_c7FMQsA%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJIXI7XEPqlrqxDDBIYhY1KxH_gPlaaYGqOLDgGLbN3qAiEApmA4G_cWpLVWtLElCL6wUROgOKFlXTKiHldbv6V85-k%3D")
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    urllib.urlopen("https://r8---sn-524pcxgpo-8u1s.googlevideo.com/videoplayback?expire=1634934512&ei=kMpyYfjHBoyJz7sPuqmaqA8&ip=160.238.75.115&id=o-ACwRdbXIzvCSLorbAWcWLn8AdpIfwiknJ_MWZj87mqn6&itag=251&source=youtube&requiressl=yes&mh=RY&mm=31%2C29&mn=sn-524pcxgpo-8u1s%2Csn-cvh7knze&ms=au%2Crdu&mv=m&mvi=8&pl=24&initcwndbps=506250&vprv=1&mime=audio%2Fwebm&ns=4NXFl3OpDJZcdGnkBvz9yRUG&gir=yes&clen=117725199&dur=6739.581&lmt=1622655028911302&mt=1634912243&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=5532434&n=Cb_QeLS7O0TObE8eV17&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAMRg29alzVCeIkjv_pF0WIE3ceBSy4C9fljgq7zwZFSuAiBWCGRZKm03VLreUG9rOME14ZryfDiEePuyOt_c7FMQsA%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJIXI7XEPqlrqxDDBIYhY1KxH_gPlaaYGqOLDgGLbN3qAiEApmA4G_cWpLVWtLElCL6wUROgOKFlXTKiHldbv6V85-k%3D")
AttributeError: module 'urllib' has no attribute 'urlopen'
>>> import urllib2
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    import urllib2
ModuleNotFoundError: No module named 'urllib2'
>>> import selenium
>>> from selenium import webdriver
>>> driver = webdriver.Chrome()
Traceback (most recent call last):
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/selenium/webdriver/common/service.py", line 74, in start
    self.process = subprocess.Popen(cmd, env=self.env,
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/subprocess.py", line 951, in __init__
    self._execute_child(args, executable, preexec_fn, close_fds,
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/subprocess.py", line 1821, in _execute_child
    raise child_exception_type(errno_num, err_msg, err_filename)
FileNotFoundError: [Errno 2] No such file or directory: 'chromedriver'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    driver = webdriver.Chrome()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/selenium/webdriver/chrome/webdriver.py", line 69, in __init__
    super(WebDriver, self).__init__(DesiredCapabilities.CHROME['browserName'], "goog",
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/selenium/webdriver/chromium/webdriver.py", line 90, in __init__
    self.service.start()
  File "/Library/Frameworks/Python.framework/Versions/3.9/lib/python3.9/site-packages/selenium/webdriver/common/service.py", line 84, in start
    raise WebDriverException(
selenium.common.exceptions.WebDriverException: Message: 'chromedriver' executable needs to be in PATH. Please see https://chromedriver.chromium.org/home

>>> driver = webdriver.Chrome(executable_path=r"/Users/vsuryakumar/CodeBase/chromedriver")

Warning (from warnings module):
  File "<pyshell#39>", line 1
DeprecationWarning: executable_path has been deprecated, please pass in a Service object
>>> driver.get("https://r8---sn-524pcxgpo-8u1s.googlevideo.com/videoplayback?expire=1634934512&ei=kMpyYfjHBoyJz7sPuqmaqA8&ip=160.238.75.115&id=o-ACwRdbXIzvCSLorbAWcWLn8AdpIfwiknJ_MWZj87mqn6&itag=251&source=youtube&requiressl=yes&mh=RY&mm=31%2C29&mn=sn-524pcxgpo-8u1s%2Csn-cvh7knze&ms=au%2Crdu&mv=m&mvi=8&pl=24&initcwndbps=506250&vprv=1&mime=audio%2Fwebm&ns=4NXFl3OpDJZcdGnkBvz9yRUG&gir=yes&clen=117725199&dur=6739.581&lmt=1622655028911302&mt=1634912243&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=5532434&n=Cb_QeLS7O0TObE8eV17&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAMRg29alzVCeIkjv_pF0WIE3ceBSy4C9fljgq7zwZFSuAiBWCGRZKm03VLreUG9rOME14ZryfDiEePuyOt_c7FMQsA%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJIXI7XEPqlrqxDDBIYhY1KxH_gPlaaYGqOLDgGLbN3qAiEApmA4G_cWpLVWtLElCL6wUROgOKFlXTKiHldbv6V85-k%3D")
>>> from selenium.webdriver.chrome.options import Options
>>> chrome_options = Options()
>>> chrome_options.add_argument("--headless")
>>> chrome_options.add_argument("--no-sandbox")
>>> driver = webdriver.Chrome(executable_path=r"/Users/vsuryakumar/CodeBase/chromedriver", options=chrome_options)
>>> driver.get("https://r8---sn-524pcxgpo-8u1s.googlevideo.com/videoplayback?expire=1634934512&ei=kMpyYfjHBoyJz7sPuqmaqA8&ip=160.238.75.115&id=o-ACwRdbXIzvCSLorbAWcWLn8AdpIfwiknJ_MWZj87mqn6&itag=251&source=youtube&requiressl=yes&mh=RY&mm=31%2C29&mn=sn-524pcxgpo-8u1s%2Csn-cvh7knze&ms=au%2Crdu&mv=m&mvi=8&pl=24&initcwndbps=506250&vprv=1&mime=audio%2Fwebm&ns=4NXFl3OpDJZcdGnkBvz9yRUG&gir=yes&clen=117725199&dur=6739.581&lmt=1622655028911302&mt=1634912243&fvip=1&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=5532434&n=Cb_QeLS7O0TObE8eV17&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAMRg29alzVCeIkjv_pF0WIE3ceBSy4C9fljgq7zwZFSuAiBWCGRZKm03VLreUG9rOME14ZryfDiEePuyOt_c7FMQsA%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRgIhAJIXI7XEPqlrqxDDBIYhY1KxH_gPlaaYGqOLDgGLbN3qAiEApmA4G_cWpLVWtLElCL6wUROgOKFlXTKiHldbv6V85-k%3D")
>>> 