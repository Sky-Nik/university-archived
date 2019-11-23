import datetime as dt
from sqlalchemy.exc import IntegrityError
from _class import Base, University, PrivateUniversity, PublicUniversity, UniversityFaculty, \
	UniversityFacultySpecialization, UniversityFacultySpecializationGroup, \
	UniversityRector, UniversityProfessor, UniversityAssociateProfessor, \
	UniversityAssistantProfessor, UniversityStudent, UniversitySubject, UniversitySchedule
import sys


def read_university(session):
	name = input("\nEnter the name of university to read: ")

	country = input("\nEnter the country of university to read: ")

	try:
		university = session.query(University) \
			.filter(University.name == name) \
			.filter(University.country == country).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return
	
	faculty_names = ',\n\t\t'.join(list(map(lambda _: _.name, university.faculties)))

	professor_names = ',\n\t\t'.join(list(map(lambda _: _.name, university.professors)))

	print(
		f'Univeristy {university.name} found in {university.city}, {university.country}.\n'
		f'\tEstablished on {university.established}.\n'
		f'\tHas endowment of {university.endowment}.\n'
		f'\tLocated on {university.address}.\n'
		f'\tCurrent rector is {university.rector}.\n'
		f'\tHas faculties: \n'
		f'\t\t{faculty_names}.\n'
		f'\tHas professors: \n'
		f'\t\t{professor_names}.\n'
	)


def read_faculty(session):
	university_name = input("\nEnter the name of university to read faculty of: ")

	university_country = input("\nEnter the country of university to read faculty of: ")

	try:
		university = session.query(University) \
			.filter(University.name == university_name) \
			.filter(University.country == university_country).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

	name = input("\nEnter the name of faculty to read: ")

	try:
		faculty = session.query(UniversityFaculty) \
			.filter(UniversityFaculty.university == university) \
			.filter(UniversityFaculty.name == name).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

	specialization_names = ',\n\t\t'.join(list(map(lambda _: _.name, \
		faculty.specializations)))

	print(
		f'Faculty {faculty.name} of university {university} found.\n'
		f'\tLocated on {faculty.address}.\n'
		f'\tHas specializations: \n'
		f'\t\t{specialization_names}.\n'
	)


def read_specialization(session):
	university_name = input("\nEnter the name of university to read specialization of: ")

	university_country = input(
		"\nEnter the country of university to read specialization of: ")

	try:
		university = session.query(University) \
			.filter(University.name == university_name) \
			.filter(University.country == university_country).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

	faculty_name = input("\nEnter the name of faculty to read specialization of: ")

	try:
		faculty = session.query(UniversityFaculty) \
			.filter(UniversityFaculty.university == university) \
			.filter(UniversityFaculty.name == faculty_name).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

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


def read_group(session):
	university_name = input("\nEnter the name of university to read group of: ")

	university_country = input(
		"\nEnter the country of university to read group of: ")

	try:
		university = session.query(University) \
			.filter(University.name == university_name) \
			.filter(University.country == university_country).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

	faculty_name = input("\nEnter the name of faculty to read group of: ")

	try:
		faculty = session.query(UniversityFaculty) \
			.filter(UniversityFaculty.university == university) \
			.filter(UniversityFaculty.name == faculty_name).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

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


def read_professor(session):
	university_name = input("\nEnter the name of university to read professor of: ")

	university_country = input("\nEnter the country of university to read professor of: ")

	try:
		university = session.query(University) \
			.filter(University.name == university_name) \
			.filter(University.country == university_country).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

	passport = input("\nEnter passport of professor to read: ")

	try:
		professor = session.query(UniversityProfessor) \
			.filter(UniversityProfessor.passport == passport).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

	print(
		f'Professor {professor.name} from university {university} found.\n'
		f'\tFullname is {professor.fullname}.\n'
		f'\tPassport is {professor.passport}.\n'
		f'\tBirth date is {professor.birth_date}.\n'
		f'\tIn office from {professor.in_office_from}.\n'
		f'\tIn office to {professor.in_office_to}.\n'
		f'\tAcademic degree: {professor.academic_degree}.\n'
	)


def read_rector(session):
	university_name = input("\nEnter the name of university to read rector of: ")

	university_country = input("\nEnter the country of university to read rector of: ")

	try:
		university = session.query(University) \
			.filter(University.name == university_name) \
			.filter(University.country == university_country).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

	passport = input("\nEnter passport of rector to read: ")

	try:
		rector = session.query(UniversityRector) \
			.filter(UniversityRector.passport == passport).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

	print(
		f'Rector {rector.name} from university {university} found.\n'
		f'\tFullname is {rector.fullname}.\n'
		f'\tPassport is {rector.passport}.\n'
		f'\tBirth date is {rector.birth_date}.\n'
		f'\tIn office from {rector.in_office_from}.\n'
		f'\tIn office to {rector.in_office_to}.\n'
	)


def read_student(session):
	university_name = input("\nEnter the name of university to read student of: ")

	university_country = input(
		"\nEnter the country of university to read student of: ")

	try:
		university = session.query(University) \
			.filter(University.name == university_name) \
			.filter(University.country == university_country).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

	faculty_name = input("\nEnter the name of faculty to read student of: ")

	try:
		faculty = session.query(UniversityFaculty) \
			.filter(UniversityFaculty.university == university) \
			.filter(UniversityFaculty.name == faculty_name).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return

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


def read_subject(session):
	name = input("\nEnter the name of subject to read: ")

	try:
		subject = session.query(UniversitySubject) \
			.filter(UniversitySubject.name == name).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return
	
	print(f'Subject {subject.name} found.\n')
