# 10-10. Common Words

with open('sample_content.txt') as f:
    sample_content = f.read()

print(f"The no. of time 'the' has occured in the txt file is {sample_content.lower().count('the')}.")

print(f"The no. of time 'the ' has occured in the txt file is {sample_content.lower().count('the ')}.")