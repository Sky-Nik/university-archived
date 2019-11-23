import os
import sys
import datetime as dt
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from _class import University, PrivateUniversity, PublicUniversity, UniversityFaculty, \
	UniversityFacultySpecialization, UniversityFacultySpecializationGroup, \
	UniversityRector, UniversityProfessor, UniversityAssociateProfessor, \
	UniversityAssistantProfessor, UniversityStudent, UniversitySubject, UniversitySchedule
from university_create import create_faculty, create_specialization, create_group, \
	create_rector, create_professor, create_student
from university_update import update, update_faculty, update_group, update_rector, \
	update_professor, update_student
from university_read import read, read_faculty, read_specialization, read_group, \
	read_rector, read_professor, read_student
from university_delete import delete, delete_faculty, delete_specialization, delete_group, \
	delete_rector, delete_professor, delete_student
from faculty_driver import faculty_menu


def university_menu(session):
	university_cmd = {
		'create_faculty': create_faculty, 
		'create_specialization': create_specialization, 
		'create_group': create_group,
		'create_rector': create_rector, 
		'create_professor': create_professor, 
		'create_student': create_student,

		'update': update, 
		'update_faculty': update_faculty, 
		'update_group': update_group, 
		'update_rector': update_rector,
		'update_professor': update_professor,
		'update_student': update_student,

		'read': read, 
		'read_faculty': read_faculty, 
		'read_specialization': read_specialization, 
		'read_group': read_group,
		'read_rector': read_rector,
		'read_professor': read_professor,
		'read_student': read_student,

		'delete': delete, 
		'delete_faculty': delete_faculty, 
		'delete_specialization': delete_specialization, 
		'delete_group': delete_group,
		'delete_rector': delete_rector,
		'delete_professor': delete_professor,
		'delete_student': delete_student,

		'faculty_menu': faculty_menu,
	}

	def university_cls(session, university):
		os.system('cls')

	university_cmd['\x0c'] = university_cmd['cls'] = university_cmd['clear'] = university_cls

	def university_help(session, university):
		print('Possible commands:\n\t', '\n\t'.join(university_cmd.keys()), sep='')

	university_cmd['h'] = university_cmd['H'] = university_cmd['help'] = \
		university_cmd['Help'] = university_cmd['HELP'] = university_help

	def university_exit(session, university):
		return 1

	university_cmd['back'] = university_cmd['exit'] = university_exit

	name = input("\nEnter the name of university to enter the menu of: ")

	country = input("\nEnter the country of university to enter the menu of: ")

	try:
		university = session.query(University) \
			.filter(University.name == name) \
			.filter(University.country == country).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return
	
	while True:
		if university_cmd[input("\nEnter the command: ")](session, university):
			return
