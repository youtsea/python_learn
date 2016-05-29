#coding=utf-8

record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = record
print name
print email
print phone_numbers

# 以上为python3 语法