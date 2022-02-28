import pandas as pd
from tkinter import Menu, Entry, Label, ttk
from tkinter import *
import tkinter as tk
import os.path
from datetime import datetime


try:
    Users_Data = pd.DataFrame({
        'First_name':[],
        'Last_name':[],
        'User_name':[],
        'E-mail':[],
        'Password':[],
        'Date_of_birth':[],
        'Sign_up_date':[]
        })

    Current_User = pd.DataFrame({'Current User' : []})
    path = os.getcwd() + '/Admin/'
    os.mkdir(path)
    Users_Data.to_csv(path + 'Users.csv', index = False)
    Current_User.to_csv(path + 'CurrentUser.csv', index = False)
except:
    pass


class App(Tk):
    '''
        User Interface showing all needed tabs for the user to easy:
            View
            Send
            Edit
            Save
            Star
            Archive and 
            Delete his Emails
    '''
    def __init__(self):
        super(App, self).__init__()
 
        self.title("Karim Mailing System")
        self.minsize(500,500)
        self.geometry('1200x500')
        self.wm_iconbitmap("icon.ico")

        self.tabControl = ttk.Notebook(self)
        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tab3 = ttk.Frame(self.tabControl)
        self.tab4 = ttk.Frame(self.tabControl)
        self.tab5 = ttk.Frame(self.tabControl)
        self.tab6 = ttk.Frame(self.tabControl)
        self.tab7 = ttk.Frame(self.tabControl)
        self.tab8 = ttk.Frame(self.tabControl)
        self.tab9 = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tab1, text ='Sign In')
        self.tabControl.add(self.tab2, text ='Sign Up')
        self.tabControl.pack(expand = 1, fill ="both") 
        
        Sign_in_button = Button(self.tab1, text='Sign In', command = self.Sign_in, bg='#181915', fg='#f8f8f2', font=20)
        Sign_in_button.grid(row=16, column=0, pady=(20, 20), columnspan=2, ipadx=10, ipady=2)

        Email_label_sn = Label(self.tab1, text='E-mail', font=14)
        Password_label_sn = Label(self.tab1, text='Password', font=14)

        self.Email_sn = Entry(self.tab1, font=14, width=25)
        self.Password_sn = Entry(self.tab1, font=14, width=25)

        Email_label_sn.grid(row=4, column=0, pady=(25, 5))
        Password_label_sn.grid(row=6, column=0, pady=(25, 5))

        self.Email_sn.grid(row=4, column=1, pady=(25, 5), padx=(10,10))
        self.Password_sn.grid(row=6, column=1, pady=(25, 5), padx=(10,10))

        Sign_up_button = Button(self.tab2, text='Sign Up', command = self.Sign_up, bg='#181915', fg='#f8f8f2', font=20)
        Sign_up_button.grid(row=16, column=0, pady=(20, 20), columnspan=2, ipadx=10, ipady=2)

        FirstName_label_sp = Label(self.tab2, text='First Name', font=14)
        LastName_label_sp = Label(self.tab2, text='Last Name', font=14)
        UserName_label_sp = Label(self.tab2, text='UserName', font=14)
        Email_label_sp = Label(self.tab2, text='E-mail', font=14)
        Password_label_sp = Label(self.tab2, text='Password', font=14)
        Date_label_sp = Label(self.tab2, text='Date of Birth', font=14)

        self.FirstName_sp = Entry(self.tab2, font=14, width=25)
        self.LastName_sp = Entry(self.tab2, font=14, width=25)
        self.UserName_sp = Entry(self.tab2, font=14, width=25)
        self.Email_sp = Entry(self.tab2, font=14, width=25)
        self.Password_sp = Entry(self.tab2, font=14, width=25)
        self.Date_sp = Entry(self.tab2, font=14, width=25)

        FirstName_label_sp.grid(row=4, column=0, pady=(25, 5))
        LastName_label_sp.grid(row=6, column=0, pady=(25, 5))
        UserName_label_sp.grid(row=8, column=0, pady=(25, 5))
        Email_label_sp.grid(row=10, column=0, pady=(25, 5))
        Password_label_sp.grid(row=12, column=0, pady=(25, 5))
        Date_label_sp.grid(row=14, column=0, pady=(25, 5))

        self.FirstName_sp.grid(row=4, column=1, pady=(25, 5), padx=(10,10))
        self.LastName_sp.grid(row=6, column=1, pady=(25, 5), padx=(10,10))
        self.UserName_sp.grid(row=8, column=1, pady=(25, 5), padx=(10,10))
        self.Email_sp.grid(row=10, column=1, pady=(25, 5), padx=(10,10))
        self.Password_sp.grid(row=12, column=1, pady=(25, 5), padx=(10,10))
        self.Date_sp.grid(row=14, column=1, pady=(25, 5), padx=(10,10))

        Send_Email_button = Button(self.tab8, text='Send Email', command = self.Send_Email, bg='#181915', fg='#f8f8f2', font=20)
        Save_Draft_button = Button(self.tab8, text='Save Draft', command = self.Save_Draft, bg='#181915', fg='#f8f8f2', font=20)
        Send_Email_button.grid(row=8, column=0, pady=(20, 20), columnspan=2, ipadx=10, ipady=2)
        Save_Draft_button.grid(row=8, column=2, pady=(20, 20), columnspan=2, ipadx=10, ipady=2)


        From_label = Label(self.tab8, text='From', font=14)
        To_label = Label(self.tab8, text='To', font=14)
        Subject_label = Label(self.tab8, text='Subject', font=14)
        Compose_label = Label(self.tab8, text='Compose email', font=14)

        self.From = Entry(self.tab8, font=14, width=25)
        self.To = Entry(self.tab8, font=14, width=25)
        self.Subject = Entry(self.tab8, font=14, width=25)
        self.Compose = Text(self.tab8, font=14, height =10, width=40)


        From_label.grid(row=0, column=0, pady=(5, 5), padx=10)
        To_label.grid(row=2, column=0, pady=(5, 5), padx=10)
        Subject_label.grid(row=4, column=0, pady=(5, 5), padx=10)
        Compose_label.grid(row=6, column=0, pady=(5, 5), padx=10)
        
        self.From.grid(row=0, column=1, pady=(5, 5), padx=(10,10))
        self.To.grid(row=2, column=1, pady=(5, 5), padx=(10,10))
        self.Subject.grid(row=4, column=1, pady=(5, 5), padx=(10,10))
        self.Compose.grid(row=6, column=1, pady=(5, 5), padx=(10,10), ipady=20, ipadx = 20, columnspan=2)

        Sign_Out = Button(self.tab9, text='Sign Out', command = self.Sign_out, bg='#181915', fg='#f8f8f2', font=20)
        Sign_Out.pack(pady=80, ipadx=10, ipady=2)



    def Sign_up(self):
        '''
            Create New User by adding him to the users local database and then
            create the user data and folder according to his email address.
        '''
        try:
            path = os.getcwd() + '/Users/'
            os.mkdir(path)
        except:
            pass

        try:
            Sign_up_date = datetime.now()
            self.Sign_up_date = Sign_up_date.strftime("%d/%m/%Y %H:%M:%S")
            
            Email_Composition = pd.DataFrame({
                'From':[],
                'To':[],
                'Subject':[],
                'Compose E-mail':[],
                'Send_Date':[]
            })

            path = os.getcwd() + '/Users/' + self.Email_sp.get() + '/'
            os.mkdir(path)
            Email_Types = ['Inbox.csv','Sentbox.csv','Draft.csv','Archive.csv','Starred.csv', 'Deleted.csv']

            for Type in Email_Types:
                Email_Composition.to_csv(path + Type, index=False)

            path = os.getcwd() + '/Admin/Users.csv'
            Users_Data = pd.read_csv(path)
            df = pd.DataFrame(data=[[self.FirstName_sp.get(),
                                      self.LastName_sp.get(),
                                      self.UserName_sp.get(),
                                      self.Email_sp.get(),
                                      self.Password_sp.get(),
                                      self.Date_sp.get(),
                                      self.Sign_up_date]],

                               columns=['First_name', 
                                        'Last_name', 
                                        'User_name', 
                                        'E-mail', 
                                        'Password', 
                                        'Date_of_birth',
                                        'Sign_up_date'])

            Users_Data = pd.concat([Users_Data,df])
            Users_Data.to_csv(path, mode='w', index=False)
            Message = messagebox.showinfo('Message', 'You have successfully signed up')
            self.tabControl.select(0)
            self.FirstName_sp.delete(0, 'end')
            self.LastName_sp.delete(0, 'end')
            self.UserName_sp.delete(0, 'end')
            self.Email_sp.delete(0, 'end')
            self.Password_sp.delete(0, 'end')
            self.Date_sp.delete(0, 'end')
            

        except FileExistsError:
            Message = messagebox.askyesno('Message', 'User is already exist')
            if Message == 1:
                self.tabControl.select(1)
            else:
                self.tabControl.select(0)
            print('User is already exist')

    def Sign_in(self):
        '''
            Get user Email and password and check them to sign in successfully
        '''
        path = os.getcwd() + '/Admin/Users.csv'
        Users_Data = pd.read_csv(path)

        if self.Email_sn.get() in Users_Data.values and self.Password_sn.get() in Users_Data.values:
            # messagebox.showinfo('Message', 'You have successfully signed in')
            self.tabControl.hide(1)
            self.tabControl.add(self.tab3, text ='Inbox')
            self.tabControl.add(self.tab4, text ='Sentbox')
            self.tabControl.add(self.tab5, text ='Draft')
            self.tabControl.add(self.tab6, text ='Archived')
            self.tabControl.add(self.tab7, text ='Starred')
            self.tabControl.add(self.tab8, text ='Send Email')
            self.tabControl.add(self.tab9, text ='Sign Out')
            self.tabControl.select(2)
            self.From.insert(0,self.Email_sn.get())
            print('You have successfully signed in')
            self.ImportUserData()
        else:
            messagebox.showwarning('Message', 'E-mail or password is incorrect')
            print('E-mail or password is incorrect')

    def Send_Email(self):
        '''
            Send Emails to another account
        '''
        Send_Date = datetime.now()
        self.Send_Date = Send_Date.strftime("%d/%m/%Y %H:%M:%S")

        path = os.getcwd() + '/Admin/Users.csv'
        Users_Data = pd.read_csv(path)

        if self.To.get() in Users_Data.values or self.ToEn.get() in Users_Data.values:
            path = os.getcwd() + '/Users/' + self.To.get() + '/Inbox.csv'

            if path == os.getcwd() + '/Users/' + '/Inbox.csv':
                path = os.getcwd() + '/Users/' + self.ToEn.get() + '/Inbox.csv'
                df = pd.DataFrame(data=[[ self.From.get(),
                                      self.ToEn.get(),
                                      self.SubjectEn.get(),
                                      self.ComposeEn.get("1.0",END),
                                      self.Send_Date]],

                               columns=['From',
                                        'To', 
                                        'Subject', 
                                        'Compose E-mail', 
                                        'Send_Date'])
            else:    
                df = pd.DataFrame(data=[[ self.From.get(),
                                          self.To.get(),
                                          self.Subject.get(),
                                          self.Compose.get("1.0",END),
                                          self.Send_Date]],

                                   columns=['From',
                                            'To', 
                                            'Subject', 
                                            'Compose E-mail', 
                                            'Send_Date'])
            Inbox = pd.read_csv(path)
            Inbox = pd.concat([Inbox,df])
            Inbox.to_csv(path, mode='w', index=False)

            path = os.getcwd() + '/Users/' + self.Email_sn.get() + '/Sentbox.csv'
            Sentbox = pd.read_csv(path)
            Sentbox = pd.concat([Sentbox,df])
            Sentbox.to_csv(path, mode='w', index=False)
            self.To.delete(0, 'end')
            self.Subject.delete(0, 'end')
            self.Compose.delete('1.0', END)
            self.tab3.after(10, self.ImportUserData)
        else:
            messagebox.showwarning('Message', 'E-mail you are sending to is incorrect')



    def Save_Draft(self):
        '''
            Save Email as a draft and the user can view, edit, and send it later
        '''
        Send_Date = datetime.now()
        self.Send_Date = Send_Date.strftime("%d/%m/%Y %H:%M:%S")

        path = os.getcwd() + '/Admin/Users.csv'
        Users_Data = pd.read_csv(path)

        if self.Email_sn.get() in Users_Data.values:
            path = os.getcwd() + '/Users/' + self.Email_sn.get() + '/Draft.csv'
            Draft = pd.read_csv(path)

            df = pd.DataFrame(data=[[ self.From.get(),
                                      self.To.get(),
                                      self.Subject.get(),
                                      self.Compose.get("1.0",END),
                                      self.Send_Date]],

                               columns=['From',
                                        'To', 
                                        'Subject', 
                                        'Compose E-mail', 
                                        'Send_Date'])

            Draft = pd.concat([Draft,df])
            Draft.to_csv(path, mode='w', index=False)
            self.To.delete(0, 'end')
            self.Subject.delete(0, 'end')
            self.Compose.delete('1.0', END)
            self.tab3.after(10, self.ImportUserData)
          

    def Save_Draft2(self):
        Send_Date = datetime.now()
        self.Send_Date = Send_Date.strftime("%d/%m/%Y %H:%M:%S")

        path = os.getcwd() + '/Admin/Users.csv'
        Users_Data = pd.read_csv(path)

        if self.FromEn.get() in Users_Data.values:
            path = os.getcwd() + '/Users/' + self.Email_sn.get() + '/Draft.csv'
            Draft = pd.read_csv(path)

            df = pd.DataFrame(data=[[ self.FromEn.get(),
                                      self.ToEn.get(),
                                      self.SubjectEn.get(),
                                      self.ComposeEn.get("1.0",END),
                                      self.Send_Date]],

                               columns=['From',
                                        'To', 
                                        'Subject', 
                                        'Compose E-mail', 
                                        'Send_Date'])

            Draft = pd.concat([Draft,df])
            Draft.to_csv(path, mode='w', index=False)
            self.To.delete(0, 'end')
            self.Subject.delete(0, 'end')
            self.Compose.delete('1.0', END)
            self.tab3.after(10, self.ImportUserData)
  

    def Edit_Draft(self):
        '''
            View and Edit Selected Draft Emails to send them or save them again 
        '''
        try:
            Send_Date = datetime.now()
            self.Send_Date = Send_Date.strftime("%d/%m/%Y %H:%M:%S")

            path = os.getcwd() + '/Admin/Users.csv'
            Users_Data = pd.read_csv(path)

            if self.Email_sn.get() in Users_Data.values:
                path = os.getcwd() + '/Users/' + self.Email_sn.get() + '/Draft.csv'
                Users_Data = pd.read_csv(path)
                self.View(2)
                self.Delete(2)
            self.tab3.after(10, self.ImportUserData)

        except:
            pass            
  

    def View(self, Where):
        '''
            View Selected Emails
        '''
        try:
            Email_Types = ['Inbox.csv','Sentbox.csv','Draft.csv','Archive.csv','Starred.csv', 'Deleted.csv']
            path = os.getcwd() + '/Users/' + self.Email_sn.get() + '/' + Email_Types[Where]
            Users_Data = pd.read_csv(path)

            View = Tk()
            View.title('E-mail')
            View.geometry('600x350')
            View.wm_iconbitmap("icon.ico")
            
            if Where == 0:
                Selected_Email = int(str(self.Email_List1.curselection()).replace('(','').replace(')','').replace(',',''))

            elif Where == 1:
                Selected_Email = int(str(self.Email_List2.curselection()).replace('(','').replace(')','').replace(',',''))

            elif Where == 2:
                View.geometry('600x400')
                Selected_Email = int(str(self.Email_List3.curselection()).replace('(','').replace(')','').replace(',',''))
                Send_Email_button = Button(View, text='Send Email', command = self.Send_Email, bg='#181915', fg='#f8f8f2', font=20).grid(row=8, column=0, pady=(20, 20), columnspan=2, ipadx=10, ipady=2)
                Save_Draft_button = Button(View, text='Save Draft', command = self.Save_Draft2, bg='#181915', fg='#f8f8f2', font=20).grid(row=8, column=2, pady=(20, 20), columnspan=2, ipadx=10, ipady=2)

            elif Where == 3:
                Selected_Email = int(str(self.Email_List4.curselection()).replace('(','').replace(')','').replace(',',''))  

            elif Where == 4:
                Selected_Email = int(str(self.Email_List5.curselection()).replace('(','').replace(')','').replace(',',''))

            
            From = Users_Data.at[(len(Users_Data.index)-(Selected_Email+1)), 'From']
            To = Users_Data.at[(len(Users_Data.index)-(Selected_Email+1)), 'To']
            Subject = Users_Data.at[(len(Users_Data.index)-(Selected_Email+1)), 'Subject']
            Content = Users_Data.at[(len(Users_Data.index)-(Selected_Email+1)), 'Compose E-mail']

            From_label = Label(View, text='From', font=14)
            To_label = Label(View, text='To', font=14)
            Subject_label = Label(View, text='Subject', font=14)
            Compose_label = Label(View, text='Compose email', font=14)

            self.FromEn = Entry(View, font=14, width=25)
            self.ToEn = Entry(View, font=14, width=25)
            self.SubjectEn = Entry(View, font=14, width=25)
            self.ComposeEn = Text(View, font=14, height =10, width=40)

            self.FromEn.insert(0,From)
            self.ToEn.insert(0,To)
            self.SubjectEn.insert(0,Subject)
            self.ComposeEn.insert('1.0',Content)

            From_label.grid(row=0, column=0, pady=(5, 5), padx=10)
            To_label.grid(row=2, column=0, pady=(5, 5), padx=10)
            Subject_label.grid(row=4, column=0, pady=(5, 5), padx=10)
            Compose_label.grid(row=6, column=0, pady=(5, 5), padx=10)
            
            self.FromEn.grid(row=0, column=1, pady=(5, 5), padx=(10,10))
            self.ToEn.grid(row=2, column=1, pady=(5, 5), padx=(10,10))
            self.SubjectEn.grid(row=4, column=1, pady=(5, 5), padx=(10,10))
            self.ComposeEn.grid(row=6, column=1, pady=(5, 5), padx=(10,10), ipady=20, ipadx = 20, columnspan=2)

        except:
            pass


    def Star(self):
        '''
            Star or Mark Selected Emails
        '''
        try:    
            Email_Types = ['Inbox.csv','Sentbox.csv','Draft.csv','Archive.csv','Starred.csv', 'Deleted.csv']
            path = os.getcwd() + '/Users/' + self.Email_sn.get() + '/' + Email_Types[0]
            Users_Data = pd.read_csv(path)

            Selected_Email = int(str(self.Email_List1.curselection()).replace('(','').replace(')','').replace(',',''))
            
            From = Users_Data.at[(len(Users_Data.index)-(Selected_Email+1)), 'From']
            To = Users_Data.at[(len(Users_Data.index)-(Selected_Email+1)), 'To']
            Subject = Users_Data.at[(len(Users_Data.index)-(Selected_Email+1)), 'Subject']
            Content = Users_Data.at[(len(Users_Data.index)-(Selected_Email+1)), 'Compose E-mail']
            Date = Users_Data.at[(len(Users_Data.index)-(Selected_Email+1)), 'Send_Date']

            df = pd.DataFrame(data=[[ From,
                                      To,
                                      Subject,
                                      Content,
                                      Date]],

                              columns=['From',
                                       'To', 
                                       'Subject', 
                                       'Compose E-mail', 
                                       'Send_Date'])

            path = os.getcwd() + '/Users/' + self.Email_sn.get() + '/' + Email_Types[4]
            Users_Data = pd.read_csv(path)
            Starred = pd.concat([Users_Data,df])
            Starred.to_csv(path, mode='w', index=False)
            self.tab3.after(10, self.ImportUserData)

        except:
            pass

    def Archive(self, Where):
        '''
            Archive Selected Emails
        '''
        try:
            Email_Types = ['Inbox.csv','Sentbox.csv','Draft.csv','Archive.csv','Starred.csv', 'Deleted.csv']
            path = os.getcwd() + '/Users/' + self.Email_sn.get() + '/' + Email_Types[Where]
            Users_Data = pd.read_csv(path)
            
            if Where == 0:
                Selected_Email = int(str(self.Email_List1.curselection()).replace('(','').replace(')','').replace(',',''))
                self.Email_List1.delete(Selected_Email)
            elif Where == 1:
                Selected_Email = int(str(self.Email_List2.curselection()).replace('(','').replace(')','').replace(',',''))
                self.Email_List2.delete(Selected_Email)


            From = Users_Data.at[(len(Users_Data.index)-(Selected_Email+1)), 'From']
            To = Users_Data.at[(len(Users_Data.index)-(Selected_Email+1)), 'To']
            Subject = Users_Data.at[(len(Users_Data.index)-(Selected_Email+1)), 'Subject']
            Content = Users_Data.at[(len(Users_Data.index)-(Selected_Email+1)), 'Compose E-mail']
            Date = Users_Data.at[(len(Users_Data.index)-(Selected_Email+1)), 'Send_Date']

            Archived_row = pd.DataFrame(data=[[From,
                                              To,
                                              Subject,
                                              Content,
                                              Date]],

                                   columns=['From',
                                            'To', 
                                            'Subject', 
                                            'Compose E-mail', 
                                            'Send_Date'])
            

            Users_Data.drop((len(Users_Data.index)-1-Selected_Email), axis=0, inplace=True)
            Users_Data.to_csv(path, mode='w', index=False)

            path = os.getcwd() + '/Users/' + self.Email_sn.get() + '/' + Email_Types[3]
            Users_Data = pd.read_csv(path)
            Archived = pd.concat([Users_Data,Archived_row])
            Archived.to_csv(path, mode='w', index=False)
            self.tab3.after(10, self.ImportUserData)

        except:
            pass

    def Delete(self, Where):
        '''
            Delete Selected Emails
        '''
        try:
            Email_Types = ['Inbox.csv','Sentbox.csv','Draft.csv','Archive.csv','Starred.csv', 'Deleted.csv']
            path = os.getcwd() + '/Users/' + self.Email_sn.get() + '/' + Email_Types[Where]
            Users_Data = pd.read_csv(path)
            
            if Where == 0:
                Selected_Email = int(str(self.Email_List1.curselection()).replace('(','').replace(')','').replace(',',''))
                self.Email_List1.delete(Selected_Email)
            elif Where == 1:
                Selected_Email = int(str(self.Email_List2.curselection()).replace('(','').replace(')','').replace(',',''))
                self.Email_List2.delete(Selected_Email)
            elif Where == 2:
                Selected_Email = int(str(self.Email_List3.curselection()).replace('(','').replace(')','').replace(',',''))
                self.Email_List3.delete(Selected_Email)
            elif Where == 3:
                Selected_Email = int(str(self.Email_List4.curselection()).replace('(','').replace(')','').replace(',',''))
                self.Email_List4.delete(Selected_Email)   
            elif Where == 4:
                Selected_Email = int(str(self.Email_List5.curselection()).replace('(','').replace(')','').replace(',',''))
                self.Email_List5.delete(Selected_Email)

            From = Users_Data.at[(len(Users_Data.index)-(Selected_Email+1)), 'From']
            To = Users_Data.at[(len(Users_Data.index)-(Selected_Email+1)), 'To']
            Subject = Users_Data.at[(len(Users_Data.index)-(Selected_Email+1)), 'Subject']
            Content = Users_Data.at[(len(Users_Data.index)-(Selected_Email+1)), 'Compose E-mail']
            Date = Users_Data.at[(len(Users_Data.index)-(Selected_Email+1)), 'Send_Date']

            Deleted_row = pd.DataFrame(data=[[From,
                                              To,
                                              Subject,
                                              Content,
                                              Date]],

                                   columns=['From',
                                            'To', 
                                            'Subject', 
                                            'Compose E-mail', 
                                            'Send_Date'])
            

            Users_Data.drop((len(Users_Data.index)-1-Selected_Email), axis=0, inplace=True)
            Users_Data.to_csv(path, mode='w', index=False)

            if Where ==2:
                pass
            else:
                path = os.getcwd() + '/Users/' + self.Email_sn.get() + '/' + Email_Types[5]
                Users_Data = pd.read_csv(path)
                Deleted = pd.concat([Users_Data,Deleted_row])
                Deleted.to_csv(path, mode='w', index=False)
                self.tab3.after(10, self.ImportUserData)
        except:
            pass



    def Sign_out(self):
        '''
            Sign out
        '''
        self.tabControl.add(self.tab2, text ='Sign Up')
        self.Email_sn.delete(0, 'end')
        self.Password_sn.delete(0, 'end')
        self.From.delete(0, 'end')
        self.tabControl.select(0)
        for i in range(2,9,1):
            self.tabControl.hide(i)



    def ImportUserData(self):
        '''
            Import All User Emails (Inbox, Sentbox, Draft, Archive, Starred)
            to view them at the user interface.
        '''
        path = os.getcwd() + '/Users/' + self.Email_sn.get() + '/'
        Email_Types = ['Inbox.csv','Sentbox.csv','Draft.csv','Archive.csv','Starred.csv']
        
        self.Email_List1 = MultiListbox(self.tab3, (('From', 30), ('Content', 100), ('Date', 15)))
        self.Email_List2 = MultiListbox(self.tab4, (('To', 30), ('Content', 100), ('Date', 15)))
        self.Email_List3 = MultiListbox(self.tab5, (('To', 30), ('Content', 100), ('Date', 15)))
        self.Email_List4 = MultiListbox(self.tab6, (('From', 30), ('Content', 100), ('Date', 15)))
        self.Email_List5 = MultiListbox(self.tab7, (('From', 30), ('Content', 100), ('Date', 15)))

        
        self.Email_List1.grid(row=0, column=1, padx=5, pady=5, ipady=110, ipadx=150, columnspan=8)
        self.Email_List2.grid(row=0, column=1, padx=5, pady=5, ipady=110, ipadx=150, columnspan=6)
        self.Email_List3.grid(row=0, column=1, padx=5, pady=5, ipady=110, ipadx=150, columnspan=4)
        self.Email_List4.grid(row=0, column=1, padx=5, pady=5, ipady=110, ipadx=150, columnspan=4)
        self.Email_List5.grid(row=0, column=1, padx=5, pady=5, ipady=110, ipadx=150, columnspan=6)


        View_button1 = Button(self.tab3, text='View', command = lambda: self.View(0), bg='#181915', fg='#f8f8f2', font=20)
        Archive_button1 = Button(self.tab3, text='Archive', command = lambda: self.Archive(0), bg='#181915', fg='#f8f8f2', font=20)
        Star_button1 = Button(self.tab3, text='Star', command = self.Star, bg='#181915', fg='#f8f8f2', font=20)
        Delete_button1 = Button(self.tab3, text='Delete', command = lambda: self.Delete(0), bg='#181915', fg='#f8f8f2', font=20)

        View_button1.grid(row=8, column=0, pady=(20, 20), columnspan=2, ipadx=10, ipady=2)
        Archive_button1.grid(row=8, column=2, pady=(20, 20), columnspan=2, ipadx=10, ipady=2)
        Star_button1.grid(row=8, column=4, pady=(20, 20), columnspan=2, ipadx=10, ipady=2)
        Delete_button1.grid(row=8, column=6, pady=(20, 20), columnspan=2, ipadx=10, ipady=2)


        View_button2 = Button(self.tab4, text='View', command = lambda: self.View(1), bg='#181915', fg='#f8f8f2', font=20)
        Archive_button2 = Button(self.tab4, text='Archive', command = lambda: self.Archive(1), bg='#181915', fg='#f8f8f2', font=20)
        Delete_button2 = Button(self.tab4, text='Delete', command = lambda: self.Delete(1), bg='#181915', fg='#f8f8f2', font=20)

        View_button2.grid(row=8, column=0, pady=(20, 20), columnspan=2, ipadx=10, ipady=2)
        Archive_button2.grid(row=8, column=2, pady=(20, 20), columnspan=2, ipadx=10, ipady=2)
        Delete_button2.grid(row=8, column=4, pady=(20, 20), columnspan=2, ipadx=10, ipady=2)


        Edit_button3 = Button(self.tab5, text='Edit Draft', command = self.Edit_Draft, bg='#181915', fg='#f8f8f2', font=20)
        Delete_button3 = Button(self.tab5, text='Delete', command = lambda: self.Delete(2), bg='#181915', fg='#f8f8f2', font=20)
        
        Edit_button3.grid(row=8, column=0, pady=(20, 20), columnspan=2, ipadx=10, ipady=2)
        Delete_button3.grid(row=8, column=2, pady=(20, 20), columnspan=2, ipadx=10, ipady=2)

        View_button4 = Button(self.tab6, text='View', command = lambda: self.View(3), bg='#181915', fg='#f8f8f2', font=20)
        Delete_button4 = Button(self.tab6, text='Delete', command = lambda: self.Delete(3), bg='#181915', fg='#f8f8f2', font=20)
        
        View_button4.grid(row=8, column=0, pady=(20, 20), columnspan=2, ipadx=10, ipady=2)
        Delete_button4.grid(row=8, column=2, pady=(20, 20), columnspan=2, ipadx=10, ipady=2) 

        View_button5 = Button(self.tab7, text='View', command = lambda: self.View(4), bg='#181915', fg='#f8f8f2', font=20)
        Delete_button5 = Button(self.tab7, text='Unstar', command = lambda: self.Delete(4), bg='#181915', fg='#f8f8f2', font=20)

        View_button5.grid(row=8, column=0, pady=(20, 20), columnspan=2, ipadx=10, ipady=2)
        Delete_button5.grid(row=8, column=4, pady=(20, 20), columnspan=2, ipadx=10, ipady=2) 


        Users_Data = pd.read_csv(path + Email_Types[0])
        for i in range(len(Users_Data.index)-1,-1,-1):        
            From = Users_Data.at[i, 'From']
            Content = Users_Data.at[i, 'Compose E-mail']
            Date = Users_Data.at[i, 'Send_Date']
            self.Email_List1.insert(END, (From, Content, Date))
    
        Users_Data = pd.read_csv(path + Email_Types[1])
        for i in range(len(Users_Data.index)-1,-1,-1):        
            From = Users_Data.at[i, 'To']
            Content = Users_Data.at[i, 'Compose E-mail']
            Date = Users_Data.at[i, 'Send_Date']
            self.Email_List2.insert(END, (From, Content, Date))

        Users_Data = pd.read_csv(path + Email_Types[2])
        for i in range(len(Users_Data.index)-1,-1,-1):        
            From = Users_Data.at[i, 'To']
            Content = Users_Data.at[i, 'Compose E-mail']
            Date = Users_Data.at[i, 'Send_Date']
            self.Email_List3.insert(END, (From, Content, Date))

        Users_Data = pd.read_csv(path + Email_Types[3])
        for i in range(len(Users_Data.index)-1,-1,-1):        
            From = Users_Data.at[i, 'From']
            Content = Users_Data.at[i, 'Compose E-mail']
            Date = Users_Data.at[i, 'Send_Date']
            self.Email_List4.insert(END, (From, Content, Date))

        Users_Data = pd.read_csv(path + Email_Types[4])
        for i in range(len(Users_Data.index)-1,-1,-1):        
            From = Users_Data.at[i, 'From']
            Content = Users_Data.at[i, 'Compose E-mail']
            Date = Users_Data.at[i, 'Send_Date']
            self.Email_List5.insert(END, (From, Content, Date))   
        

        
class MultiListbox(Frame):
    '''
        Multi-listbox viewr to create a table that organize the emails that 
        will be viewed later and also to excute the functions on the selected emails.

        This Class is not my own code, it is taken from this link:
            https://www.oreilly.com/library/view/python-cookbook/0596001673/ch09s05.html
    '''
    def __init__(self, master, lists):
        Frame.__init__(self, master)
        self.lists = []
        for l,w in lists:
            frame = Frame(self); 
            frame.pack(side=LEFT, expand=YES, fill=BOTH)
            Label(frame, text=l, borderwidth=1, relief=RAISED).pack(fill=X)
            lb = Listbox(frame, width=w, borderwidth=0, selectborderwidth=0,
                         relief=FLAT, exportselection=FALSE)
            lb.pack(expand=YES, fill=BOTH)
            
            self.lists.append(lb)
            lb.bind('<B1-Motion>', lambda e, s=self: s._select(e.y))
            lb.bind('<Button-1>', lambda e, s=self: s._select(e.y))
            lb.bind('<Leave>', lambda e: 'break')
            lb.bind('<B2-Motion>', lambda e, s=self: s._b2motion(e.x, e.y))
            lb.bind('<Button-2>', lambda e, s=self: s._button2(e.x, e.y))

        frame = Frame(self); frame.pack(side=LEFT, fill=Y)
        Label(frame, borderwidth=1, relief=RAISED).pack(fill=X)
        sb = Scrollbar(frame, orient=VERTICAL, command=self._scroll)
        sb.pack(expand=YES, fill=Y)
        self.lists[0]['yscrollcommand']=sb.set

    def _select(self, y):
        row = self.lists[0].nearest(y)
        self.selection_clear(0, END)
        self.selection_set(row)
        return 'break'

    def _button2(self, x, y):
        for l in self.lists: l.scan_mark(x, y)
        return 'break'

    def _b2motion(self, x, y):
        for l in self.lists: l.scan_dragto(x, y)
        return 'break'

    def _scroll(self, *args):
        for l in self.lists:
            apply(l.yview, args)

    def curselection(self):
        return self.lists[0].curselection()

    def delete(self, first, last=None):
        for l in self.lists:
            l.delete(first, last)

    def get(self, first, last=None):
        result = []
        for l in self.lists:
            result.append(l.get(first,last))
        if last: return apply(map, [None] + result)
        return result

    def index(self, ANCHOR):
        self.lists[0].index(ANCHOR)

    def insert(self, index, *elements):
        for e in elements:
            i = 0
            for l in self.lists:
                l.insert(index, e[i])
                i = i + 1

    def size(self):
        return self.lists[0].size(  )

    def see(self, index):
        for l in self.lists:
            l.see(index)

    def selection_anchor(self, index):
        for l in self.lists:
            l.selection_anchor(index)

    def selection_clear(self, first, last=None):
        for l in self.lists:
            l.selection_clear(first, last)

    def selection_includes(self, index):
        return self.lists[0].selection_includes(index)

    def selection_set(self, first, last=None):
        for l in self.lists:
            l.selection_set(first, last)



app = App()
app.mainloop()