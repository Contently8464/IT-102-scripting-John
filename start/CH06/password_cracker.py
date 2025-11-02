

#BY John Gurney
from passlib.hash import sha512_crypt

SHADOW_FILE = r'/home/vividly9612/Documents/SchoolG7/IT 102/IT-102-scripting-John/start/CH06/shadow2.txt'
PASSWORD_FILE = r'/home/vividly9612/Documents/SchoolG7/IT 102/IT-102-scripting-John/start/CH06/wordlist.txt'
def guess_password(ShadowFile, PasswordFile):
   successful_attempts = []
   try:
      with open(SHADOW_FILE, 'r', encoding='utf-8') as sf, open(PASSWORD_FILE, 'r', encoding='utf-8') as pf:
         shadows = sf.readlines()
         passwords = [pw.strip() for pw in pf.readlines()]
         
         for shadow in shadows:
            parts = shadow.split(":")
            if len(parts) < 2 or '!' in parts [1] or '*' in parts [1]:
               continue
            username, hash_password = parts[0], parts[1].strip()
            
            for password in passwords:
               try:
                  if sha512_crypt.verify(password, hash_password):
                     successful_attempts.append((username, password))
                     print(f'[+] Cracked {username}: {password}')
                     break
               except ValueError:
                  continue
   except FileNotFoundError as e:
      print(f"Error: {e}")
      return

   if successful_attempts:
      print("\n=======CRACKED PASSWORD =====")
      for username, password in successful_attempts:
         print(f'User: {username}, Password: {password}')
   else:
      print("/nNo passwords were found or cracked")

guess_password(SHADOW_FILE, PASSWORD_FILE)