for i in range(1,11):
    if (i==5):
        continue

    else:
     print(i)

for i in range(1,21):
    if i%2==0:
        continue

    else:
     print(i)
for i in range(1,5):
    if i==3:
     print(f'Skipping Testcase {i}')
    else:
       print(f'Running Testcase {i}')