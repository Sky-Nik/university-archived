import datetime as dt
from sqlalchemy.exc import IntegrityError
from _class import University, PrivateUniversity, PublicUniversity, UniversityFaculty, \
	UniversityFacultySpecialization, UniversityFacultySpecializationGroup, \
	UniversityRector, UniversityProfessor, UniversityAssociateProfessor, \
	UniversityAssistantProfessor, UniversityStudent, UniversitySubject, UniversitySchedule
import sys


def read(session, faculty):
	specialization_names = ',\n\t\t'.join(list(map(lambda _: _.name, \
		faculty.specializations)))

	print(
		f'Faculty {faculty.name} of university {university} found.\n'
		f'\tLocated on {faculty.address}.\n'
		f'\tHas specializations: \n'
		f'\t\t{specialization_names}.\n'
	)


def read_specialization(session, faculty):
	name = input("\nEnter the name of specialization to read: ")

	try:
		specialization = session.query(UniversityFacultySpecialization) \
			.filter(UniversityFacultySpecialization.faculty == faculty) \
			.filter(UniversityFacultySpecialization.name == name).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

	group_names = ',\n\t\t'.join(list(map(lambda _: _.name, specialization.groups)))

	print(
		f'Specialization {specialization.name} of faculty {faculty} found.\n'
		f'\tHas groups: \n'
		f'\t\t{group_names}.\n'
	)


def read_group(session, faculty):
	specialization_name = input("\nEnter the name of specialization to read group of: ")

	try:
		specialization = session.query(UniversityFacultySpecialization) \
			.filter(UniversityFacultySpecialization.faculty == faculty) \
			.filter(UniversityFacultySpecialization.name == specialization_name).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

	name = input("\nEnter the name of group to read: ")

	try:
		group = session.query(UniversityFacultySpecializationGroup) \
			.filter(UniversityFacultySpecializationGroup.specialization == specialization) \
			.filter(UniversityFacultySpecializationGroup.name == name).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

	student_names = ',\n\t\t'.join(list(map(lambda _: _.name, group.students)))

	print(
		f'Group {group.name} of specialization {specialization} found.\n'
		f'\tCourse is {group.course}.\n'
		f'\tDepartment is {group.department}.\n'
		f'\tHas students: \n'
		f'\t\t{student_names}.\n'
	)


def read_student(session, faculty):
	specialization_name = input("\nEnter the name of specialization to read student of: ")

	try:
		specialization = session.query(UniversityFacultySpecialization) \
			.filter(UniversityFacultySpecialization.faculty == faculty) \
			.filter(UniversityFacultySpecialization.name == specialization_name).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

	group_name = input("\nEnter the name of group to read student of: ")

	try:
		group = session.query(UniversityFacultySpecializationGroup) \
			.filter(UniversityFacultySpecializationGroup.specialization == specialization) \
			.filter(UniversityFacultySpecializationGroup.name == group_name).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

	passport = input("\nEnter passport of student to read: ")

	try:
		student = session.query(UniversityStudent) \
			.filter(UniversityStudent.passport == passport).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

	print(
		f'Student {student.name} from group {group} found.\n'
		f'\tFullname is {student.fullname}.\n'
		f'\tPassport is {student.passport}.\n'
		f'\tBirth date is {student.birth_date}.\n'
		f'\tEntrance date is {student.entrance_date}.\n'
		f'\tGraduation date id {student.graduation_date}.\n'
	)
