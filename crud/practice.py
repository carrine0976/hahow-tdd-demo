import pytest
import requests
from bs4 import BeautifulSoup
from models import Board
from sqlalchemy.orm import Session, sessionmaker
def practicepython():
    res=requests.get("https://www.ptt.cc/bbs/index.html")
    soup=BeautifulSoup(res.text,"html")

    result=[]
    for tmp in soup.find_all(name="div", attrs={"class":"board-name"}):
     result.append(tmp.text)
    return result


def insert_ptt_board(name:str):
    pass

def test_insert_ptt_board(sqlite_session):
    expected = "test"
    insert_ptt_board(name=expected)
    assert sqlite_session.query(Board).first().name == expected
def test_practicepython():
    expected="Stock"
    result=practicepython()
    print(result)
    assert expected in result

test_practicepython()


