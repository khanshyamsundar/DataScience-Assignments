# Read the following data set:
# https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data
# Task:
# 1. Create an sqlalchemy engine using a sample from the data set
# 2. Write two basic update queries
# 3. Write two delete queries
# 4. Write two filter queries
# 5. Write two function queries


from numpy import genfromtxt
from time import time
from sqlalchemy import Column, Integer, Float, Date, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.schema import Sequence
from sqlalchemy import update, insert, delete, func, select

# 1. Create an sqlalchemy engine using a sample from the data set


def Load_Data(file_name):
    data = genfromtxt(file_name, delimiter=',', names=True,
                      dtype=None, encoding=None)
    return data.tolist()


Base = declarative_base()


class Adult_data(Base):

    __tablename__ = 'Adult_data'
    __table_args__ = {'sqlite_autoincrement': True}

    id = Column(Integer, Sequence('id', start=1, increment=1),
                primary_key=True, nullable=False)
    age = Column(Integer)
    workclass = Column(String)
    fnlwgt = Column(Integer)
    education = Column(String)
    education_num = Column(Integer)
    marital_status = Column(String)
    relationship = Column(String)
    occupation = Column(String)
    race = Column(String)
    sex = Column(String)
    capital_gain = Column(Integer)
    capital_loss = Column(Integer)
    hours_per_week = Column(Integer)
    native_country = Column(String)
    salary = Column(String)

    def __repr__(self):
        return "<User(id='%s', age='%s', workclass='%s', fnlwgt='%s', education='%s', \
        education_num='%s', marital_status='%s', relationship='%s', occupation='%s', \
        race='%s', sex='%s', capital_gain='%s', capital_loss='%s', hours_per_week='%s', \
        native_country='%s', salary='%s')>" % (
            self.id, self.age, self.workclass, self.fnlwgt, self.education, self.education_num,
            self.marital_status, self.relationship, self.occupation, self.race, self.sex, self.capital_gain,
            self.capital_loss, self.hours_per_week, self.native_country, self.salary)


engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)

# Create the session
session = sessionmaker()
session.configure(bind=engine)
s = session()


try:
    # sample CSV file used:  http://www.google.com/finance/historical?q=NYSE%3AT&ei=W4ikVam8LYWjmAGjhoHACw&output=csv
    # file_name = "adult_data.csv"
    file_name = "https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data"
    data = Load_Data(file_name)
    t = time()
    for i in data[0:99]:  # Select top 100 rows
        record = Adult_data(**{
            'age': i[0],
            'workclass': i[1],
            'fnlwgt': i[2],
            'education': i[3],
            'education_num': i[4],
            'marital_status': i[5],
            'occupation': i[6],
            'relationship': i[7],
            'race': i[8],
            'sex': i[9],
            'capital_gain': i[10],
            'capital_loss': i[11],
            'hours_per_week': i[12],
            'native_country': i[13],
            'salary': i[14]
        })
        s.add(record)  # Add all the records

    s.commit()  # Attempt to commit all the records
except:
    s.rollback()  # Rollback the changes on error
finally:
    s.close()  # Close the connection
# print("Time elapsed: " + str(time() - t) + " s.")  # 0.091s

# show all data
print('-'*100)
print("Show all data:\n")
print(s.query(Adult_data).all())

# 2. Write two basic update queries
# update age where id = 99
print('-'*100)
stmt = update(Adult_data).where(Adult_data.id == 99).values(age=55)
s.execute(stmt)
s.commit()

print("\nCheck after 1st update:\n")
result_set1 = s.query(Adult_data).filter(Adult_data.id == 99).all()
print(result_set1)

# update salary who has Bechelors
stmt = update(Adult_data).where(Adult_data.education ==
                                ' Bachelors').values(salary='>70k')
s.execute(stmt)
s.commit()

print("\nCheck after 2nd update:\n")
result_set2 = s.query(Adult_data.id, Adult_data.education, Adult_data.salary).filter(
    Adult_data.education == ' Bachelors').all()
print(result_set2)

# 3. Write two delete queries
print("-"*100)
# delete from adult_data where edution = Some-college
stmt = delete(Adult_data).where(Adult_data.education == ' Some-college')
s.execute(stmt)
s.commit()
print("\nCheck after 1st delete:\n")
result_set3 = s.query(Adult_data.id, Adult_data.education, Adult_data.salary).filter(
    Adult_data.education == ' Some-college').all()

# delete from adult_data where id = 101
stmt = delete(Adult_data).where(Adult_data.id == 101)
s.execute(stmt)
s.commit()

print("\nCheck after 2nd delete:\n")
result_set4 = s.query(Adult_data.id, Adult_data.education, Adult_data.salary).filter(
    Adult_data.id == 101).all()
print(result_set4)

# 4. Write two filter queries
print('-'*100)
print("\nfiltered data where workclass is Federal-gov:\n")
result_set5 = s.query(Adult_data).filter(
    Adult_data.workclass == ' Federal-gov').all()
print(result_set5)


print('-'*100)
print("\nfiltered data where education is Bechelors:\n")
result_set6 = s.query(Adult_data.id, Adult_data.education, Adult_data.salary).filter(
    Adult_data.education == ' Bachelors').all()
print(result_set6)


# 5. Write two function queries
print('-'*100)
print("\ndata count who has workclass as Federal-gov:\n")
result_set7 = s.query(func.count(1)).filter(
    Adult_data.workclass == ' Federal-gov').scalar()
print(result_set7)

print("\ntotal working hours group by workclass:\n")
result_set8 = s.query(Adult_data.education, func.sum(
    Adult_data.hours_per_week)).group_by(Adult_data.workclass).all()
print(result_set8)
