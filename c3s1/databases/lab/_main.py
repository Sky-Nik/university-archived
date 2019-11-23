import sys
import datetime as dt
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from _class import Base, University, PrivateUniversity, PublicUniversity, UniversityRector, \
	UniversityProfessor, UniversityAssistantProfessor, UniversityStudent, \
	UniversityFaculty, UniversityFacultySpecialization,	UniversityFacultySpecializationGroup

engine = create_engine('sqlite:///:memory:')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

KNU = PublicUniversity(name='Taras Shevchenko National University of Kyiv',
	motto='Utilitas honor et gloria', country='Ukraine', city='Kyiv',
	established=dt.date(year=1834, month=11, day=8))

session.add(KNU)

Hubersky = UniversityRector(passport=1, name='Leonid', 
	fullname="Leonid Vasyl'ovych Hubersky",
	birth_date=dt.date(year=1941, month=10, day=4), 
	in_office_from=dt.date(year=2015, month=10, day=20), university=KNU)

KNU.rector = Hubersky

session.add(Hubersky)

session.commit()

for univ in session.query(University):
	print(univ, univ.rector)

Klyushyn = UniversityProfessor(passport=2, name='Dmytro', 
	fullname='Dmytro Anatoliyovych Klyushyn', 
	birth_date=dt.date(year=1963, month=9, day=19), 
	in_office_from=dt.date(year=2011, month=9, day=1), university=KNU)

session.add(Klyushyn)

Nomirovsky = UniversityProfessor(passport=3, name='Dmytro',
	fullname='Dmytro Anatoliyovych Nomirovsky',
	birth_date=dt.date(year=1974, month=12, day=25),
	in_office_from=dt.date(year=2008, month=9, day=1), university=KNU)

for univ in session.query(University):
	print(f'{univ}:')
	for prof in univ.professors:
		print(f'\t{prof}')

KPI = PublicUniversity(name='Igor Sikorsky Kyiv Polytechnic Institute', motto=None, 
	country='Ukraine', city='Kyiv', established=dt.date(year=1896, month=11, day=25))

session.add(KPI)

Zghurovskyi = UniversityRector(name='Mykhailo', fullname='Mykhailo Zakharovych Zghurovskyi',
	birth_date=dt.date(year=1950, month=1, day=30),
	in_office_from=dt.date(year=1992, month=9, day=1), university=KPI)

session.add(Zghurovskyi)

session.commit()

for univ in session.query(University):
	print(univ, univ.rector)

Onotskyi = UniversityAssistantProfessor(name="V'yacheslav",
	fullname="V'ycheslav Valeriyovych Onotskyi", birth_date=dt.date(1978, 1, 1),
	in_office_from=dt.date(1999, 1, 1), university=KNU)

session.add(Onotskyi)

session.commit()

for univ in session.query(University):
	print(f'{univ}:')
	for prof in univ.professors:
		print(f'\t{prof}, type = {prof.type}')

for univ in session.query(University):
	print(f'{univ}:')
	for prof in univ.professors.filter(text("type = 'Assistant Professor'")):
		print(f'\t{prof}')

csc = UniversityFaculty(name='Faculty of Computer Science and Cybernetics', university=KNU)

applmath_csc = UniversityFacultySpecialization(name='Applied Mathematics', faculty=csc)

k21 = UniversityFacultySpecializationGroup(name='K21', specialization=applmath_csc, course=2)

om3 = UniversityFacultySpecializationGroup(name='OM3', specialization=applmath_csc, course=3,
	department='Computational Mathematics')

inf = UniversityFacultySpecialization(name='Informatics', faculty=csc)

mm = UniversityFaculty(name='Mechanics and Mathematics Faculty', university=KNU)

applmath_mm = UniversityFacultySpecialization(name='Applied Mathematics', faculty=mm)

math = UniversityFacultySpecialization(name='Mathematics', faculty=mm)

mech = UniversityFacultySpecialization(name='Mechanics', faculty=mm)

session.add_all([csc, applmath_csc, k21, om3, inf, mm, applmath_mm, math, mech])

session.commit()

for univ in session.query(University):
	print(f'{univ}:')
	for stud in univ.students:
		print(f'\t{stud}')

