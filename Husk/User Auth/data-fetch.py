import sys, getpass, pwd, spwd

checkuser = getpass.getuser()
username = sys.argv
user_info = pwd.getpwnam(checkuser)

print(('Username:'), user_info.pw_name)
print (('Password:'), user_info.pw_passwd)
print (('Comment :'), user_info.pw_gecos)
print (('UID/GID :'), user_info.pw_uid, '/', user_info.pw_gid)
print (('Home    :'), user_info.pw_dir)
print (('Shell   :'), user_info.pw_shell)
print("The user currently logged in is: " + checkuser)

i = spwd.getspnam(checkuser)

###FIGURE OUT HOW TO GET PERMISSION TO ACCESS SHADOW FILE###
###ONCE WE HAVE ACCESS TO SHADOW FILE WE CAN THEN MAKE FEATURE###
###ADD FEATURE TO CONFIRM USER PASSWORD BEFORE APP INSTALLATION###
