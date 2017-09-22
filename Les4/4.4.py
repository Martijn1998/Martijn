oldpassword = input ('old password:')
newpassword = input ('new password')
if len(newpassword) >= 6 and oldpassword != newpassword:
    print('true')
else: print('false')