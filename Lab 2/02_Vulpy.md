# Results to VULPY

***Test results:***
```ruby
Issue: [B113:request_without_timeout]
Requests call without timeout
Severity: Medium   Confidence: Low
CWE: CWE-400 (https://cwe.mitre.org/data/definitions/400.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b113_request_without_timeout.html
Location: ./bad/api_list.py:10:8
9
10        r = requests.get('http://127.0.1.1:5000/api/post/{}'.format(username))
11        if r.status_code != 200:
```

***Test results:***
```ruby
Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
Severity: Medium   Confidence: Medium 
CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b108_hardcoded_tmp_directory.html
Location: ./bad/api_post.py:6:20
5
6       api_key_file = Path('/tmp/supersecret.txt')
7
```

***Test results:*** 
```ruby
Issue: [B113:request_without_timeout] Requests call without timeout 
Severity: Medium   Confidence: Low 
CWE: CWE-400 (https://cwe.mitre.org/data/definitions/400.html) 
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b113_request_without_timeout.html 
Location: ./bad/api_post.py:16:12 
15 
16      r = requests.post('http://127.0.1.1:5000/api/key', json={'username':username, '	password':password}) 
17
```

***Test results:***
```ruby
Issue: [B113:request_without_timeout] Requests call without timeout
Severity: Medium   Confidence: Low
CWE: CWE-400 (https://cwe.mitre.org/data/definitions/400.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b113_request_without_timeout.html
Location: ./bad/api_post.py:30:8
29        api_key = api_key_file.open().read()
30        r = requests.post('http://127.0.1.1:5000/api/post', json={'text':message}, headers={'X APIKEY': api_key})
31        print(r.text)
```

***Test results:***
```ruby
Issue: [B404:blacklist] Consider possible security implications associated with the subprocess module.
Severity: Low   Confidence: High
CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/blacklists/blacklist_imports.html#b404-import-subprocess
Location: ./bad/brute.py:3:0
2
3       import subprocess
4       import sys
```

***Test results:***
```ruby
Issue: [B603:subprocess_without_shell_equals_true] subprocess call - check for execution of untrusted input.
Severity: Low   Confidence: High
CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b603_subprocess_without_shell_equals_true.html
Location: ./bad/brute.py:21:13
20        for password in passwords:
21        result = subprocess.run([program, username, password], stdout=subprocess.DEVNULL)
22        if result.returncode == 0:
```

***Test results:***
```ruby
Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
Severity: Medium   Confidence: Medium
CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b608_hardcoded_sql_expressions.html
Location: ./bad/db.py:19:18
18       for u,p in users:
19       c.execute("INSERT INTO users (user, password, failures) VALUES ('%s', '%s', '%d')" %(u, p, 0))
20
```

***Test results:***
```ruby
Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
Severity: Medium   Confidence: Medium
CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b608_hardcoded_sql_expressions.html
Location: ./bad/db_init.py:20:18
19        for u,p in users:
20        c.execute("INSERT INTO users (username, password, failures, mfa_enabled, mfa_secret) VALUES ('%s', '%s', '%d', '%d', '%s')" %(u, p, 0, 0, ''))
21
```

***Test results:***
```ruby
Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
Severity: Medium   Confidence: Medium
CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b108_hardcoded_tmp_directory.html
Location: ./bad/libapi.py:16:18
15
16        for f in Path('/tmp/').glob('vulpy.apikey.' + username + '.*'):
17        print('removing', f)
```

***Test results:***
```ruby
Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
Severity: Medium   Confidence: Medium
CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b108_hardcoded_tmp_directory.html
Location: ./bad/libapi.py:20:14
19
20        keyfile = '/tmp/vulpy.apikey.{}.{}'.format(username, key)
21
```

***Test results:***
```ruby
Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
Severity: Medium   Confidence: Medium
CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b108_hardcoded_tmp_directory.html
Location: ./bad/libapi.py:33:18
32
33        for f in Path('/tmp/').glob('vulpy.apikey.*.' + key):
34        return f.name.split('.')[2]
```

***Test results:***
```ruby
Issue: [B110:try_except_pass] Try, Except, Pass detected.
Severity: Low   Confidence: High
CWE: CWE-703 (https://cwe.mitre.org/data/definitions/703.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b110_try_except_pass.html
Location: ./bad/libsession.py:21:4
20        session = json.loads(base64.b64decode(cookie))
21        except Exception:
22        pass
23
```

***Test results:***
```ruby
Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
Severity: Medium   Confidence: Medium
CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b608_hardcoded_sql_expressions.html
Location: ./bad/libuser.py:12:21
11
12        user = c.execute("SELECT * FROM users WHERE username = '{}' and password = '{}'".format(username, password)).fetchone()
13
```

***Test results:***
```ruby
Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
Severity: Medium   Confidence: Medium
CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b608_hardcoded_sql_expressions.html
Location: ./bad/libuser.py:25:14
24
25        c.execute("INSERT INTO users (username, password, failures, mfa_enabled, mfa_secret) VALUES ('%s', '%s', '%d', '%d', '%s')" %(username, password, 0, 0,''))
26
```

***Test results:***
```ruby
Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
Severity: Medium   Confidence: Medium
CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b608_hardcoded_sql_expressions.html
Location: ./bad/libuser.py:53:14
52
53        c.execute("UPDATE users SET password = '{}' WHERE username = '{}'".format(password, username))
54       conn.commit()
```

***Test results:***
```ruby
Issue: [B105:hardcoded_password_string] Possible hardcoded password: 'aaaaaaa'
Severity: Low   Confidence: Medium
CWE: CWE-259 (https://cwe.mitre.org/data/definitions/259.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b105_hardcoded_password_string.html
Location: ./bad/vulpy-ssl.py:13:11
12        app = Flask('vulpy')
13        app.config['SECRET_KEY'] = 'aaaaaaa'
14
```

***Test results:***
```ruby
Issue: [B201:flask_debug_true] A Flask app appears to be run with debug=True, which exposes the Werkzeug debugger and allows the execution of arbitrary code.
Severity: High   Confidence: Medium
CWE: CWE-94 (https://cwe.mitre.org/data/definitions/94.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b201_flask_debug_true.html
Location: ./bad/vulpy-ssl.py:29:0
28
29      app.run(debug=True, host='127.0.1.1', ssl_context=('/tmp/acme.cert', '/tmp/acme.key'))
```

***Test results:***
```ruby
Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
Severity: Medium   Confidence: Medium
CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b108_hardcoded_tmp_directory.html
Location: ./bad/vulpy-ssl.py:29:51
28
29        app.run(debug=True, host='127.0.1.1', ssl_context=('/tmp/acme.cert', '/tmp/acme.key'))
```

***Test results:***
```ruby
Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
Severity: Medium   Confidence: Medium
CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b108_hardcoded_tmp_directory.html
Location: ./bad/vulpy-ssl.py:29:69
28
29        app.run(debug=True, host='127.0.1.1', ssl_context=('/tmp/acme.cert', '/tmp/acme.key'))
```

***Test results:***
```ruby
Issue: [B105:hardcoded_password_string] Possible hardcoded password: 'aaaaaaa'
Severity: Low   Confidence: Medium
CWE: CWE-259 (https://cwe.mitre.org/data/definitions/259.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b105_hardcoded_password_string.html
Location: ./bad/vulpy.py:16:11
15        app = Flask('vulpy')
16        app.config['SECRET_KEY'] = 'aaaaaaa'
17
```

***Test results:***
```ruby
Issue: [B201:flask_debug_true] A Flask app appears to be run with debug=True, which exposes the Werkzeug debugger and allows the execution of arbitrary code.
Severity: High   Confidence: Medium
CWE: CWE-94 (https://cwe.mitre.org/data/definitions/94.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b201_flask_debug_true.html
Location: ./bad/vulpy.py:55:0
54
55        app.run(debug=True, host='127.0.1.1', port=5000, extra_files='csp.txt')
```

***Test results:***
```ruby
Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
Severity: Medium   Confidence: Medium
CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b108_hardcoded_tmp_directory.html
Location: ./good/cutpasswd.py:3:10
2
3       with open('/tmp/darkweb2017-top10000.txt') as f:
4       for password in f.readlines():
```

***Test results:***
```ruby
Issue: [B113:request_without_timeout] Requests call without timeout
Severity: Medium   Confidence: Low
CWE: CWE-400 (https://cwe.mitre.org/data/definitions/400.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b113_request_without_timeout.html
Location: ./good/httpbrute.py:22:15
21        for password in passwords:
22        response = requests.post(URL, data = {'username': username, 'password': password})
23        if 'HOME' in response.text:
```

***Test results:***
```ruby
Issue: [B105:hardcoded_password_string] Possible hardcoded password: 'MYSUPERSECRETKEY'
Severity: Low   Confidence: Medium
CWE: CWE-259 (https://cwe.mitre.org/data/definitions/259.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b105_hardcoded_password_string.html
Location: ./good/libapi.py:10:9
9
10        secret = 'MYSUPERSECRETKEY'
11        not_after = 60 # 1 minute
```

***Test results:***
```ruby
Issue: [B110:try_except_pass] Try, Except, Pass detected.
Severity: Low   Confidence: High
CWE: CWE-703 (https://cwe.mitre.org/data/definitions/703.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b110_try_except_pass.html
Location: ./good/libsession.py:22:4
21        country = geo.country.iso_code
22        except Exception:
23        pass
24
```

***Test results:***
```ruby
Issue: [B608:hardcoded_sql_expressions] Possible SQL injection vector through string-based query construction.
Severity: Medium   Confidence: Medium
CWE: CWE-89 (https://cwe.mitre.org/data/definitions/89.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b608_hardcoded_sql_expressions.html
Location: ./good/libuser.py:61:14
60        c = conn.cursor()
61        c.execute("INSERT INTO users (username, password, salt, failures, mfa_enabled, mfa_secret) VALUES ('%s', '%s', '%s', '%d', '%d', '%s')" %(username, '', '', 0, 0, ''))
62        conn.commit()
```

***Test results:***
```ruby
Issue: [B105:hardcoded_password_string] Possible hardcoded password: 'aaaaaaa'
Severity: Low   Confidence: Medium
CWE: CWE-259 (https://cwe.mitre.org/data/definitions/259.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b105_hardcoded_password_string.html
Location: ./good/vulpy-ssl.py:13:11
12        app = Flask('vulpy')
13        app.config['SECRET_KEY'] = 'aaaaaaa'
14
```

***Test results:***
```ruby
Issue: [B201:flask_debug_true] A Flask app appears to be run with debug=True, which exposes the Werkzeug debugger and allows the execution of arbitrary code.
Severity: High   Confidence: Medium
CWE: CWE-94 (https://cwe.mitre.org/data/definitions/94.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b201_flask_debug_true.html
Location: ./good/vulpy-ssl.py:29:0
28
29        app.run(debug=True, host='127.0.1.1', ssl_context=('/tmp/acme.cert', '/tmp/acme.key'))
```

***Test results:***
```ruby
Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
Severity: Medium   Confidence: Medium
CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b108_hardcoded_tmp_directory.html
Location: ./good/vulpy-ssl.py:29:51
28
29        app.run(debug=True, host='127.0.1.1', ssl_context=('/tmp/acme.cert', '/tmp/acme.key'))
```

***Test results:***
```ruby
Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
Severity: Medium   Confidence: Medium
CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b108_hardcoded_tmp_directory.html
Location: ./good/vulpy-ssl.py:29:69
28
29        app.run(debug=True, host='127.0.1.1', ssl_context=('/tmp/acme.cert', '/tmp/acme.key'))
```

***Test results:***
```ruby
Issue: [B105:hardcoded_password_string] Possible hardcoded password: '123aa8a93bdde342c871564a62282af857bda14b3359fde95d0c5e4b321610c1'
Severity: Low   Confidence: Medium
CWE: CWE-259 (https://cwe.mitre.org/data/definitions/259.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b105_hardcoded_password_string.html
Location: ./good/vulpy.py:17:11
16	app = Flask('vulpy')
17	app.config['SECRET_KEY'] = '123aa8a93bdde342c871564a62282af857bda14b3359fde95d0c5e4b321610c1'
18
```

***Test results:***
```ruby
Issue: [B201:flask_debug_true] A Flask app appears to be run with debug=True, which exposes the Werkzeug debugger and allows the execution of arbitrary code.
Severity: High   Confidence: Medium
CWE: CWE-94 (https://cwe.mitre.org/data/definitions/94.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b201_flask_debug_true.html
Location: ./good/vulpy.py:53:0
52
53	app.run(debug=True, host='127.0.1.1', port=5001, extra_files='csp.txt')
54
```

***Test results:***
```ruby
Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
Severity: Medium   Confidence: Medium
CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b108_hardcoded_tmp_directory.html
Location: ./utils/ca-create.py:31:10
30
31	with open('/tmp/ca.key', 'wb') as out:
32	out.write(pem_private)
```

***Test results:***
```ruby
Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
Severity: Medium   Confidence: Medium
CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b108_hardcoded_tmp_directory.html
Location: ./utils/ca-create.py:34:10
33
34	with open('/tmp/ca.pub', 'wb') as out:
35	out.write(pem_public)
```

***Test results:***
```ruby
Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
Severity: Medium   Confidence: Medium
CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b108_hardcoded_tmp_directory.html
Location: ./utils/ca-create.py:58:10
57        # Write our certificate out to disk.
58        with open('/tmp/ca.cert', 'wb') as out:
59        out.write(cert.public_bytes(serialization.Encoding.PEM))
```

***Test results:***
```ruby
Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
Severity: Medium   Confidence: Medium
CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b108_hardcoded_tmp_directory.html
Location: ./utils/ca-csr-create.py:12:10
11
12        with open("/tmp/acme.key", "rb") as key_file:
13        private_key = serialization.load_pem_private_key(
```

***Test results:***
```ruby
Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
Severity: Medium   Confidence: Medium
CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b108_hardcoded_tmp_directory.html
Location: ./utils/ca-csr-create.py:35:10
34        # Write our CSR out to disk.
35        with open("/tmp/acme.csr", "wb") as out:
36        out.write(csr.public_bytes(serialization.Encoding.PEM))
```

***Test results:***
```ruby
Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
Severity: Medium   Confidence: Medium
CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b108_hardcoded_tmp_directory.html
Location: ./utils/ca-csr-load.py:13:10
12
13          with open("/tmp/ca.cert", "rb") as ca_cert_file:
14	        ca_cert = x509.load_pem_x509_certificate(ca_cert_file.read(), default_backend())
```

***Test results:***
```ruby
Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
Severity: Medium   Confidence: Medium
CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b108_hardcoded_tmp_directory.html
Location: ./utils/ca-csr-load.py:16:10
15
16        with open("/tmp/acme.csr", "rb") as csr_file:
17        csr = x509.load_pem_x509_csr(csr_file.read(), default_backend())
```

***Test results:***
```ruby
Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
Severity: Medium   Confidence: Medium
CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b108_hardcoded_tmp_directory.html
Location: ./utils/ca-csr-load.py:19:10
18
19        with open("/tmp/ca.key", "rb") as key_file:
20        private_key = serialization.load_pem_private_key(
```

***Test results:***
```ruby
Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
Severity: Medium   Confidence: Medium
CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b108_hardcoded_tmp_directory.html
Location: ./utils/ca-csr-load.py:35:10
34        # Write our certificate out to disk.
35        with open('/tmp/acme.cert', 'wb') as out:
36        out.write(cert.public_bytes(serialization.Encoding.PEM))
```

***Test results:***
```ruby
Issue: [B113:request_without_timeout] Requests call without timeout
Severity: Medium   Confidence: Low
CWE: CWE-400 (https://cwe.mitre.org/data/definitions/400.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b113_request_without_timeout.html
Location: ./utils/generate_bad_passwords.py:21:9
20        click.echo('Downloading password file...', nl=False, err=True)
21        with requests.get(url, stream=True) as r:
22        r.raise_for_status()
```

***Test results:***
```ruby
Issue: [B113:request_without_timeout] Requests call without timeout
Severity: Medium   Confidence: Low
CWE: CWE-400 (https://cwe.mitre.org/data/definitions/400.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b113_request_without_timeout.html
Location: ./utils/httpbrute.py:25:19
24        for password in passwords:
25        response = requests.post(url, data = {'username': username, 'password': password})
26        logging.info('{} {} {}'.format(username, password, response.status_code))
```

***Test results:***
```ruby
Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
Severity: Medium   Confidence: Medium
CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b108_hardcoded_tmp_directory.html
Location: ./utils/rsa-decrypt.py:14:10
13
14        with open("/tmp/acme.key", "rb") as key_file:
15        private_key = serialization.load_pem_private_key(
```

***Test results:***
```ruby
Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
Severity: Medium   Confidence: Medium
CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b108_hardcoded_tmp_directory.html
Location: ./utils/rsa-encrypt.py:14:10
13
14        with open("/tmp/acme.pub", "rb") as key_file:
15        public_key = serialization.load_pem_public_key(
```

***Test results:***
```ruby
Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
Severity: Medium   Confidence: Medium
CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b108_hardcoded_tmp_directory.html
Location: ./utils/rsa-keygen.py:26:10
25
26        with open('/tmp/acme.key', 'wb') as out:
27        out.write(pem_private)
```

***Test results:***
```ruby
Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
Severity: Medium   Confidence: Medium
CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b108_hardcoded_tmp_directory.html
Location: ./utils/rsa-keygen.py:29:10
28
29        with open('/tmp/acme.pub', 'wb') as out:
30        out.write(pem_public)
```

***Test results:***
```ruby
Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
Severity: Medium   Confidence: Medium
CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b108_hardcoded_tmp_directory.html
Location: ./utils/rsa-sign.py:15:10
14
15        with open("/tmp/acme.key", "rb") as key_file:
16        private_key = serialization.load_pem_private_key(
```

***Test results:***
```ruby
Issue: [B108:hardcoded_tmp_directory] Probable insecure usage of temp file/directory.
Severity: Medium   Confidence: Medium
CWE: CWE-377 (https://cwe.mitre.org/data/definitions/377.html)
More Info: https://bandit.readthedocs.io/en/1.7.5/plugins/b108_hardcoded_tmp_directory.html
Location: ./utils/rsa-verify.py:16:10
15
16        with open("/tmp/acme.pub", "rb") as key_file:
17        public_key = serialization.load_pem_public_key(
```
