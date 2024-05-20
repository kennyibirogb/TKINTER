from tkinter import*

        
class StudentGrade:
    def __init__(self, root):
        self.root = root
        self.root.title('GRADE CALCULATOR')
        self.root.geometry('700x625')

    
        
        self.label = Label(root, text = 'KINDLY ENTER THE SCORE OF THE FOLLOWING SUBJECT:')
        self.label.grid(row = 0, column = 2)

        self.label1 = Label(root, text ='SUBJECT 1')
        self.label1.grid(row = 2, column = 0)

        self.label2 = Label(root, text = 'SUBJECT2')
        self.label2.grid(row = 3, column = 0)

        self.label3 = Label(root, text = 'SUBJECT3')
        self.label3.grid(row = 4, column = 0)

        self.label4 = Label(root, text = 'SUBJECT4')
        self.label4.grid(row = 5, column = 0)

        self.label5 = Label(root, text = 'RESULT')
        self.label5.grid(row = 9, column = 2)

        self.label6 = Label(root, text = 'TOTAL')
        self.label6.grid(row = 10, column = 0)

        self.label7 = Label(root, text = 'AVERAGE')
        self.label7.grid(row = 11, column = 0)

        self.label8 = Label(root, text = 'GRADE')
        self.label8.grid(row = 12, column = 0)
                        
        self.enter1 = Entry(root, width = '5', borderwidth = '5', bg = 'white')
        self.enter1.grid(row = 2, column = 1)

        self.enter2 = Entry(root, width = '5', borderwidth = '5', bg = 'white')
        self.enter2.grid(row = 3, column = 1)

        self.enter3 = Entry(root, width = '5', borderwidth = '5', bg = 'white')
        self.enter3.grid(row = 4, column = 1)

        self.enter4 = Entry(root, width = '5', borderwidth = '5', bg = 'white')
        self.enter4.grid(row = 5, column = 1)

        self.total = Entry(root, width = '5', borderwidth = '8', bg ='grey')
        self.total.grid(row = 10, column = 1)

        self.average = Entry(root, width = '5', borderwidth = '8', bg = 'grey')
        self.average.grid(row = 11, column = 1)

        self.grade = Entry(root, width = '5', borderwidth = '8', bg = 'grey')
        self.grade.grid(row = 12, column = 1)

        self.button = Button(root,text = 'calculate', padx = 10, pady =10,fg = 'black', bg = 'white',command = self.calculate)
        self.button.grid(row = 13, column = 2)
   
        

        
    def calculate(self):
        sub1 = int(self.enter1.get())
        sub2 = int(self.enter2.get())
        sub3 = int(self.enter3.get())
        sub4 = int(self.enter4.get())
            
        total = int(sub1 + sub2 + sub3 +sub4)
        self.total.delete(0, END)
        self.total.insert(0, total)

        average = total/4
        self.average.delete(0, END)
        self.average.insert(0, round(average, 2))


        if average >= 90:
            self.grade.delete(0, END)
            self.grade.insert(0, 'A')
        elif average >= 80:
            self.grade.delete(0, END)
            self.grade.insert(0, 'B')
        elif average >= 70:
            self.grade.delete(0, END)
            self.grade.insert(0, 'C')
        elif average >= 60:
            self.grade.delete(0, END)
            self.grade.insert(0, 'D')
        else:
            self.grade.delete(0, END)
            self.grade.insert(0, 'F')
            
if __name__ == '__main__':
    root = Tk()
    game = StudentGrade(root)
    root.mainloop()
