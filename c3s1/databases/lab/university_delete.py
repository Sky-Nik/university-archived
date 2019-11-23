import sys
import datetime as dt
from sqlalchemy.exc import IntegrityError
from _class import University, PrivateUniversity, PublicUniversity, UniversityFaculty, \
	UniversityFacultySpecialization, UniversityFacultySpecializationGroup, \
	UniversityRector, UniversityProfessor, UniversityAssociateProfessor, \
	UniversityAssistantProfessor, UniversityStudent, UniversitySubject, UniversitySchedule
import sys


def safe_commit(session, university):
	try:
		session.commit()

		print(f'\nSuccessful commit.\n')
	except IntegrityError:
		print(f'\n{sys.exc_info()}\n')

		session.rollback()


def delete(session, university):
	session.delete(university)

	safe_commit(session, university)

	return 1


def delete_faculty(session, university):
	name = input("\nEnter the name of faculty to delete: ")

	try:
		faculty = session.query(UniversityFaculty) \
			.filter(UniversityFaculty.university == university) \
			.filter(UniversityFaculty.name == name).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

	session.delete(faculty)

	safe_commit(session, university)


def delete_specialization(session, university):
	faculty_name = input("\nEnter the name of faculty to delete specialization of: ")

	try:
		faculty = session.query(UniversityFaculty) \
			.filter(UniversityFaculty.university == university) \
			.filter(UniversityFaculty.name == faculty_name).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

	name = input("\nEnter the name of specialization to delete: ")

	try:
		specialization = session.query(UniversityFacultySpecialization) \
			.filter(UniversityFacultySpecialization.faculty == faculty) \
			.filter(UniversityFacultySpecialization.name == name).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

	session.delete(specialization)

	safe_commit(session, university)


def delete_group(session, university):
	faculty_name = input("\nEnter the name of faculty to delete group of: ")

	try:
		faculty = session.query(UniversityFaculty) \
			.filter(UniversityFaculty.university == university) \
			.filter(UniversityFaculty.name == faculty_name).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

	specialization_name = input("\nEnter the name of specialization to delete group of: ")

	try:
		specialization = session.query(UniversityFacultySpecialization) \
			.filter(UniversityFacultySpecialization.faculty == faculty) \
			.filter(UniversityFacultySpecialization.name == specialization_name).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

	name = input("\nEnter the name of group to delete: ")

	try:
		group = session.query(UniversityFacultySpecializationGroup) \
			.filter(UniversityFacultySpecializationGroup.specialization == specialization) \
			.filter(UniversityFacultySpecializationGroup.name == name).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

	session.delete(group)

	safe_commit(session, university)


def delete_professor(session, university):
	passport = input("\nEnter passport of professor to delete: ")

	try:
		professor = session.query(UniversityProfessor) \
			.filter(UniversityProfessor.passport == passport).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

	session.delete(professor)

	safe_commit(session, university)


def delete_rector(session, university):
	passport = input("\nEnter passport of rector to delete: ")

	try:
		rector = session.query(UniversityRector) \
			.filter(UniversityRector.passport == passport).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

	session.delete(rector)

	safe_commit(session, university)


def delete_student(session, university):
	faculty_name = input("\nEnter the name of faculty to delete student of: ")

	try:
		faculty = session.query(UniversityFaculty) \
			.filter(UniversityFaculty.university == university) \
			.filter(UniversityFaculty.name == faculty_name).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

	specialization_name = input("\nEnter the name of specialization to delete student of: ")

	try:
		specialization = session.query(UniversityFacultySpecialization) \
			.filter(UniversityFacultySpecialization.faculty == faculty) \
			.filter(UniversityFacultySpecialization.name == specialization_name).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

	group_name = input("\nEnter the name of group to delete student of: ")

	try:
		group = session.query(UniversityFacultySpecializationGroup) \
			.filter(UniversityFacultySpecializationGroup.specialization == specialization) \
			.filter(UniversityFacultySpecializationGroup.name == group_name).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

	passport = input("\nEnter passport of student to delete: ")

	try:
		student = session.query(UniversityStudent) \
			.filter(UniversityStudent.passport == passport).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

	session.delete(student)

	safe_commit(session, university)
