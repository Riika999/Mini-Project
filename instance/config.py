import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://solly06:sollypb06@vercel:5.5.5.5/Mini_-_Project'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
