from sqlalchemy import create_engine, Column, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import pandas as pd

Base = declarative_base()

class TrainingData(Base):
    __tablename__ = 'training_data'

    x = Column(Float, primary_key=True)
    y1 = Column(Float)
    y2 = Column(Float)
    y3 = Column(Float)
    y4 = Column(Float)

class IdealFunction(Base):
    __tablename__ = 'ideal_functions'

    x = Column(Float, primary_key=True)
    y1 = Column(Float)
    y2 = Column(Float)
    y3 = Column(Float)
    y4 = Column(Float)
    y5 = Column(Float)
    y6 = Column(Float)
    y7 = Column(Float)
    y8 = Column(Float)
    y9 = Column(Float)
    y10 = Column(Float)
    y11 = Column(Float)
    y12 = Column(Float)
    y13 = Column(Float)
    y14 = Column(Float)
    y15 = Column(Float)
    y16 = Column(Float)
    y17 = Column(Float)
    y18 = Column(Float)
    y19 = Column(Float)
    y20 = Column(Float)
    y21 = Column(Float)
    y22 = Column(Float)
    y23 = Column(Float)
    y24 = Column(Float)
    y25 = Column(Float)
    y26 = Column(Float)
    y27 = Column(Float)
    y28 = Column(Float)
    y29 = Column(Float)
    y30 = Column(Float)
    y31 = Column(Float)
    y32 = Column(Float)
    y33 = Column(Float)
    y34 = Column(Float)
    y35 = Column(Float)
    y36 = Column(Float)
    y37 = Column(Float)
    y38 = Column(Float)
    y39 = Column(Float)
    y40 = Column(Float)
    y41 = Column(Float)
    y42 = Column(Float)
    y43 = Column(Float)
    y44 = Column(Float)
    y45 = Column(Float)
    y46 = Column(Float)
    y47 = Column(Float)
    y48 = Column(Float)
    y49 = Column(Float)
    y50 = Column(Float)

class TestData(Base):
    __tablename__ = 'test_data'

    id = Column(Integer, primary_key=True, autoincrement=True)
    x = Column(Float)
    y = Column(Float)
    ideal_function_id = Column(Integer)
    deviation = Column(Float)

class Database:
    def __init__(self, db_path):
        self.engine = create_engine(f'sqlite:///{db_path}')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def create_tables(self):
        Base.metadata.create_all(self.engine)

    def clear_tables(self):
        """
        Clear all data from the database tables.
        """
        session = self.Session()
        session.query(TrainingData).delete()
        session.query(IdealFunction).delete()
        session.query(TestData).delete()
        session.commit()
        session.close()
        
    def load_training_data(self, data):
        session = self.Session()
        for _, row in data.iterrows():
            x_value = round(row['x'], 2)  # Round 'x' to 2 decimal places
            record = TrainingData(x=row['x'], y1=row['y1'], y2=row['y2'], y3=row['y3'], y4=row['y4'])
            session.merge(record)
        session.commit()
        session.close()

    def load_ideal_functions(self, data):
        session = self.Session()
        for _, row in data.iterrows():
            record = IdealFunction(x=row['x'], y1 = row['y1'], y2 = row['y2'], y3 = row['y3'], y4 = row['y4'], y5 = row['y5'], y6 = row['y6'], y7 = row['y7'], y8 = row['y8'], y9 = row['y9'], y10 = row['y10'], y11 = row['y11'], y12 = row['y12'], y13 = row['y13'], y14 = row['y14'], y15 = row['y15'], y16 = row['y16'], y17 = row['y17'], y18 = row['y18'], y19 = row['y19'], y20 = row['y20'], y21 = row['y21'], y22 = row['y22'], y23 = row['y23'], y24 = row['y24'], y25 = row['y25'], y26 = row['y26'], y27 = row['y27'], y28 = row['y28'], y29 = row['y29'], y30 = row['y30'], y31 = row['y31'], y32 = row['y32'], y33 = row['y33'], y34 = row['y34'], y35 = row['y35'], y36 = row['y36'], y37 = row['y37'], y38 = row['y38'], y39 = row['y39'], y40 = row['y40'], y41 = row['y41'], y42 = row['y42'], y43 = row['y43'], y44 = row['y44'], y45 = row['y45'], y46 = row['y46'], y47 = row['y47'], y48 = row['y48'], y49 = row['y49'], y50 = row['y50']
)
            session.merge(record)
        session.commit()
        session.close()

    def save_test_data(self, data):
        session = self.Session()
        for record in data:
            test_data = TestData(x=record['x'], y=record['y'], ideal_function_id=record['ideal_function_id'], deviation=record['deviation'])
            session.add(test_data)
        session.commit()
        session.close()

    def get_test_data(self):
        session = self.Session()
        test_data = session.query(TestData).all()
        session.close()
        return pd.DataFrame([(data.x, data.y, data.ideal_function_id, data.deviation) for data in test_data], columns=['x', 'y', 'ideal_function_id', 'deviation'])