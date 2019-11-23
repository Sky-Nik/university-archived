import sys
import datetime as dt
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from _class import Base, University, PrivateUniversity, PublicUniversity, UniversityRector, \
	UniversityProfessor, UniversityAssistantProfessor, UniversityStudent, \
	UniversityFaculty, UniversityFacultySpecialization,	\
	UniversityFacultySpecializationGroup, UniversitySubject, UniversitySchedule

engine = create_engine('sqlite:///:memory:')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()


# University (PublicUniversity)
KNU = PublicUniversity(name='Taras Shevchenko National University of Kyiv',
	motto='Utilitas honor et gloria', country='Ukraine', city='Kyiv',
	established=dt.date(year=1834, month=11, day=8))

KPI = PublicUniversity(name='Igor Sikorsky Kyiv Polytechnic Institute', motto=None, 
	country='Ukraine', city='Kyiv', established=dt.date(year=1896, month=11, day=25))

session.add_all([KNU, KPI])


# UniversityRector
Hubersky = UniversityRector(passport=1, name='Leonid', 
	fullname="Leonid Vasyl'ovych Hubersky",
	birth_date=dt.date(year=1941, month=10, day=4), 
	in_office_from=dt.date(year=2015, month=10, day=20), university=KNU)

Zghurovskyi = UniversityRector(name='Mykhailo', fullname='Mykhailo Zakharovych Zghurovskyi',
	birth_date=dt.date(year=1950, month=1, day=30),
	in_office_from=dt.date(year=1992, month=9, day=1), university=KPI)

session.add_all([Hubersky, Zghurovskyi])


# UniversityProfessor
Klyushyn = UniversityProfessor(passport=2, name='Dmytro', 
	fullname='Dmytro Anatoliyovych Klyushyn', 
	birth_date=dt.date(year=1963, month=9, day=19), 
	in_office_from=dt.date(year=2011, month=9, day=1), university=KNU)

Nomirovsky = UniversityProfessor(passport=3, name='Dmytro',
	fullname='Dmytro Anatoliyovych Nomirovsky',
	birth_date=dt.date(year=1974, month=12, day=25),
	in_office_from=dt.date(year=2008, month=9, day=1), university=KNU)

Kukush = UniversityProfessor(name='Alexander', fullname='Alexander Kukush',
	birth_date=dt.date(1957, 5, 23), in_office_from=dt.date(1998, 1, 1), university=KNU)

session.add_all([Klyushyn, Nomirovsky, Kukush])

# UniversityProfessor (UniversityAssistantProfessor)
Onotskyi = UniversityAssistantProfessor(name="V'yacheslav",
	fullname="V'ycheslav Valeriyovych Onotskyi", birth_date=dt.date(1978, 1, 1),
	in_office_from=dt.date(1999, 1, 1), university=KNU)

session.add(Onotskyi)


# UniversityFaculty
csc = UniversityFaculty(name='Faculty of Computer Science and Cybernetics', university=KNU)

mm = UniversityFaculty(name='Mechanics and Mathematics Faculty', university=KNU)

session.add_all([csc, mm])


# UniversityFacultySpecialization
applmath_csc = UniversityFacultySpecialization(name='Applied Mathematics', faculty=csc)

inf = UniversityFacultySpecialization(name='Informatics', faculty=csc)

applmath_mm = UniversityFacultySpecialization(name='Applied Mathematics', faculty=mm)

math = UniversityFacultySpecialization(name='Mathematics', faculty=mm)

mech = UniversityFacultySpecialization(name='Mechanics', faculty=mm)

session.add_all([applmath_csc, inf, applmath_mm, math, mech])


# UniversityFacultySpecializationGroup
k22 = UniversityFacultySpecializationGroup(name='K22', specialization=applmath_csc, course=2)

om3 = UniversityFacultySpecializationGroup(name='OM3', specialization=applmath_csc, course=3,
	department='Computational Mathematics')

k15 = UniversityFacultySpecializationGroup(name='K15', specialization=inf, course=1)

session.add_all([k22, om3, k15])


# UniversityStudent
Skybytskyi = UniversityStudent(name='Nikita', fullname='Nikita Maksymovych Skybytskyi',
	birth_date=dt.date(1999, 6, 2), entrance_date=dt.date(2016, 9, 1), group=om3)

Pushkin = UniversityStudent(name='Denis', fullname='Denis Evgenovych Pushkin',
	birth_date=dt.date(1998, 11, 4), entrance_date=dt.date(2016, 9, 1), group=om3)

Antipova = UniversityStudent(name='Alice', fullname='Alice Antipova',
	birth_date=dt.date(1999, 11, 23), entrance_date=dt.date(2016, 9, 1), group=om3)

Banders = UniversityStudent(name='Mariia', fullname='Banders Mariia',
	birth_date=dt.date(2000, 5, 26), entrance_date=dt.date(2017, 9, 1), group=k22)

Zarina = UniversityStudent(name='Zarina', fullname='Zarina Kodyrova',
	birth_date=dt.date(2000, 4, 10), entrance_date=dt.date(2017, 9, 1), group=k22)

session.add_all([Skybytskyi, Pushkin, Antipova, Banders, Zarina])


# UniversitySubject
matan = UniversitySubject(name='mathematical analysis')

numan = UniversitySubject(name='numerical analysis')

complan = UniversitySubject(name='complex analysis')

sysprog = UniversitySubject(name='system programming')

session.add_all([matan, numan, complan, sysprog])


# UniversitySchedule
pair1 = UniversitySchedule(subject=matan, group=k22, professor=Nomirovsky, audience=42, 
	weekday='Wednesday', pair_number=2)

pair2 = UniversitySchedule(subject=matan, group=k22, professor=Nomirovsky, audience=42, 
	weekday='Friday', pair_number=1)

pair3 = UniversitySchedule(subject=complan, group=om3, professor=Onotskyi, audience=1,
	weekday='Thursday', pair_number=2)

pair4 = UniversitySchedule(subject=complan, group=om3, professor=Onotskyi, audience=1,
	weekday='Friday', pair_number=4)

session.add_all([pair1, pair2, pair3, pair4])


session.commit()

print('Session:\n')
for obj in session:
	print(f'\tObject {obj} of type {type(obj)};\n')
