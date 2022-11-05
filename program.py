Last login: Fri Nov  4 20:28:50 on ttys000
arkan@MacBook-Pro-ArKan ~ % ssh-keygen
Generating public/private rsa key pair.
Enter file in which to save the key (/Users/arkan/.ssh/id_rsa): 
Created directory '/Users/arkan/.ssh'.
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /Users/arkan/.ssh/id_rsa
Your public key has been saved in /Users/arkan/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:WJerXGqmsfoHi79PA4SkqwcB7jktkSxvID0HWIoQTro arkan@MacBook-Pro-ArKan.local
The key's randomart image is:
+---[RSA 3072]----+
|+=o .            |
|@o.+ .     .     |
|O*+ o . . o      |
|+=++ . o . .     |
|E=+.  o S o      |
| +o   .o +       |
|. .  ..oO        |
| .  . .B..       |
|    .+*+.        |
+----[SHA256]-----+
arkan@MacBook-Pro-ArKan ~ % cat .ssh/id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC/YJr96X6fucNgWmfYLVoT4Qh45ryGy8qx1p0CqXaV8WPjUtfcziyOjs8xzwpOyUjABvazCz45+rKdj3hkTcFODqxXHrxg43qkZOuN9yL0Cuvi7b/hrhW5B55jE/k1gESIfX84XmwXLTMWjafmmTAIZoYTTYnxN+wHhutzgW4ZKybFa+o7QtbNqcbh7H73YWmJI7kWFQSHoJYHFjW3mkP639nDLBuCELdd8tLAklQyLBZEqRKLExTeK5DbhbyzhvXsdF20ac8qoAdMnRDUi5CDZ6YgSAzQC5V2HMwiGAWu0b7P4oEZfDOIhHnaB3HsCCJ/8E1uWkW30p6/WJuFQJ4DAOvSvGESj73vRzLIGnGqi6/BOqNZwQG4Fnh5n9WQtOzvUTKps+8b3ZTjWplT57BXgB1WGBg3frMSlVC1DCJUC2e221f+df2/JXsngHWhVAURYsS41gZagwlokweMbo52lkbakCGb99rNDQicyEgsJmw13ZOHHDT1itqMSZlbto8= arkan@MacBook-Pro-ArKan.local
arkan@MacBook-Pro-ArKan ~ % .ssh/id_rsa.pub
zsh: permission denied: .ssh/id_rsa.pub
arkan@MacBook-Pro-ArKan ~ % cat .ssh/id_rsa.pub
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQC/YJr96X6fucNgWmfYLVoT4Qh45ryGy8qx1p0CqXaV8WPjUtfcziyOjs8xzwpOyUjABvazCz45+rKdj3hkTcFODqxXHrxg43qkZOuN9yL0Cuvi7b/hrhW5B55jE/k1gESIfX84XmwXLTMWjafmmTAIZoYTTYnxN+wHhutzgW4ZKybFa+o7QtbNqcbh7H73YWmJI7kWFQSHoJYHFjW3mkP639nDLBuCELdd8tLAklQyLBZEqRKLExTeK5DbhbyzhvXsdF20ac8qoAdMnRDUi5CDZ6YgSAzQC5V2HMwiGAWu0b7P4oEZfDOIhHnaB3HsCCJ/8E1uWkW30p6/WJuFQJ4DAOvSvGESj73vRzLIGnGqi6/BOqNZwQG4Fnh5n9WQtOzvUTKps+8b3ZTjWplT57BXgB1WGBg3frMSlVC1DCJUC2e221f+df2/JXsngHWhVAURYsS41gZagwlokweMbo52lkbakCGb99rNDQicyEgsJmw13ZOHHDT1itqMSZlbto8= arkan@MacBook-Pro-ArKan.local
arkan@MacBook-Pro-ArKan ~ % git config --global user.name "Аркадий Канбер"
arkan@MacBook-Pro-ArKan ~ % arkan@MacBook-Pro-ArKan ~ % git config --global user.email "kanber.arkadi@mail.ru"  
zsh: command not found: arkan@MacBook-Pro-ArKan
arkan@MacBook-Pro-ArKan ~ % git config --global user.name "Аркадий Канбер"
arkan@MacBook-Pro-ArKan ~ % git config --global user.email "kanber.arkadi@mail.ru" 
arkan@MacBook-Pro-ArKan ~ % cd Dev
arkan@MacBook-Pro-ArKan Dev % git clone git@github.com:yandex-praktikum/backend_test_homework.git
Cloning into 'backend_test_homework'...
The authenticity of host 'github.com (140.82.121.4)' can't be established.
ED25519 key fingerprint is SHA256:+DiY3wvvV6TuJJhbpZisF/zLDA0zPMSvHdkr4UvCOqU.
This key is not known by any other names
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes  
Warning: Permanently added 'github.com' (ED25519) to the list of known hosts.
Enter passphrase for key '/Users/arkan/.ssh/id_rsa': 
remote: Enumerating objects: 17, done.
remote: Total 17 (delta 0), reused 0 (delta 0), pack-reused 17
Receiving objects: 100% (17/17), 5.41 KiB | 5.41 MiB/s, done.
Resolving deltas: 100% (1/1), done.
arkan@MacBook-Pro-ArKan Dev % cd backend_test_homework/
arkan@MacBook-Pro-ArKan backend_test_homework % ls -a
.		.git		program.py	test_program.py
..		README.md	pytest.ini
arkan@MacBook-Pro-ArKan backend_test_homework % git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
arkan@MacBook-Pro-ArKan backend_test_homework % cd program.py
cd: not a directory: program.py
arkan@MacBook-Pro-ArKan backend_test_homework % cd ~
arkan@MacBook-Pro-ArKan ~ % cd program.py
cd: no such file or directory: program.py
arkan@MacBook-Pro-ArKan ~ % cd Dev
arkan@MacBook-Pro-ArKan Dev % cd program.py
cd: no such file or directory: program.py
arkan@MacBook-Pro-ArKan Dev % cd backend_test_homework/ 
arkan@MacBook-Pro-ArKan backend_test_homework % cd program.py
cd: not a directory: program.py
arkan@MacBook-Pro-ArKan backend_test_homework % program.py
zsh: command not found: program.py
arkan@MacBook-Pro-ArKan backend_test_homework % open program.py
arkan@MacBook-Pro-ArKan backend_test_homework % cd ~
arkan@MacBook-Pro-ArKan ~ % cd Dev
arkan@MacBook-Pro-ArKan Dev % sude chmod + program.py
zsh: command not found: sude
arkan@MacBook-Pro-ArKan Dev % cat program.py
cat: program.py: No such file or directory
arkan@MacBook-Pro-ArKan Dev % cd ~
arkan@MacBook-Pro-ArKan ~ % cat program.py
cat: program.py: No such file or directory
arkan@MacBook-Pro-ArKan ~ % cd Dev
arkan@MacBook-Pro-ArKan Dev % cd backend_test_homework/
arkan@MacBook-Pro-ArKan backend_test_homework % cd ..
arkan@MacBook-Pro-ArKan Dev % cd backend_test_homework/
arkan@MacBook-Pro-ArKan backend_test_homework % ls
README.md	program.py	pytest.ini	test_program.py
arkan@MacBook-Pro-ArKan backend_test_homework % ls -a
.		.git		program.py	test_program.py
..		README.md	pytest.ini
arkan@MacBook-Pro-ArKan backend_test_homework % pwd
/Users/arkan/Dev/backend_test_homework
arkan@MacBook-Pro-ArKan backend_test_homework % nano program.py

  UW PICO 5.09                             File: program.py                              Modified  

print('Я домашка')





















































^G Get Help     ^O WriteOut     ^R Read File    ^Y Prev Pg      ^K Cut Text     ^C Cur Pos      
^X Exit         ^J Justify      ^W Where is     ^V Next Pg      ^U UnCut Text   ^T To Spell     
