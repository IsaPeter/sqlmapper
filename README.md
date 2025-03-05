# sqlmapper
SQLMap command creation based on Burp Saved Items


**Export Requests to a folder**

```bash
python3 sqlmapper.py --export-requests /tmp/exported.burp --export-out /tmp/kakukk/ 
```

```
┌──(kali㉿kali)-[/tmp]
└─$ ls kakukk       
req1   req11  req13  req15  req17  req19  req20  req22  req24  req26  req28  req3   req31  req33  req35  req37  req39  req40  req42  req5  req7  req9
req10  req12  req14  req16  req18  req2   req21  req23  req25  req27  req29  req30  req32
```

**Generate SQLMap Requests for testing**

```bash
└─$ python3 sqlmapper.py --requests /tmp/kakukk
sqlmap -r /tmp/kakukk/req1 --batch --tamper between --hostname --current-user | tee result_req1.txt
sqlmap -r /tmp/kakukk/req2 --batch --tamper between --hostname --current-user | tee result_req2.txt
sqlmap -r /tmp/kakukk/req3 --batch --tamper between --hostname --current-user | tee result_req3.txt
sqlmap -r /tmp/kakukk/req4 --batch --tamper between --hostname --current-user | tee result_req4.txt
sqlmap -r /tmp/kakukk/req5 --batch --tamper between --hostname --current-user | tee result_req5.txt
sqlmap -r /tmp/kakukk/req6 --batch --tamper between --hostname --current-user | tee result_req6.txt
sqlmap -r /tmp/kakukk/req7 --batch --tamper between --hostname --current-user | tee result_req7.txt
sqlmap -r /tmp/kakukk/req8 --batch --tamper between --hostname --current-user | tee result_req8.txt
sqlmap -r /tmp/kakukk/req9 --batch --tamper between --hostname --current-user | tee result_req9.txt

```
