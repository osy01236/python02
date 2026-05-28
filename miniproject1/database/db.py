from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from urllib.parse import quote_plus

pw = quote_plus("123456")
DB_URL = f"mysql+pymysql://root:{pw}@localhost:3306/Yong"


#데이터 베이스 연결 - echo는 실행하는 sql 출력(개발시 또는 로그기록용)
engine = create_engine(DB_URL, echo=True)

#DB 쿼리문 실행 시킬 객체
SessionLocal = sessionmaker( autocommit=False, autoflush=False,
                            bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()