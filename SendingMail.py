"""Script that sends a mail using Gmail
:author: Victor Nieves Sanchez
:version: 1.0"""

import smtplib
import getpass

def sendemail(fromAddr, toAddr, ccAddr,
              subject, msg, username, passw, smtpserver ='smtp.gmail.com:587'):
    """Function that creates the email and sends it.

    :param:fromAddr: from address.
    :param: toAddr: to address.
    :param ccAddr: cc address.
    :param: subject: subject.
    :param: msg: message.
    :param: username: username.
    :param: passw: password.
    :param: smtpserver: smtpserver."""

    header = 'From: %s\n'%fromAddr
    header += 'To: %s\n'%','.join(toAddr)
    header += 'Cc: %s\n'%','.join(ccAddr)
    header += 'Subject: %s\n\n'%subject
    msg = header + msg

    server = smtplib.SMTP(smtpserver)
    server.starttls()
    server.login(username, passw)
    problems = server.sendmail(fromAddr,toAddr,msg)
    server.quit()
    return problems

def main():
    """Main function"""
    print ("///// EMAIL SETUP /////")
    print ("From address:")
    fromAddress = input()
    print ("To address:")
    toAddress = [input()]
    print ("Cc address (optional):")
    ccAddress = [input()]
    print ("Subject:")
    subj = input()
    print ("Message:")
    message = input()
    print("Username:")
    uname = input()
    password =getpass.getpass()

    print("///// SENDING EMAIL /////")
    try :
        sendemail(fromAddress, toAddress, ccAddress,
              subj, message, uname, password)
        print("///// EMAIL SENT /////")

    except smtplib.SMTPAuthenticationError:
        print ("///// SOMETHING WENT WRONG ///// \n Username and password not accepted.")

if __name__ == "__main__":
    main()