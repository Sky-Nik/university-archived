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


def update(session, faculty):
	update_name = input("\nDo you want to update name? [Y/n]: ")
	if update_name == 'Y':
		faculty.name = input("\n\tEnter new name: ")

	update_address = input("\nDo you want to update address? [Y/n]: ")
	if update_address == 'Y':
		faculty.address = input("\nEnter new address: ")

	safe_commit(session, faculty)


def update_group(session, faculty):
	specialization_name = input("\nEnter the name of specialization to update group of: ")

	try:
		specialization = session.query(UniversityFacultySpecialization) \
			.filter(UniversityFacultySpecialization.faculty == faculty) \
			.filter(UniversityFacultySpecialization.name == specialization_name).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

	name = input("\nEnter the name of group to update: ")

	try:
		group = session.query(UniversityFacultySpecializationGroup) \
			.filter(UniversityFacultySpecializationGroup.specialization == specialization) \
			.filter(UniversityFacultySpecializationGroup.name == name).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

	update_name = input("\nDo you want to update name? [Y/n]: ")
	if update_name == 'Y':
		group.name = input("\n\tEnter new name: ")

	update_course = input("\nDo you want to update course? [Y/n]: ")
	if update_course == 'Y':
		group.course = input("\nEnter new course: ")
	
	update_department = input("\nDo you want to update department? [Y/n]: ")
	if update_department == 'Y':
		group.department = input("\nEnter new department: ")
	
	safe_commit(session, faculty)


def update_student(session, faculty):
	specialization_name = input("\nEnter the name of specialization to update student of: ")

	try:
		specialization = session.query(UniversityFacultySpecialization) \
			.filter(UniversityFacultySpecialization.faculty == faculty) \
			.filter(UniversityFacultySpecialization.name == specialization_name).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

	group_name = input("\nEnter the name of group to update student of: ")

	try:
		group = session.query(UniversityFacultySpecializationGroup) \
			.filter(UniversityFacultySpecializationGroup.specialization == specialization) \
			.filter(UniversityFacultySpecializationGroup.name == group_name).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

	passport = input("\nEnter passport of student to update: ")

	try:
		student = session.query(UniversityStudent) \
			.filter(UniversityStudent.passport == passport).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

	update_passport = input("\nDo you want to update passport? [Y/n]: ")
	if update_passport == 'Y':
		student.passport = input("\n\tEnter new passport: ")

	update_name = input("\nDo you want to update name? [Y/n]: ")
	if update_name == 'Y':
		student.name = input("\nEnter new name: ")
	
	update_fullname = input("\nDo you want to update fullname? [Y/n]: ")
	if update_fullname == 'Y':
		student.fullname = input("\nEnter new fullname: ")
	
	update_academic_degree = input("\nDo you want to update academic degree? [Y/n]: ")
	if update_academic_degree == 'Y':
		student.academic_degree = input("\nEnter new academic degree: ")

	safe_commit(session, faculty)
