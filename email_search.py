def choose_input():
  valid = False
  valid_entries = [1,2]
  while valid == False:
    try:
      choice = input('Choose: \n1 to search by subject\n2 to search by email address')
      if int(choice) not in valid_entries:
        print ('pick a value between 1 and 2\n')
      elif int(choice) in valid_entries:
        valid = True
    except Exception as e:
      print('error {}'.format(str(e)))
  return (int(choice))  

def get_info(x):
  if x == 1:
    email =''
    try:
      subject = input('\nplease enter the subject line you want to search\n')
    except Exception as e:
      print('error {}'.format(str(e)))
    return (x,subject,email)
  elif x ==2:
    subject =''
    try:
      email = input('\nplease enter the email_address you want to search\n')
    except Exception as e:
      print('error {}'.format(str(e)))
    return (x,subject,email)

def searchstring(x,subject,email):
  if x ==1:
    try:
      result = '(index=ironport [search index=ironport message_subject="*' + subject + '*" | fields internal_message_id]) OR (index=o365 *' + subject + '*)'
    except Exception as e:
      print('error {}'.format(str(e)))
    return result
  elif x ==2:
    try:
      result = '(index=ironport [search index=ironport recipient="' + email + '" | fields internal_message_id]) OR (index=o365 ' + email + ')'
    except Exception as e:
      print('error {}'.format(str(e)))
    return result

def mainfxn():
  x = choose_input()
  reslist = get_info(x)
  subject=reslist[1]
  email=reslist[2]
  print('\n')
  print(searchstring(x,subject,email))

if __name__ == "__main__":
  mainfxn()