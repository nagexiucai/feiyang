#!/usr/bin/env python
#-*-coding:utf-8-*-
'''
@author: hualingson
@license: gpl
'''

import sqlite3

class Database(object):
    DB = None
    def __init__(self, db):
        self.connect = sqlite3.connect(db, check_same_thread=False)
        self.cursor = self.connect.cursor()
    def SQL(self, sql):
        self.cursor.execute(sql)
        self.connect.commit()
    def __del__(self):
        self.cursor.close()
        self.connect.close()
    def List(self):
        return self.cursor.fetchall()
    @staticmethod
    def DoesTableExist(table):
        Database.DB.SQL('PRAGMA table_info([%s]);' % table)
        return Database.DB.List()

# from sqlalchemy import create_engine, Column, ForeignKey, Integer, String
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import relationship
# from sqlalchemy.orm.session import sessionmaker
# 
# Base = declarative_base()
# 
# class Person(Base):
#     __tablename__ = 'person'
#     id = Column(Integer, primary_key=True)
#     name = Column(String(255), nullable=False)
# 
# class Address(Base):
#     __tablename__ = 'address'
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(255))
#     post_code = Column(String(255), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)
# 
# engine = create_engine('sqlite:///:memory:')
# Base.metadata.bind = engine
# Base.metadata.create_all()
# Session = sessionmaker()
# session = Session()
# 
# person = Person(name='xiucai')
# session.add(person)
# session.commit()
# 
# address = Address(street_name='here', post_code="0", person=person)
# session.add(address)
# session.commit()
# 
# persons = session.query(Person).all()
# addresses = session.query(Address).filter(Address.person == person).all()
# for p in persons:
#     print p.name
# for a in addresses:
#     print a.street_name
# 
# session.close_all()

# -----session-----
# add
# add_all
# autocommit
# autoflush
# begin
# begin_nested
# bind
# bind_mapper
# bind_table
# bulk_insert_mappings
# bulk_save_objects
# bulk_update_mappings
# close
# close_all
# commit
# connection
# connection_callable
# delete
# deleted
# dirty
# dispatch
# enable_relationship_loading
# execute
# expire
# expire_all
# expire_on_commit
# expunge
# expunge_all
# flush
# get_bind
# hash_key
# identity_key
# identity_map
# info
# invalidate
# is_active
# is_modified
# merge
# new
# no_autoflush
# object_session
# prepare
# prune
# public_methods
# query
# refresh
# rollback
# scalar
# transaction
# twophase
# 
# -----engine-----
# begin
# connect
# contextual_connect
# create
# dialect
# dispatch
# dispose
# driver
# drop
# echo
# engine
# execute
# execution_options
# has_table
# logger
# logging_name
# name
# pool
# raw_connection
# run_callable
# scalar
# schema_for_object
# table_names
# transaction
# update_execution_options
# url
