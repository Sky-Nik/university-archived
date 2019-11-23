import datetime as dt
from sqlalchemy.exc import IntegrityError
from _class import University, PrivateUniversity, PublicUniversity, UniversityFaculty, \
	UniversityFacultySpecialization, UniversityFacultySpecializationGroup, \
	UniversityRector, UniversityProfessor, UniversityAssociateProfessor, \
	UniversityAssistantProfessor, UniversityStudent, UniversitySubject, UniversitySchedule
import sys


def safe_commit(session, faculty):
	try:
		session.commit()

		print(f'\nSuccessful commit.\n')
	except IntegrityError:
		print(f'\n{sys.exc_info()}\n')

		session.rollback()


def create_specialization(session, faculty):
	name = input("\nEnter the name of new specialization: ")

	session.add(UniversityFacultySpecialization(name=name, faculty=faculty))

	safe_commit(session, faculty)


def create_group(session, faculty):
	specialization_name = input("\nEnter the name of specialization to add group to: ")

	try:
		specialization = session.query(UniversityFacultySpecialization) \
			.filter(UniversityFacultySpecialization.faculty == faculty) \
			.filter(UniversityFacultySpecialization.name == specialization_name)
	except:
		print(f'\n{sys.exc_info()}\n')
		return

	name = input("\nEnter the name of new group: ")
	course = input("\nEnter the course of new group: ")
	if course >= '3':
		department = input("\nEnter the department of new group: ")

	session.add(name=name, course=course, department=department, 
		specialization=specialization)

	safe_commit(session, faculty)


def create_student(session, faculty):
	specialization_name = input("\nEnter the name of specialization to add student to: ")

	try:
		specialization = session.query(UniversityFacultySpecialization) \
			.filter(UniversityFacultySpecialization.faculty == faculty) \
			.filter(UniversityFacultySpecialization.name == specialization_name)
	except:
		print(f'\n{sys.exc_info()}\n')
		return

	group_name = input("\nEnter the name of group to add student to: ")

	try:
		group = session.query(UniversityFacultySpecializationGroup) \
			.filter(UniversityFacultySpecializationGroup.specialization == specialization) \
			.filter(UniversityFacultySpecializationGroup.name == group_name)
	except:
		print(f'\n{sys.exc_info()}\n')
		return	

	name = input("\nEnter the name of new student: ")
	fullname = input("\nEnter the fullname of new student: ")
	birth_date = dt.datetime.strptime(input(
		"\nEnter the birth date date in yyyy-mm-dd format: "), '%Y-%m-%d')

	is_new = input("\nIs the student new? [Y/n]: ")
	if is_new == 'Y':
		entrance_date = dt.datetime.today()
	else:
		entrance_date = dt.datetime.strptime(input(
			"\n\tEnter the entrance date in yyyy-mm-dd format: "), '%Y-%m-%d')

	session.add(UniversityStudent(name=name, fullname=fullname, birth_date=birth_date,
		entrance_date=entrance_date, group=group))

	safe_commit(session, faculty)
