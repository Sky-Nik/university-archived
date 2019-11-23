import os
import sys
import datetime as dt
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from _class import University, PrivateUniversity, PublicUniversity, UniversityFaculty, \
	UniversityFacultySpecialization, UniversityFacultySpecializationGroup, \
	UniversityRector, UniversityProfessor, UniversityAssociateProfessor, \
	UniversityAssistantProfessor, UniversityStudent, UniversitySubject, UniversitySchedule
from faculty_create import create_specialization, create_group, create_student
from faculty_update import update, update_group, update_student
from faculty_read import read, read_specialization, read_group, read_student
from faculty_delete import delete, delete_specialization, delete_group, delete_student


def faculty_menu(session, university):
	faculty_cmd = {
		'create_specialization': create_specialization, 
		'create_group': create_group,
		'create_student': create_student,

		'update': update, 
		'update_group': update_group, 
		'update_student': update_student,

		'read': read, 
		'read_specialization': read_specialization, 
		'read_group': read_group,
		'read_student': read_student,

		'delete': delete, 
		'delete_specialization': delete_specialization, 
		'delete_group': delete_group,
		'delete_student': delete_student,
	}

	def faculty_cls(session, faculty):
		os.system('cls')

	faculty_cmd['\x0c'] = faculty_cmd['cls'] = faculty_cmd['clear'] = faculty_cls

	def faculty_help(session, faculty):
		print('Possible commands:\n\t', '\n\t'.join(faculty_cmd.keys()), sep='')

	faculty_cmd['h'] = faculty_cmd['H'] = faculty_cmd['help'] = faculty_cmd['Help'] = \
		faculty_cmd['HELP'] = faculty_help

	def faculty_exit(session, faculty):
		return 1

	faculty_cmd['back'] = faculty_cmd['exit'] = faculty_exit

	name = input("\nEnter the name of faculty to enter the menu of: ")

	try:
		faculty = session.query(UniversityFaculty) \
			.filter(UniversityFaculty.name == name).one()
	except:
		print(f'\n{sys.exc_info()}\n')
		return
	
	while True:
		if faculty_cmd[input("\nEnter the command: ")](session, faculty):
			return
