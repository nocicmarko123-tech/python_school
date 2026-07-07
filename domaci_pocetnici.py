pacijent = []

for i in range(7):
    temperatura = int(input())
    pacijent.append(temperatura)

razlika = max(pacijent) - min(pacijent)
print(razlika)
print(pacijent[2])