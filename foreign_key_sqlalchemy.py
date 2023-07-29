import urllib
from sqlalchemy import create_engine,Column, String, Integer, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship


password= urllib.parse.quote_plus("p@ssw0rd")
connection_string = f"postgresql://postgres:{password}@localhost/postgres"
engine = create_engine(connection_string)
Base = declarative_base()
Session = sessionmaker(bind=engine)
class Student(Base):
    __tablename__ ='students'

    id= Column(Integer, primary_key=True)
    name = Column(String(100))
    age = Column(Integer)
    courses = relationship('Course', back_populates="student")

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key = True)
    name = Column(String(100))
    instructor = Column(String(100))
    student_id = Column(Integer, ForeignKey('students.id'))

    student = relationship("Student", back_populates = "courses")

# create table in the database
Base.metadata.create_all(engine)

# Session = sessionmaker()
# session = Session()
with Session() as session:
    student = Student(name= "John", age = 25)
    course = Course(name = "Math", instructor = "Mr. Smith", student_id = 1)

    session.add(student)
    session.add(course)
    session.commit()