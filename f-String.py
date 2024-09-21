# info="My name is  {1} and my branch is  {0}"
name="Sagar Suryakant Waghmare"
branch="Computer Science and Engginering"
# print(info.format(branch,name))
# We can simply use the f-string for this
print(f"Hey my name is {name} and my branch is {branch}")
print(f"We use the f-string like this Hey my name is {{name}} and my branch is {{branch}}")
# String formating in the python
# by the simple method
txt="Fot only {price:.2f} dollars!"
print(txt.format(price=49.09999))
#by the f-string method
price=49.09999
txt=f"For only {price:.2f} dollars!"
print(txt)
print(f"{2*60}")
print(type(f"{2*60}"))
print("thank you")