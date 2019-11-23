import os
import sys
import datetime as dt
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from _class import Base, University, PrivateUniversity, PublicUniversity, UniversityFaculty, \
	UniversityFacultySpecialization, UniversityFacultySpecializationGroup, \
	UniversityRector, UniversityProfessor, UniversityAssociateProfessor, \
	UniversityAssistantProfessor, UniversityStudent, UniversitySubject, UniversitySchedule
from _create import create_university, create_faculty, create_specialization, create_group, \
	create_rector, create_professor, create_student, create_subject
from _update import update_university, update_faculty, update_group, update_rector, \
	update_professor, update_student, update_subject
from _read import read_university, read_faculty, read_specialization, read_group, \
	read_rector, read_professor, read_student, read_subject
from _delete import delete_university, delete_faculty, delete_specialization, delete_group, \
	delete_rector, delete_professor, delete_student, delete_subject
from university_driver import university_menu

cmd = {
	'create_university': create_university, 
	'create_faculty': create_faculty, 
	'create_specialization': create_specialization, 
	'create_group': create_group,
	'create_rector': create_rector, 
	'create_professor': create_professor, 
	'create_student': create_student,
	'create_subject': create_subject,

	'update_university': update_university, 
	'update_faculty': update_faculty, 
	'update_group': update_group, 
	'update_rector': update_rector,
	'update_professor': update_professor,
	'update_student': update_student,
	'update_subject': update_subject,

	'read_university': read_university, 
	'read_faculty': read_faculty, 
	'read_specialization': read_specialization, 
	'read_group': read_group,
	'read_rector': read_rector,
	'read_professor': read_professor,
	'read_student': read_student,
	'read_subject': read_subject,

	'delete_university': delete_university, 
	'delete_faculty': delete_faculty, 
	'delete_specialization': delete_specialization, 
	'delete_group': delete_group,
	'delete_rector': delete_rector,
	'delete_professor': delete_professor,
	'delete_student': delete_student,
	'delete_subject': delete_subject,

	'university_menu': university_menu,
}

def cls(session):
	os.system('cls')

cmd['\x0c'] = cmd['cls'] = cmd['clear'] = cls

def help(session):
	print('Possible commands:\n\t', '\n\t'.join(cmd.keys()), sep='')

cmd['h'] = cmd['H'] = cmd['help'] = cmd['Help'] = cmd['HELP'] = help

engine = create_engine('sqlite:///:memory:')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

while True:
	cmd[input("\nEnter the command: ")](session)
