"""
Advanced University Management System — Tkinter GUI
File: university_gui.py

Features:
- Dashboard-style GUI with sidebar navigation
- Pages for Departments, Students, Faculty, Courses
- Treeview tables for listing items with add/edit/delete
- JSON persistence (university_gui_data.json)
- Clean OOP models and serialization/deserialization

How to run:
1. Save this file as university_gui.py
2. Run: python university_gui.py (Python 3.8+ recommended)

"""
import json
import os
import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

DATA_FILE = "university_gui_data.json"

# -----------------------------
# Data models with (de)serialization
# -----------------------------
class Course:
    def __init__(self, course_name, course_code):
        self.course_name = course_name
        self.course_code = course_code

    def to_dict(self):
        return {"course_name": self.course_name, "course_code": self.course_code}

    @staticmethod
    def from_dict(d):
        return Course(d["course_name"], d["course_code"]) 


class Person:
    def __init__(self, name, id_no):
        self.name = name
        self.id_no = id_no

    def to_dict(self):
        return {"name": self.name, "id_no": self.id_no}


class Student(Person):
    def __init__(self, name, id_no, course, fees):
        super().__init__(name, id_no)
        self.course = course
        self._fees = fees

    def to_dict(self):
        d = super().to_dict()
        d.update({"course": self.course, "fees": self._fees})
        return d

    @staticmethod
    def from_dict(d):
        return Student(d["name"], d["id_no"], d["course"], d.get("fees", 0))


class Staff(Person):
    def __init__(self, name, id_no, position, salary):
        super().__init__(name, id_no)
        self.position = position
        self._salary = salary

    def to_dict(self):
        d = super().to_dict()
        d.update({"position": self.position, "salary": self._salary})
        return d

    @staticmethod
    def from_dict(d):
        return Staff(d["name"], d["id_no"], d.get("position", ""), d.get("salary", 0))


class Faculty(Staff):
    def __init__(self, name, id_no, subject, salary):
        super().__init__(name, id_no, "Faculty", salary)
        self.subject = subject
        self.courses = []

    def assign_course(self, course):
        self.courses.append(course)

    def to_dict(self):
        d = super().to_dict()
        d.update({"subject": self.subject, "courses": [c.to_dict() for c in self.courses]})
        return d

    @staticmethod
    def from_dict(d):
        f = Faculty(d["name"], d["id_no"], d.get("subject", ""), d.get("salary", 0))
        for c in d.get("courses", []):
            f.courses.append(Course.from_dict(c))
        return f


class Department:
    def __init__(self, name):
        self.dept_name = name
        self.faculty_members = []
        self.employees = []
        self.courses = []
        self.students = []

    def to_dict(self):
        return {
            "dept_name": self.dept_name,
            "faculty": [f.to_dict() for f in self.faculty_members],
            "employees": [e.to_dict() for e in self.employees],
            "courses": [c.to_dict() for c in self.courses],
            "students": [s.to_dict() for s in self.students]
        }

    @staticmethod
    def from_dict(d):
        dep = Department(d["dept_name"])
        for f in d.get("faculty", []):
            dep.faculty_members.append(Faculty.from_dict(f))
        for e in d.get("employees", []):
            dep.employees.append(Staff.from_dict(e))
        for c in d.get("courses", []):
            dep.courses.append(Course.from_dict(c))
        for s in d.get("students", []):
            dep.students.append(Student.from_dict(s))
        return dep


class University:
    def __init__(self, name="Uttaranchal University", address="Dehradun, Uttarakhand"):
        self.university_name = name
        self.address = address
        self.departments = []
        self.admin_staff = []

    def to_dict(self):
        return {
            "university_name": self.university_name,
            "address": self.address,
            "departments": [d.to_dict() for d in self.departments],
            "admin_staff": [s.to_dict() for s in self.admin_staff]
        }

    @staticmethod
    def from_dict(d):
        u = University(d.get("university_name", "Uttaranchal University"), d.get("address", "Dehradun"))
        for s in d.get("admin_staff", []):
            u.admin_staff.append(Staff.from_dict(s))
        for dep in d.get("departments", []):
            u.departments.append(Department.from_dict(dep))
        return u


# -----------------------------
# Persistence helpers
# -----------------------------

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                data = json.load(f)
                return University.from_dict(data)
            except Exception as e:
                print("Error loading JSON:", e)
    return University()


def save_data(university):
    with open(DATA_FILE, "w") as f:
        json.dump(university.to_dict(), f, indent=4)


# -----------------------------
# GUI Application
# -----------------------------
class UniversityApp(tk.Tk):
    def __init__(self, uni: University):
        super().__init__()
        self.title("University Management System")
        self.geometry("1000x600")
        self.uni = uni

        self.style = ttk.Style(self)
        # Use default theme

        self._create_widgets()

    def _create_widgets(self):
        # Sidebar frame
        sidebar = tk.Frame(self, width=200, bg="#2b2b2b")
        sidebar.pack(side=tk.LEFT, fill=tk.Y)

        brand = tk.Label(sidebar, text=self.uni.university_name, bg="#2b2b2b", fg="white", font=(None, 11, "bold"), wraplength=180, justify=tk.CENTER)
        brand.pack(pady=12)

        btn_dashboard = tk.Button(sidebar, text="Dashboard", command=self.show_dashboard, width=22)
        btn_departments = tk.Button(sidebar, text="Departments", command=self.show_departments_frame, width=22)
        btn_students = tk.Button(sidebar, text="Students", command=self.show_students_frame, width=22)
        btn_faculty = tk.Button(sidebar, text="Faculty", command=self.show_faculty_frame, width=22)
        btn_courses = tk.Button(sidebar, text="Courses", command=self.show_courses_frame, width=22)
        btn_save = tk.Button(sidebar, text="Save Now", command=self.save_all, width=22)
        btn_quit = tk.Button(sidebar, text="Exit", command=self.on_close, width=22)

        for b in (btn_dashboard, btn_departments, btn_students, btn_faculty, btn_courses, btn_save, btn_quit):
            b.pack(pady=6)

        # Main container for pages
        self.container = tk.Frame(self, bg="#f0f0f0")
        self.container.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create frames
        self.frames = {}
        for F in (DashboardFrame, DepartmentsFrame, StudentsFrame, FacultyFrame, CoursesFrame):
            frame = F(parent=self.container, controller=self)
            self.frames[F.__name__] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_dashboard()

    def show_frame(self, name):
        frame = self.frames[name]
        frame.refresh()
        frame.tkraise()

    def show_dashboard(self):
        self.show_frame('DashboardFrame')

    def show_departments_frame(self):
        self.show_frame('DepartmentsFrame')

    def show_students_frame(self):
        self.show_frame('StudentsFrame')

    def show_faculty_frame(self):
        self.show_frame('FacultyFrame')

    def show_courses_frame(self):
        self.show_frame('CoursesFrame')

    def save_all(self):
        save_data(self.uni)
        messagebox.showinfo("Saved", "All data saved to disk.")

    def on_close(self):
        if messagebox.askyesno("Exit", "Save before exit?"):
            save_data(self.uni)
        self.destroy()


# -----------------------------
# Dashboard Frame
# -----------------------------
class DashboardFrame(tk.Frame):
    def __init__(self, parent, controller: UniversityApp):
        super().__init__(parent)
        self.controller = controller
        self._build()

    def _build(self):
        lbl = tk.Label(self, text="Dashboard", font=(None, 16, "bold"))
        lbl.pack(pady=10)

        self.summary = tk.Label(self, text="", justify=tk.LEFT, anchor="nw", font=(None, 11))
        self.summary.pack(fill=tk.BOTH, expand=True, padx=12, pady=8)

    def refresh(self):
        uni = self.controller.uni
        total_depts = len(uni.departments)
        total_students = sum(len(d.students) for d in uni.departments)
        total_faculty = sum(len(d.faculty_members) for d in uni.departments)
        total_courses = sum(len(d.courses) for d in uni.departments)
        admin = len(uni.admin_staff)

        txt = f"University: {uni.university_name}\nAddress: {uni.address}\n\n"
        txt += f"Departments: {total_depts}\nStudents: {total_students}\nFaculty: {total_faculty}\nCourses: {total_courses}\nAdmin Staff: {admin}\n"

        self.summary.config(text=txt)


# -----------------------------
# Departments Frame
# -----------------------------
class DepartmentsFrame(tk.Frame):
    def __init__(self, parent, controller: UniversityApp):
        super().__init__(parent)
        self.controller = controller
        self._build()

    def _build(self):
        top = tk.Frame(self)
        top.pack(fill=tk.X, pady=6)
        tk.Label(top, text="Departments", font=(None, 14, "bold")).pack(side=tk.LEFT, padx=8)

        btn_add = tk.Button(top, text="Add Dept", command=self.add_department)
        btn_add.pack(side=tk.RIGHT, padx=8)

        btn_del = tk.Button(top, text="Delete Dept", command=self.delete_selected)
        btn_del.pack(side=tk.RIGHT)

        # Treeview
        cols = ("#1", "#2", "#3", "#4")
        self.tree = ttk.Treeview(self, columns=cols, show="headings")
        self.tree.heading("#1", text="Index")
        self.tree.heading("#2", text="Department Name")
        self.tree.heading("#3", text="#Students")
        self.tree.heading("#4", text="#Faculty")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

        self.tree.bind('<Double-1>', self.on_double)

    def refresh(self):
        for r in self.tree.get_children():
            self.tree.delete(r)
        for i, d in enumerate(self.controller.uni.departments, start=1):
            self.tree.insert('', 'end', values=(i, d.dept_name, len(d.students), len(d.faculty_members)))

    def add_department(self):
        name = simpledialog.askstring("Add Department", "Department Name:")
        if name:
            self.controller.uni.departments.append(Department(name))
            save_data(self.controller.uni)
            self.refresh()

    def delete_selected(self):
        sel = self.tree.selection()
        if not sel:
            messagebox.showwarning("No selection", "Select a department to delete.")
            return
        idx = int(self.tree.item(sel[0])["values"][0]) - 1
        dep = self.controller.uni.departments[idx]
        if messagebox.askyesno("Confirm", f"Delete department '{dep.dept_name}'? This will remove all its data."):
            del self.controller.uni.departments[idx]
            save_data(self.controller.uni)
            self.refresh()

    def on_double(self, event):
        sel = self.tree.selection()
        if not sel:
            return
        idx = int(self.tree.item(sel[0])["values"][0]) - 1
        dep = self.controller.uni.departments[idx]
        DeptDetailWindow(self, dep, self.controller.uni)


# -----------------------------
# Dept Detail Window
# -----------------------------
class DeptDetailWindow(tk.Toplevel):
    def __init__(self, parent, department: Department, uni: University):
        super().__init__(parent)
        self.title(f"Department - {department.dept_name}")
        self.geometry("800x500")
        self.dep = department
        self.uni = uni
        self._build()

    def _build(self):
        # Left: lists, Right: controls
        left = tk.Frame(self)
        left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=6, pady=6)

        right = tk.Frame(self, width=220)
        right.pack(side=tk.RIGHT, fill=tk.Y, padx=6, pady=6)

        # Faculty Tree
        tk.Label(left, text="Faculty", font=(None, 12, "bold")).pack(anchor='w')
        self.fac_tree = ttk.Treeview(left, columns=("#1", "#2"), show='headings', height=6)
        self.fac_tree.heading('#1', text='Name')
        self.fac_tree.heading('#2', text='Subject')
        self.fac_tree.pack(fill=tk.X)

        # Courses Tree
        tk.Label(left, text="Courses", font=(None, 12, "bold")).pack(anchor='w', pady=(8,0))
        self.course_tree = ttk.Treeview(left, columns=("#1", "#2"), show='headings', height=4)
        self.course_tree.heading('#1', text='Course')
        self.course_tree.heading('#2', text='Code')
        self.course_tree.pack(fill=tk.X)

        # Students Tree
        tk.Label(left, text="Students", font=(None, 12, "bold")).pack(anchor='w', pady=(8,0))
        self.stu_tree = ttk.Treeview(left, columns=("#1", "#2", "#3"), show='headings')
        self.stu_tree.heading('#1', text='Name')
        self.stu_tree.heading('#2', text='ID')
        self.stu_tree.heading('#3', text='Course')
        self.stu_tree.pack(fill=tk.BOTH, expand=True)

        # Right-side controls
        btn_add_fac = tk.Button(right, text="Add Faculty", command=self.add_faculty)
        btn_add_fac.pack(fill=tk.X, pady=4)
        btn_del_fac = tk.Button(right, text="Delete Faculty", command=self.delete_faculty)
        btn_del_fac.pack(fill=tk.X, pady=4)

        btn_add_course = tk.Button(right, text="Add Course", command=self.add_course)
        btn_add_course.pack(fill=tk.X, pady=4)
        btn_del_course = tk.Button(right, text="Delete Course", command=self.delete_course)
        btn_del_course.pack(fill=tk.X, pady=4)

        btn_add_student = tk.Button(right, text="Add Student", command=self.add_student)
        btn_add_student.pack(fill=tk.X, pady=4)
        btn_del_student = tk.Button(right, text="Delete Student", command=self.delete_student)
        btn_del_student.pack(fill=tk.X, pady=4)

        btn_assign = tk.Button(right, text="Assign Course -> Faculty", command=self.assign_course_to_faculty)
        btn_assign.pack(fill=tk.X, pady=8)

        self.refresh()

    def refresh(self):
        # Faculty
        for r in self.fac_tree.get_children():
            self.fac_tree.delete(r)
        for f in self.dep.faculty_members:
            self.fac_tree.insert('', 'end', values=(f.name, f.subject))
        # Courses
        for r in self.course_tree.get_children():
            self.course_tree.delete(r)
        for c in self.dep.courses:
            self.course_tree.insert('', 'end', values=(c.course_name, c.course_code))
        # Students
        for r in self.stu_tree.get_children():
            self.stu_tree.delete(r)
        for s in self.dep.students:
            self.stu_tree.insert('', 'end', values=(s.name, s.id_no, s.course))

    def add_faculty(self):
        name = simpledialog.askstring("Faculty Name", "Name:")
        if not name:
            return
        id_no = simpledialog.askstring("ID", "ID:")
        subject = simpledialog.askstring("Subject", "Subject:")
        salary = simpledialog.askinteger("Salary", "Salary:")
        f = Faculty(name, id_no, subject, salary or 0)
        self.dep.faculty_members.append(f)
        save_data(self.uni)
        self.refresh()

    def delete_faculty(self):
        sel = self.fac_tree.selection()
        if not sel:
            messagebox.showwarning("Select","Select a faculty to delete")
            return
        name = self.fac_tree.item(sel[0])['values'][0]
        f = next((x for x in self.dep.faculty_members if x.name == name), None)
        if f and messagebox.askyesno("Confirm","Delete faculty %s?"%f.name):
            self.dep.faculty_members.remove(f)
            save_data(self.uni)
            self.refresh()

    def add_course(self):
        cname = simpledialog.askstring("Course Name","Name:")
        if not cname:
            return
        code = simpledialog.askstring("Course Code","Code:")
        c = Course(cname, code or "")
        self.dep.courses.append(c)
        save_data(self.uni)
        self.refresh()

    def delete_course(self):
        sel = self.course_tree.selection()
        if not sel:
            messagebox.showwarning("Select","Select a course to delete")
            return
        cname = self.course_tree.item(sel[0])['values'][0]
        c = next((x for x in self.dep.courses if x.course_name == cname), None)
        if c and messagebox.askyesno("Confirm","Delete course %s?"%c.course_name):
            self.dep.courses.remove(c)
            # Also remove from faculties
            for f in self.dep.faculty_members:
                f.courses = [cc for cc in f.courses if cc.course_name != c.course_name]
            save_data(self.uni)
            self.refresh()

    def add_student(self):
        name = simpledialog.askstring("Student Name","Name:")
        if not name:
            return
        id_no = simpledialog.askstring("ID","ID:")
        course = simpledialog.askstring("Course","Course:")
        fees = simpledialog.askinteger("Fees","Fees:")
        s = Student(name, id_no, course or "", fees or 0)
        self.dep.students.append(s)
        save_data(self.uni)
        self.refresh()

    def delete_student(self):
        sel = self.stu_tree.selection()
        if not sel:
            messagebox.showwarning("Select","Select a student to delete")
            return
        name = self.stu_tree.item(sel[0])['values'][0]
        s = next((x for x in self.dep.students if x.name == name), None)
        if s and messagebox.askyesno("Confirm","Delete student %s?"%s.name):
            self.dep.students.remove(s)
            save_data(self.uni)
            self.refresh()

    def assign_course_to_faculty(self):
        # select course
        sel_course = self.course_tree.selection()
        sel_fac = self.fac_tree.selection()
        if not sel_course or not sel_fac:
            messagebox.showwarning("Select","Select both course and faculty")
            return
        cname = self.course_tree.item(sel_course[0])['values'][0]
        fname = self.fac_tree.item(sel_fac[0])['values'][0]
        course = next((x for x in self.dep.courses if x.course_name == cname), None)
        fac = next((x for x in self.dep.faculty_members if x.name == fname), None)
        if course and fac:
            fac.assign_course(course)
            save_data(self.uni)
            self.refresh()
            messagebox.showinfo("Assigned", f"Assigned {course.course_name} to {fac.name}")


# -----------------------------
# Students Frame (overview and quick actions)
# -----------------------------
class StudentsFrame(tk.Frame):
    def __init__(self, parent, controller: UniversityApp):
        super().__init__(parent)
        self.controller = controller
        self._build()

    def _build(self):
        top = tk.Frame(self)
        top.pack(fill=tk.X)
        tk.Label(top, text="Students", font=(None, 14, "bold")).pack(side=tk.LEFT, padx=8)
        btn_add = tk.Button(top, text="Add Student", command=self.add_student)
        btn_add.pack(side=tk.RIGHT, padx=8)

        cols = ("Name", "ID", "Course", "Department")
        self.tree = ttk.Treeview(self, columns=cols, show='headings')
        for c in cols:
            self.tree.heading(c, text=c)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

        self.tree.bind('<Double-1>', self.on_double)

    def refresh(self):
        for r in self.tree.get_children():
            self.tree.delete(r)
        for d in self.controller.uni.departments:
            for s in d.students:
                self.tree.insert('', 'end', values=(s.name, s.id_no, s.course, d.dept_name))

    def add_student(self):
        # choose department first
        if not self.controller.uni.departments:
            messagebox.showwarning("No departments", "Add a department first.")
            return
        dep_names = [d.dept_name for d in self.controller.uni.departments]
        sel = simpledialog.askstring("Department", f"Enter Department (one of: {', '.join(dep_names)}):")
        if not sel:
            return
        dep = next((x for x in self.controller.uni.departments if x.dept_name == sel), None)
        if not dep:
            messagebox.showerror("Invalid","No such department")
            return
        name = simpledialog.askstring("Student Name","Name:")
        id_no = simpledialog.askstring("ID","ID:")
        course = simpledialog.askstring("Course","Course:")
        fees = simpledialog.askinteger("Fees","Fees:")
        s = Student(name, id_no, course or "", fees or 0)
        dep.students.append(s)
        save_data(self.controller.uni)
        self.refresh()

    def on_double(self, event):
        sel = self.tree.selection()
        if not sel:
            return
        vals = self.tree.item(sel[0])['values']
        name, id_no, course, dept_name = vals
        # Show student details and offer pay fees
        resp = messagebox.askquestion("Student", f"Pay fees for {name}? (Yes to pay)")
        if resp == 'yes':
            amount = simpledialog.askinteger("Amount","Enter amount to pay:")
            if amount:
                dep = next((x for x in self.controller.uni.departments if x.dept_name == dept_name), None)
                stu = next((x for x in dep.students if x.id_no == id_no), None)
                if stu:
                    if amount <= stu._fees:
                        stu._fees -= amount
                        save_data(self.controller.uni)
                        messagebox.showinfo("Paid", f"{amount} paid. Remaining: {stu._fees}")
                        self.refresh()
                    else:
                        messagebox.showerror("Error","Amount greater than pending fees")


# -----------------------------
# Faculty Frame
# -----------------------------
class FacultyFrame(tk.Frame):
    def __init__(self, parent, controller: UniversityApp):
        super().__init__(parent)
        self.controller = controller
        self._build()

    def _build(self):
        top = tk.Frame(self)
        top.pack(fill=tk.X)
        tk.Label(top, text="Faculty", font=(None, 14, "bold")).pack(side=tk.LEFT, padx=8)
        btn_add = tk.Button(top, text="Add Faculty", command=self.add_faculty)
        btn_add.pack(side=tk.RIGHT, padx=8)

        cols = ("Name", "ID", "Subject", "Department")
        self.tree = ttk.Treeview(self, columns=cols, show='headings')
        for c in cols:
            self.tree.heading(c, text=c)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

    def refresh(self):
        for r in self.tree.get_children():
            self.tree.delete(r)
        for d in self.controller.uni.departments:
            for f in d.faculty_members:
                self.tree.insert('', 'end', values=(f.name, f.id_no, f.subject, d.dept_name))

    def add_faculty(self):
        if not self.controller.uni.departments:
            messagebox.showwarning("No departments", "Add a department first.")
            return
        dep_names = [d.dept_name for d in self.controller.uni.departments]
        sel = simpledialog.askstring("Department", f"Enter Department (one of: {', '.join(dep_names)}):")
        if not sel:
            return
        dep = next((x for x in self.controller.uni.departments if x.dept_name == sel), None)
        if not dep:
            messagebox.showerror("Invalid","No such department")
            return

        name = simpledialog.askstring("Faculty Name","Name:")
        id_no = simpledialog.askstring("ID","ID:")
        subject = simpledialog.askstring("Subject","Subject:")
        salary = simpledialog.askinteger("Salary","Salary:")
        f = Faculty(name, id_no, subject or "", salary or 0)
        dep.faculty_members.append(f)
        save_data(self.controller.uni)
        self.refresh()


# -----------------------------
# Courses Frame
# -----------------------------
class CoursesFrame(tk.Frame):
    def __init__(self, parent, controller: UniversityApp):
        super().__init__(parent)
        self.controller = controller
        self._build()

    def _build(self):
        top = tk.Frame(self)
        top.pack(fill=tk.X)
        tk.Label(top, text="Courses", font=(None, 14, "bold")).pack(side=tk.LEFT, padx=8)
        btn_add = tk.Button(top, text="Add Course", command=self.add_course)
        btn_add.pack(side=tk.RIGHT, padx=8)

        cols = ("Course", "Code", "Department")
        self.tree = ttk.Treeview(self, columns=cols, show='headings')
        for c in cols:
            self.tree.heading(c, text=c)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

    def refresh(self):
        for r in self.tree.get_children():
            self.tree.delete(r)
        for d in self.controller.uni.departments:
            for c in d.courses:
                self.tree.insert('', 'end', values=(c.course_name, c.course_code, d.dept_name))

    def add_course(self):
        if not self.controller.uni.departments:
            messagebox.showwarning("No departments", "Add a department first.")
            return
        dep_names = [d.dept_name for d in self.controller.uni.departments]
        sel = simpledialog.askstring("Department", f"Enter Department (one of: {', '.join(dep_names)}):")
        if not sel:
            return
        dep = next((x for x in self.controller.uni.departments if x.dept_name == sel), None)
        if not dep:
            messagebox.showerror("Invalid","No such department")
            return
        cname = simpledialog.askstring("Course Name","Name:")
        code = simpledialog.askstring("Course Code","Code:")
        c = Course(cname or "", code or "")
        dep.courses.append(c)
        save_data(self.controller.uni)
        self.refresh()


# -----------------------------
# Run application
# -----------------------------

def main():
    uni = load_data()
    app = UniversityApp(uni)
    app.protocol("WM_DELETE_WINDOW", app.on_close)
    app.mainloop()


if __name__ == '__main__':
    main()
