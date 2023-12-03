def encode(self, conn):
        # Reply as HTTP/1.1 server, saying "HTTP OK" (code 200).
        # sending all this stuff
        conn.send(b"HTTP/1.1 200 OK\n")
        conn.send(b"Access-Control-Allow-Origin: http://localhost:3000\n")
        conn.send(b"Access-Control-Allow-Credentials: true\n")
        conn.send(b"message")
        
        response_headers = {
            'Content-Type': 'text/html; encoding=utf8',
            'Content-Length': 5,
            'Connection': 'close',
        }
    
        response_headers_raw = ''.join('%s: %s\n' % (k, v) for k, v in \
                                                response_headers.items())
        
        
        response_body = [
            '<html><body><h1>Hello, world!</h1>',
            '<p>This page is in location , was requested ' % locals(),
            'using , and with .</p>' % locals(),
            '<p>Request body isr</p>' % locals(),
            '<p>Actual set of headers received:</p>',
            '<ul>',
        ]
        
        response_body.append('</ul></body></html>')
    
        response_body_raw = ''.join(response_body)
        
        conn.send(memoryview(response_headers_raw.encode('utf-8')).tobytes())
        conn.send(b'\n') # to separate headers from body
        conn.send(memoryview(response_body_raw.encode('utf-8')).tobytes())
        