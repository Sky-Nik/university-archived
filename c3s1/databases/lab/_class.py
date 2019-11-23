import datetime as dt
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Boolean, Integer, BigInteger, Date, DateTime, \
	String, Unicode, Text, ForeignKey, CheckConstraint, ForeignKeyConstraint
from sqlalchemy.orm import relationship

Base = declarative_base()


class University(Base):
	__tablename__ = 'university'

	name = Column(String(50), primary_key=True)
	motto = Column(String(50))
	country = Column(String(50), primary_key=True)
	city = Column(String(50), nullable=False)
	established = Column(Date, nullable=False, default=dt.date.today())
	endowment = Column(BigInteger)
	address = Column(String(250))  # nullable=False
	
	rector = relationship("UniversityRector", uselist=False, back_populates="university")
	professors = relationship("UniversityProfessor", back_populates="university", 
		lazy='dynamic')
	faculties = relationship("UniversityFaculty", back_populates="university", 
		lazy='dynamic')

	def __repr__(self):
		return f"University<(name='{self.name}', city='{self.city}', " + \
			f"country='{self.country}', established={self.established})>"

	type = Column(String(50))
	__mapper_args__ = {'polymorphic_on': type, 'polymorphic_identity': 'University'}


class PrivateUniversity(University):
	__mapper_args__ = {'polymorphic_identity': 'Private University'}

	def __repr__(self):
		return f"PrivateUniversity<(name='{self.name}', city='{self.city}', " + \
			f"country='{self.country}', established={self.established})>"


class PublicUniversity(University):
	__mapper_args__ = {'polymorphic_identity': 'Public University'}

	def __repr__(self):
		return f"PublicUniversity<(name='{self.name}', city='{self.city}', " + \
			f"country='{self.country}', established={self.established})>"

	
class UniversityFaculty(Base):
	__tablename__ = 'faculty'

	name = Column(String(50), primary_key=True)
	address = Column(String(250))

	university_name = Column(String(50), primary_key=True)
	university_country = Column(String(50), primary_key=True)
	__table_args__ = (ForeignKeyConstraint([university_name, university_country],
		[University.name, University.country]), {})
	university = relationship("University", back_populates="faculties")

	specializations = relationship("UniversityFacultySpecialization",
		back_populates="faculty", lazy='dynamic')

	def __repr__(self):
		return f"UniversityFaculty<(name='{self.name}', address='{self.address}', " + \
			f"university_name='{self.university_name}', " + \
			f"university_country='{self.university_country}')>"


class UniversityFacultySpecialization(Base):
	__tablename__ = 'specialization'

	name = Column(String(50), primary_key=True)

	faculty_name = Column(String(50), primary_key=True)
	__table_args__ = (ForeignKeyConstraint([faculty_name], [UniversityFaculty.name]), {})
	faculty = relationship("UniversityFaculty", back_populates="specializations")

	groups = relationship("UniversityFacultySpecializationGroup",
		back_populates="specialization", lazy='dynamic')

	def __repr__(self):
		return f"UniversityFacultySpecialization<(name='{self.name}', " + \
			f"faculty_name='{self.faculty_name}')>"


class UniversityFacultySpecializationGroup(Base):
	__tablename__ = 'group'

	name = Column(String(50), primary_key=True)
	course = Column(Integer, CheckConstraint('0 < course AND course < 5'))
	department = Column(String(50))

	CheckConstraint('course < 3 OR department IS NOT NULL')

	specialization_name = Column(String(50), ForeignKey('specialization.name'),
		primary_key=True)
	specialization = relationship("UniversityFacultySpecialization", 
		back_populates="groups")

	students = relationship("UniversityStudent", back_populates="group", lazy='dynamic')

	def __repr__(self):
		return f"UniversityFacultySpecializationGroup<(name='{self.name}', " + \
			f"specialization_name='{self.specialization_name}')>"


class UniversityRector(Base):
	__tablename__ = 'rector'

	passport = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(50), nullable=False)
	fullname = Column(String(50), nullable=False)
	birth_date = Column(Date, nullable=False)
	in_office_from = Column(Date, nullable=False, default=dt.date.today())
	in_office_to = Column(Date, 
		CheckConstraint('(in_office_to IS NULL) OR (in_office_to >= in_office_from)'))

	university_name = Column(String(50), nullable=False)
	university_country = Column(String(50), nullable=False)
	__table_args__ = (ForeignKeyConstraint([university_name, university_country],
		[University.name, University.country]), {})
	university = relationship("University", back_populates="rector")

	def __repr__(self):
		return f"UniversityRector<(name='{self.name}', fullname='{self.fullname}', " + \
			f"birth_date={self.birth_date}, passport={self.passport})>"


class UniversityProfessor(Base):
	__tablename__ = 'professor'

	passport = Column(Integer, primary_key=True)
	name = Column(String(50), nullable=False)
	fullname = Column(String(50), nullable=False)
	birth_date = Column(Date, nullable=False)
	in_office_from = Column(Date, nullable=False, default=dt.date.today())
	in_office_to = Column(Date, 
		CheckConstraint('(in_office_to IS NULL) OR (in_office_to >= in_office_from)'))
	academic_degree = Column(String(5), CheckConstraint('academic_degree == "Prof."'),
		nullable=False, default='Prof.')

	type = Column(String(50), default='universityprofessor')
	__mapper_args__ = {'polymorphic_on': type, 'polymorphic_identity': 'Full Professor'}

	university_name = Column(String(50), nullable=False)
	university_country = Column(String(50), nullable=False)
	__table_args__ = (ForeignKeyConstraint([university_name, university_country],
		[University.name, University.country]), {})

	university = relationship("University", back_populates="professors")

	def __repr__(self):
		return f"UniversityProfessor<(name='{self.name}', fullname='{self.fullname}', " + \
			f"birth_date={self.birth_date}, passport={self.passport})>"


class UniversityAssociateProfessor(UniversityProfessor):
	__mapper_args__ = {'polymorphic_identity': 'Associate Professor'}

	def __repr__(self):
		return f"UniversityAssociateProfessor<(name='{self.name}', " + \
			f"fullname='{self.fullname}', birth_date={self.birth_date}, " + \
			f"passport={self.passport})>"


class UniversityAssistantProfessor(UniversityProfessor):
	__mapper_args__ = {'polymorphic_identity': 'Assistant Professor'}

	def __repr__(self):
		return f"UniversityAssistantProfessor<(name='{self.name}', " + \
			f"fullname='{self.fullname}', birth_date={self.birth_date}, " + \
			f"passport={self.passport})>"


class UniversityStudent(Base):
	__tablename__ = 'student'

	passport = Column(Integer, primary_key=True)
	name = Column(String(50), nullable=False)
	fullname = Column(String(50), nullable=False)
	birth_date = Column(Date, nullable=False)
	entrance_date = Column(Date, nullable=False, default=dt.date.today())
	graduation_date = Column(Date,
		CheckConstraint('(graduation_date IS NULL) OR (graduation_date >= entrance_date)'))

	group_name = Column(String(50), ForeignKey('group.name'), nullable=False)
	group = relationship("UniversityFacultySpecializationGroup", 
		back_populates="students")

	def __repr__(self):
		return f"UniversityStudent<(name='{self.name}', fullname='{self.fullname}', " + \
			f"birth_date={self.birth_date}, passport={self.passport})>"


class UniversitySubject(Base):
	__tablename__ = 'subject'

	name = Column(String(50), primary_key=True)

	def __repr__(self):
		return f"UniversitySubject<(name='{self.name}')>"


class UniversitySchedule(Base):
	__tablename__ = 'schedule'

	subject_name = Column(String(50), ForeignKey('subject.name'), nullable=False)
	subject = relationship("UniversitySubject")
	group_name = Column(String(50), ForeignKey('group.name'), nullable=False)
	group = relationship("UniversityFacultySpecializationGroup")
	professor_passport = Column(Integer, ForeignKey('professor.passport'))
	professor = relationship("UniversityProfessor")

	audience = Column(Integer, primary_key=True)
	weekday = Column(String(50), primary_key=True)
	pair_number = Column(Integer, primary_key=True)

	def __repr__(self):
		return f"UniversitySchedule<(subject_name='{self.subject_name}', " + \
			f"group_name='{self.group_name}', " + \
			f"professor_passport={self.professor_passport})>"
