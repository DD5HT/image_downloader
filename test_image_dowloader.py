import unittest
import http.server, socketserver
import os.path
import image_dowloader
from threading import Thread

def run_server():
    """A simple webserver running on port 60451 which handles a single request"""
    PORT = 60451

    Handler = http.server.SimpleHTTPRequestHandler

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        httpd.handle_request()

class TestImageDownloader(unittest.TestCase):

    def test_dowload_file(self):
        thread = Thread(target = run_server)
        thread.start()
        data = image_dowloader.download_file("http://127.0.0.1:60451/images/0.jpg")
        expected = b'sample0'
        self.assertEqual(data, expected)

        #Now an invalid URL, we don't have to spin up the server for that.
        data1 = image_dowloader.download_file("www.fail.fail.fail/fail.jpg")
        self.assertEqual(data1, None)
    
    def test_save_file(self):
        data = b'testdata'
        filename = "testfile"
        image_dowloader.save_file(filename, data)
        self.assertTrue(os.path.isfile(filename))
        os.remove(filename) #Cleanup

    def test_get_file_name(self):
        url = "http://example.org/fun.jpg"
        filename = image_dowloader.get_file_name(url)
        self.assertEqual("fun.jpg", filename)

if __name__ == '__main__':
    unittest.main()





