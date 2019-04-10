import re
message='''Hello my name is vaibhav i am vaibhav my real name is also vaibhav my friends call me vaibhav'''
pattern=re.compile(r'vaibhav')
message=pattern.sub('Banarasi',message)
print(message)
