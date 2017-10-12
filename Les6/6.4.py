studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]

def gemiddelde_per_student(studentencijfers):
  resultaat = []
  for student in studentencijfers:
    avg = sum(student)/len(student)
    resultaat.append(avg)
  return resultaat

ResPerStudent = gemiddelde_per_student(studentencijfers)

print('Gemiddelde per student:', ResPerStudent)

def gemiddelde_van_alle_studenten(studentencijfers):
  sgemiddelde = gemiddelde_per_student(studentencijfers)
  savg = sum(sgemiddelde)/len(sgemiddelde)
  return savg

totaal = gemiddelde_van_alle_studenten(studentencijfers)

print('Gemiddelde van alle studenten:', totaal)