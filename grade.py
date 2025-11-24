class student:
    def __init__(self, name, marks):
        self.name=name
        self.marks=marks
    def grade(self):
        if self.marks>=90:
            print(self.name,"got an A grade")
        elif self.marks>=75:
            print(self.name,"got B grade")
        else:
            print(self.name,"got a C grade")
s1=student("Anu",92)
s2=student("Rahul",80)
s3=student("Meera",60)
s1.grade()
s2.grade()
s3.grade()
