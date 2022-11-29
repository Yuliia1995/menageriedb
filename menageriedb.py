import mysql.connector as mc
conn = mc.connect(host='localhost',user = 'root',password='coding$2022', db='menagerie')
c = conn.cursor(buffered=True)

def show_db():
    c.execute('show databases')
    print("All databases:\n", c.fetchall())
def drop_db():
    c.execute('drop database if exists menagerie')
    c.execute('show databases')
    print(c.fetchall())
def create_table():
    # c.execute('create database menagerie')
    c.execute('use menagerie')
    c.execute('drop table if exists pet')
    c.execute('create table pet (name varchar(20), owner varchar(20), species varchar(20), sex char(1), birth date,'
              'death date)')
    c.execute("insert into pet (name,owner,species,sex,birth,death) values ('Fluffy', 'Harold', 'cat','f', "
              "'1993-02-04',null), ('Claws','Gwen','cat','m','1994-03-17',null), ('Buffy','Harold','dog','f',"
              "'1989-05-13',null), ('Fang','Benny','dog','m','1990-08-27',null),('Bowser', 'Diane','dog','m',"
              "'1979-08-31','1995-07-29'), ('Chirpy','Gwen','bird','f','1998-09-11', null), ('Whistler','Gwen',"
              "'bird',null,'1997-12-09',null), ('Slim','Benny','snake','m','1996-04-29', null)")
def show_structure():
    c.execute('show columns from pet in menagerie')
    print(c.fetchall())
def show_table():
    c.execute('select * from menagerie.pet')
    print(c.fetchall())
def show_female():
    c.execute("select * from pet where sex='f'")
    print(c.fetchall())
def show_name_bthd():
    c.execute("select name as Name, birth as 'Date of Birth' from pet")
    print(c.fetchall())
def show_owner_num_pets():
    c.execute("select owner, count(name) as 'Number of pets' from pet group by owner")
    print(c.fetchall())
def show_month_bthd():
    c.execute("insert into pet (name, birth) values ('Puffball','1999-03-30')")
    c.execute("select name, birth, month(birth) as 'Month of birth' from pet")
    print(c.fetchall())

def commit_close():
    conn.commit()
    c.close()
    conn.close()

def main():
    # show_db()
    # drop_db()
    # create_table()
    # show_structure()
    # show_table()
    # show_female()
    # show_name_bthd()
    # show_owner_num_pets()
    show_month_bthd()
    commit_close()

if __name__ == '__main__':
    main()