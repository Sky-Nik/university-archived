# Object Relational Tutorial

The SQLAlchemy Object Relational Mapper presents a method of associating user-defined Python classes with database tables, and instances of those classes (objects) with rows in their corresponding tables. It includes a system that transparently synchronizes all changes in state between objects and their related rows, called a [unit of work](https://docs.sqlalchemy.org/en/latest/glossary.html#term-unit-of-work), as well as a system for expressing database queries in terms of the user defined classes and their defined relationships between each other.

The ORM is in contrast to the SQLAlchemy Expression Language, upon which the ORM is constructed. Whereas the SQL Expression Language, introduced in [SQL Expression Language Tutorial](https://docs.sqlalchemy.org/en/latest/core/tutorial.html), presents a system of representing the primitive constructs of the relational database directly without opinion, the ORM presents a high level and abstracted pattern of usage, which itself is an example of applied usage of the Expression Language.

While there is overlap among the usage patterns of the ORM and the Expression Language, the similarities are more superficial than they may at first appear. One approaches the structure and content of data from the perspective of a user-defined [domain model](https://docs.sqlalchemy.org/en/latest/glossary.html#term-domain-model) which is transparently persisted and refreshed from its underlying storage model. The other approaches it from the perspective of literal schema and SQL expression representations which are explicitly composed into messages consumed individually by the database.

A successful application may be constructed using the Object Relational Mapper exclusively. In advanced situations, an application constructed with the ORM may make occasional usage of the Expression Language directly in certain areas where specific database interactions are required.

The following tutorial is in doctest format, meaning each `>>>` line represents something you can type at a Python command prompt, and the following text represents the expected return value.

## Version Check

A quick check to verify that we are on at least **version 1.3** of SQLAlchemy:

```python
>>> import sqlalchemy

>>> sqlalchemy.__version__
1.3.0
```

## Connecting

For this tutorial we will use an in-memory-only SQLite database. To connect we use `create_engine()`:

```python
>>> from sqlalchemy import create_engine

>>> engine = create_engine('sqlite:///:memory:', echo=True)
```

The `echo` flag is a shortcut to setting up SQLAlchemy logging, which is accomplished via Python’s standard `logging` module. With it enabled, we’ll see all the generated SQL produced. If you are working through this tutorial and want less output generated, set it to `False`. This tutorial will format the SQL behind a popup window so it doesn’t get in our way; just click the “SQL” links to see what’s being generated.

The return value of `create_engine()` is an instance of `Engine`, and it represents the core interface to the database, adapted through a dialect that handles the details of the database and [DBAPI](https://docs.sqlalchemy.org/en/latest/glossary.html#term-dbapi) in use. In this case the SQLite dialect will interpret instructions to the Python built-in `sqlite3` module.

The first time a method like `Engine.execute()` or `Engine.connect()` is called, the `Engine` establishes a real [DBAPI](https://docs.sqlalchemy.org/en/latest/glossary.html#term-dbapi) connection to the database, which is then used to emit the SQL. When using the ORM, we typically don’t use the `Engine` directly once created; instead, it’s used behind the scenes by the ORM as we’ll see shortly.

**Lazy Connecting**

The `Engine`, when first returned by `create_engine()`, has not actually tried to connect to the database yet; that happens only the first time it is asked to perform a task against the database.

**See also**

[Database Urls](https://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls) - includes examples of `create_engine()` connecting to several kinds of databases with links to more information.

## Declare a Mapping

When using the ORM, the configurational process starts by describing the database tables we’ll be dealing with, and then by defining our own classes which will be mapped to those tables. In modern SQLAlchemy, these two tasks are usually performed together, using a system known as [Declarative](https://docs.sqlalchemy.org/en/latest/orm/extensions/declarative/index.html), which allows us to create classes that include directives to describe the actual database table they will be mapped to.

Classes mapped using the Declarative system are defined in terms of a base class which maintains a catalog of classes and tables relative to that base - this is known as the **declarative base class**. Our application will usually have just one instance of this base in a commonly imported module. We create the base class using the `declarative_base()` function, as follows:

```python
>>> from sqlalchem.ext.declarative import declarative_base

>>> Base = declarative_base()
```

Now that we have a “base”, we can define any number of mapped classes in terms of it. We will start with just a single table called `users`, which will store records for the end-users using our application. A new class called `User` will be the class to which we map this table. Within the class, we define details about the table to which we’ll be mapping, primarily the table name, and names and datatypes of columns:

```python
>>> from sqlalchemy import Column, Integer, String

>>> class User(Base):
... 	__tablename__ = 'users'
... 
... 	id = Column(Integer, primary_key=True)
... 	name = Column(String)
... 	fullname = Column(String)
... 	password = Column(String)
... 
... 	def __repr__(self):
... 		return f"<User(name='{self.name}', fullname='{self.fullname}', password='{self.password}')>"
```

A class using Declarative at a minimum needs a `__tablename__` attribute, and at least one `Column` which is part of a primary key [[1]](https://docs.sqlalchemy.org/en/latest/faq/ormconfiguration.html#faq-mapper-primary-key). SQLAlchemy never makes any assumptions by itself about the table to which a class refers, including that it has no built-in conventions for names, datatypes, or constraints. But this doesn’t mean boilerplate is required; instead, you’re encouraged to create your own automated conventions using helper functions and mixin classes, which is described in detail at [Mixin and Custom Base Classes](https://docs.sqlalchemy.org/en/latest/orm/extensions/declarative/mixins.html#declarative-mixins).

When our class is constructed, Declarative replaces all the `Column` objects with special Python accessors known as [descriptors](https://docs.sqlalchemy.org/en/latest/glossary.html#term-descriptors); this is a process known as [instrumentation](https://docs.sqlalchemy.org/en/latest/glossary.html#term-instrumentation). The “instrumented” mapped class will provide us with the means to refer to our table in a SQL context as well as to persist and load the values of columns from the database.

Outside of what the mapping process does to our class, the class remains otherwise mostly a normal Python class, to which we can define any number of ordinary attributes and methods needed by our application.

**Tip**

The `User` class defines a `__repr__()` method, but note that is **optional**; we only implement it in this tutorial so that our examples show nicely formatted `User` objects.

## Create a Schema

With our `User` class constructed via the Declarative system, we have defined information about our table, known as table metadata. The object used by SQLAlchemy to represent this information for a specific table is called the `Table` object, and here Declarative has made one for us. We can see this object by inspecting the `__table__` attribute:

```python
>>> User.__table__ 
Table(
	'users', 
	MetaData(bind=None),
	Column('id', Integer(), table=<users>, primary_key=True, nullable=False),
	Column('name', String(), table=<users>),
	Column('fullname', String(), table=<users>),
	Column('password', String(), table=<users>), 
	schema=None
)
```

When we declared our class, `Declarative` used a Python metaclass in order to perform additional activities once the class declaration was complete; within this phase, it then created a `Table` object according to our specifications, and associated it with the class by constructing a `Mapper` object. This object is a behind-the-scenes object we normally don’t need to deal with directly (though it can provide plenty of information about our mapping when we need it).

**Classical Mappings**

The `Declarative` system, though highly recommended, is not required in order to use SQLAlchemy’s ORM. Outside of `Declarative`, any plain Python class can be mapped to any `Table` using the `mapper()` function directly; this less common usage is described at [Classical Mappings](https://docs.sqlalchemy.org/en/latest/orm/mapping_styles.html#classical-mapping).

The `Table` object is a member of a larger collection known as `MetaData`. When using Declarative, this object is available using the `.metadata` attribute of our declarative base class.

The `MetaData` is a registry which includes the ability to emit a limited set of schema generation commands to the database. As our SQLite database does not actually have a users table present, we can use `MetaData` to issue `CREATE TABLE` statements to the database for all tables that don’t yet exist. Below, we call the `MetaData.create_all()` method, passing in our `Engine` as a source of database connectivity. We will see that special commands are first emitted to check for the presence of the users table, and following that the actual `CREATE TABLE` statement:

```python
>>> Base.metadata.create_all(engine)
```
```sql
SELECT ...
PRAGMA table_info("users")
()
CREATE TABLE users (
	id INTEGER NOT NULL,
	name VARCHAR,
	fullname VARCHAR,
	password VARCHAR,
	PRIMARY KEY (id)
)
()
COMMIT
```

**Minimal Table Descriptions vs. Full Descriptions**

Users familiar with the syntax of `CREATE TABLE` may notice that the VARCHAR columns were generated without a length; on SQLite and PostgreSQL, this is a valid datatype, but on others, it’s not allowed. So if running this tutorial on one of those databases, and you wish to use SQLAlchemy to issue `CREATE TABLE`, a “length” may be provided to the `String` type as below:

```python
Column(String(50))
```

The length field on `String`, as well as similar precision/scale fields available on `Integer`, `Numeric`, etc. are not referenced by SQLAlchemy other than when creating tables.

Additionally, Firebird and Oracle require sequences to generate new primary key identifiers, and SQLAlchemy doesn’t generate or assume these without being instructed. For that, you use the `Sequence` construct:

```python
from sqlalchemy import Sequence

Column(Integer, Sequence('user_id_seq'), primary_key=True)
```

A full, foolproof `Table` generated via our declarative mapping is therefore:

```python
class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
	name = Column(String(50))
	fullname = Column(String(50))
	password = Column(String(12))

	def __repr__(self):
		return f"<User(name='{self.name}', fullname='{self.fullname}', password='{self.password}')>"
```

We include this more verbose table definition separately to highlight the difference between a minimal construct geared primarily towards in-Python usage only, versus one that will be used to emit `CREATE TABLE` statements on a particular set of backends with more stringent requirements.

## Create an Instance of the Mapped Class

With mappings complete, let’s now create and inspect a `User` object:

```python
>>> ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')

>>> ed_user.name
'ed'
>>> ed_user.password
'edspassword'
>>> str(ed_user.id)
'None'
```

Even though we didn’t specify it in the constructor, the `id` attribute still produces a value of `None` when we access it (as opposed to Python’s usual behavior of raising `AttributeError` for an undefined attribute). SQLAlchemy’s [instrumentation](https://docs.sqlalchemy.org/en/latest/glossary.html#term-instrumentation) normally produces this default value for column-mapped attributes when first accessed. For those attributes where we’ve actually assigned a value, the instrumentation system is tracking those assignments for use within an eventual `INSERT` statement to be emitted to the database.

**the `__init__()` method**

Our `User` class, as defined using the Declarative system, has been provided with a constructor (e.g. `__init__()` method) which automatically accepts keyword names that match the columns we’ve mapped. We are free to define any explicit `__init__()` method we prefer on our class, which will override the default method provided by `Declarative`.

## Creating a Session

We’re now ready to start talking to the database. The ORM’s “handle” to the database is the `Session`. When we first set up the application, at the same level as our `create_engine()` statement, we define a `Session` class which will serve as a factory for new `Session` objects:

```python
>>> from sqlalchemy.orm import sessionmaker

>>> Session = sessionmaker(bind=engine)
```

In the case where your application does not yet have an `Engine` when you define your module-level objects, just set it up like this:

```python
>>> Session = sessionmaker()
```

Later, when you create your engine with `create_engine()`, connect it to the `Session` using `configure()`:

```python
>>> Session.configure(bind=engine)  # once engine is available
```

This custom-made `Session` class will create new `Session` objects which are bound to our database. Other transactional characteristics may be defined when calling `sessionmaker` as well; these are described in a later chapter. Then, whenever you need to have a conversation with the database, you instantiate a `Session`:

```python
>>> session = Session()
```

The above `Session` is associated with our SQLite-enabled `Engine`, but it hasn’t opened any connections yet. When it’s first used, it retrieves a connection from a pool of connections maintained by the `Engine`, and holds onto it until we commit all changes and/or close the session object.

**Session Lifecycle Patterns**

The question of when to make a `Session` depends a lot on what kind of application is being built. Keep in mind, the `Session` is just a workspace for your objects, local to a particular database connection - if you think of an application thread as a guest at a dinner party, the `Session` is the guest’s plate and the objects it holds are the food (and the database … the kitchen?)! More on this topic available at [When do I construct a Session, when do I commit it, and when do I close it?](https://docs.sqlalchemy.org/en/latest/orm/session_basics.html#session-faq-whentocreate).

## Adding and Updating Objects

To persist our `User` object, we `add()` it to our `Session`:

```python
>>> ed_user = User(name='ed', fullname='Ed Jones', password='edspassword')

>>> session.add(ed_user)
```

At this point, we say that the instance is **pending**; no SQL has yet been issued and the object is not yet represented by a row in the database. The `Session` will issue the SQL to persist `Ed Jones` as soon as is needed, using a process known as a **flush**. If we query the database for `Ed Jones`, all pending information will first be flushed, and the query is issued immediately thereafter.

For example, below we create a new `Query` object which loads instances of `User`. We “filter by” the `name` attribute of `ed`, and indicate that we’d like only the first result in the full list of rows. A `User` instance is returned which is equivalent to that which we’ve added:

```python
>>> our_user = session.query(User).filter_by(name='ed').first()
```
```sql 
BEGIN (implicit)
INSERT INTO users (name, fullname, password) 
VALUES (?, ?, ?)
('ed', 'Ed Jones', 'edspassword')
```
```sql
SELECT users.id AS users_id,
	users.name AS users_name,
	users.fullname AS users_fullname,
	users.password AS users_password
FROM users
WHERE users.name = ?
LIMIT ? OFFSET ?
('ed', 1, 0)
```
```python
>>> our_user
<User(name='ed', fullname='Ed Jones', password='edspassword')>
```

In fact, the `Session` has identified that the row returned is the same row as one already represented within its internal map of objects, so we actually got back the identical instance as that which we just added:

```python
>>> ed_user is our_user
True
```

The ORM concept at work here is known as an [identity map](https://docs.sqlalchemy.org/en/latest/glossary.html#term-identity-map) and ensures that all operations upon a particular row within a `Session` operate upon the same set of data. Once an object with a particular primary key is present in the `Session`, all SQL queries on that `Session` will always return the same Python object for that particular primary key; it also will raise an error if an attempt is made to place a second, already-persisted object with the same primary key within the session.

We can add more `User` objects at once using `add_all()`:

```python
>>> session.add_all([
... 	User(name='wendy', fullname='Wendy Williams', password='foobar'),
... 	User(name='mary', fullname='Mary Contrary', password='xxg527'),
... 	User(name='fred', fullname='Fred Flinstone', password='blah'),
... ])
```

Also, we’ve decided the password for Ed isn’t too secure, so lets change it:

```python
>>> ed_user.password = 'f8s7ccs'
```

The `Session` is paying attention. It knows, for example, that `Ed Jones` has been modified:

```python
>>> session.dirty
IdentitySet([<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>])
```

and that three new `User` objects are pending:

```python
>>> session.new  
IdentitySet([
	<User(name='wendy', fullname='Wendy Williams', password='foobar')>,
	<User(name='mary', fullname='Mary Contrary', password='xxg527')>,
	<User(name='fred', fullname='Fred Flinstone', password='blah')>,
])
```

We tell the `Session` that we’d like to issue all remaining changes to the database and commit the transaction, which has been in progress throughout. We do this via `commit()`. The `Session` emits the `UPDATE` statement for the password change on “ed”, as well as `INSERT` statements for the three new `User` objects we’ve added:

```python
>>> session.commit()
``` 
```sql
UPDATE users 
SET password=? 
WHERE users.id = ?
('f8s7ccs', 1)
```
```sql
INSERT INTO users (name, fullname, password) 
VALUES (?, ?, ?)
('wendy', 'Wendy Williams', 'foobar')
INSERT INTO users (name, fullname, password) 
VALUES (?, ?, ?)
('mary', 'Mary Contrary', 'xxg527')
INSERT INTO users (name, fullname, password) 
VALUES (?, ?, ?)
('fred', 'Fred Flinstone', 'blah')
COMMIT
```

`commit()` flushes the remaining changes to the database, and commits the transaction. The connection resources referenced by the session are now returned to the connection pool. Subsequent operations with this session will occur in a **new** transaction, which will again re-acquire connection resources when first needed.

If we look at Ed’s `id` attribute, which earlier was `None`, it now has a value:

```python
>>> ed_user.id 
```
```sql
BEGIN (implicit)
SELECT users.id AS users_id,
	users.name AS users_name,
	users.fullname AS users_fullname,
	users.password AS users_password
FROM users
WHERE users.id = ?
(1,)
```
```python
1
```

After the `Session` inserts new rows in the database, all newly generated identifiers and database-generated defaults become available on the instance, either immediately or via load-on-first-access. In this case, the entire row was re-loaded on access because a new transaction was begun after we issued `commit()`. SQLAlchemy by default refreshes data from a previous transaction the first time it’s accessed within a new transaction, so that the most recent state is available. The level of reloading is configurable as is described in [Using the Session](https://docs.sqlalchemy.org/en/latest/orm/session.html).

**Session Object States**

As our `User` object moved from being outside the `Session`, to inside the `Session` without a primary key, to actually being inserted, it moved between three out of four available “object states” - **transient**, **pending**, and **persistent**. Being aware of these states and what they mean is always a good idea - be sure to read [Quickie Intro to Object States](https://docs.sqlalchemy.org/en/latest/orm/session_state_management.html#session-object-states) for a quick overview.

## Rolling Back

Since the `Session` works within a transaction, we can roll back changes made too. Let’s make two changes that we’ll revert; `ed_user`’s user name gets set to `Edwardo`:

```python
>>> ed_user.name = 'Edwardo'
```

and we’ll add another erroneous user, `fake_user`:

```python
>>> fake_user = User(name='fakeuser', fullname='Invalid', password='12345')

>>> session.add(fake_user)
```

Querying the session, we can see that they’re flushed into the current transaction:

```python
>>> session.query(User).filter(User.name.in_(['Edwardo', 'fakeuser'])).all()
```
```sql
UPDATE users 
SET name=? 
WHERE users.id = ?
('Edwardo', 1)
```
```sql
INSERT INTO users (name, fullname, password) 
VALUES (?, ?, ?)
('fakeuser', 'Invalid', '12345')
```
```sql
SELECT users.id AS users_id,
	users.name AS users_name,
	users.fullname AS users_fullname,
	users.password AS users_password
FROM users
WHERE users.name IN (?, ?)
('Edwardo', 'fakeuser')
```
```python
[
	<User(name='Edwardo', fullname='Ed Jones', password='f8s7ccs')>,
	<User(name='fakeuser', fullname='Invalid', password='12345')>,
]
```

Rolling back, we can see that `ed_user`’s name is back to `ed`, and `fake_user` has been kicked out of the session:

```python
>>> session.rollback()
```
```sql
ROLLBACK
```
```python
>>> ed_user.name
```
```sql
BEGIN (implicit)
SELECT users.id AS users_id,
	users.name AS users_name,
	users.fullname AS users_fullname,
	users.password AS users_password
FROM users
WHERE users.id = ?
(1,)
```
```python
u'ed'
```
```python
>>> fake_user in session
False
```

issuing a `SELECT` illustrates the changes made to the database:
```python
>>> session.query(User).filter(User.name.in_(['ed', 'fakeuser'])).all()
```
```sql
SELECT users.id AS users_id,
	users.name AS users_name,
	users.fullname AS users_fullname,
	users.password AS users_password
FROM users
WHERE users.name IN (?, ?)
('ed', 'fakeuser')
```
```python
[<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>]
```

## Querying

A `Query` object is created using the `query()` method on `Session`. This function takes a variable number of arguments, which can be any combination of classes and class-instrumented descriptors. Below, we indicate a `Query` which loads `User` instances. When evaluated in an iterative context, the list of `User` objects present is returned:

```python
>>> for instance in session.query(User).order_by(User.id):
...     print(instance.name, instance.fullname)
```
```sql
SELECT users.id AS users_id,
	users.name AS users_name,
	users.fullname AS users_fullname,
	users.password AS users_password
FROM users
ORDER BY users.id
()
```
```python
ed Ed Jones
wendy Wendy Williams
mary Mary Contrary
fred Fred Flinstone
```

The `Query` also accepts ORM-instrumented descriptors as arguments. Any time multiple class entities or column-based entities are expressed as arguments to the `query()` function, the return result is expressed as tuples:

```python
>>> for name, fullname in session.query(User.name, User.fullname):
...     print(name, fullname)
```
```sql
SELECT users.name AS users_name,
	users.fullname AS users_fullname
FROM users
()
```
```python
ed Ed Jones
wendy Wendy Williams
mary Mary Contrary
fred Fred Flinstone
```

The tuples returned by `Query` are _named_ tuples, supplied by the `KeyedTuple` class, and can be treated much like an ordinary Python object. The names are the same as the attribute’s name for an attribute, and the class name for a class:

```python
>>> for row in session.query(User, User.name).all():
...    print(row.User, row.name)
```
```sql
SELECT users.id AS users_id,
	users.name AS users_name,
	users.fullname AS users_fullname,
	users.password AS users_password
FROM users
()
```
```python
<User(name='ed', fullname='Ed Jones', password='f8s7ccs')> ed
<User(name='wendy', fullname='Wendy Williams', password='foobar')> wendy
<User(name='mary', fullname='Mary Contrary', password='xxg527')> mary
<User(name='fred', fullname='Fred Flinstone', password='blah')> fred
```

You can control the names of individual column expressions using the `label()` construct, which is available from any `ColumnElement`-derived object, as well as any class attribute which is mapped to one (such as `User.name`):

```python
>>> for row in session.query(User.name.label('name_label')).all():
...    print(row.name_label)
```
```sql
SELECT users.name AS name_label
FROM users
()
```
```python
ed
wendy
mary
fred
```

The name given to a full entity such as `User`, assuming that multiple entities are present in the call to `query()`, can be controlled using `aliased()`:

```python
>>> from sqlalchemy.orm import aliased
>>> user_alias = aliased(User, name='user_alias')

>>> for row in session.query(user_alias, user_alias.name).all():
...    print(row.user_alias)
```
```sql
SELECT user_alias.id AS user_alias_id,
	user_alias.name AS user_alias_name,
	user_alias.fullname AS user_alias_fullname,
	user_alias.password AS user_alias_password
FROM users AS user_alias
()
```
```python
<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>
<User(name='wendy', fullname='Wendy Williams', password='foobar')>
<User(name='mary', fullname='Mary Contrary', password='xxg527')>
<User(name='fred', fullname='Fred Flinstone', password='blah')>
```

Basic operations with `Query` include issuing LIMIT and OFFSET, most conveniently using Python array slices and typically in conjunction with ORDER BY:

```python
>>> for u in session.query(User).order_by(User.id)[1:3]:
...    print(u)
```
```sql
SELECT users.id AS users_id,
	users.name AS users_name,
	users.fullname AS users_fullname,
	users.password AS users_password
FROM users 
ORDER BY users.id
LIMIT ? OFFSET ?
(2, 1)
```
```python
<User(name='wendy', fullname='Wendy Williams', password='foobar')>
<User(name='mary', fullname='Mary Contrary', password='xxg527')>
```

and filtering results, which is accomplished either with `filter_by()`, which uses keyword arguments:

```python
>>> for name, in session.query(User.name).filter_by(fullname='Ed Jones'):
...    print(name)
```
```sql
SELECT users.name AS users_name 
FROM users
WHERE users.fullname = ?
('Ed Jones',)
```
```python
ed
```

… or `filter()`, which uses more flexible SQL expression language constructs. These allow you to use regular Python operators with the class-level attributes on your mapped class:

```python
>>> for name, in session.query(User.name).filter(User.fullname=='Ed Jones'):
...    print(name)
```
```sql
SELECT users.name AS users_name 
FROM users
WHERE users.fullname = ?
('Ed Jones',)
```
```python
ed
```

The `Query` object is fully **generative**, meaning that most method calls return a new `Query` object upon which further criteria may be added. For example, to query for users named “ed” with a full name of “Ed Jones”, you can call `filter()` twice, which joins criteria using `AND`:

```python
>>> for user in session.query(User).filter(User.name=='ed').filter(User.fullname=='Ed Jones'):
...    print(user)
```
```sql
SELECT users.id AS users_id,
	users.name AS users_name,
	users.fullname AS users_fullname,
	users.password AS users_password
FROM users
WHERE users.name = ? 
	AND users.fullname = ?
('ed', 'Ed Jones')
```
```python
<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>
```

### Common Filter Operators

Here’s a rundown of some of the most common operators used in `filter()`:

* `equals`:

```python
query.filter(User.name == 'ed')
```

* `not equals`:

```python
query.filter(User.name != 'ed')
```

* `LIKE`:

```python
query.filter(User.name.like('%ed%'))
```

**Note**

`ColumnOperators.like()` renders the LIKE operator, which is case insensitive on some backends, and case sensitive on others. For guaranteed case-insensitive comparisons, use `ColumnOperators.ilike()`.

* `ILIKE` (case-insensitive LIKE):

```python
query.filter(User.name.ilike('%ed%'))
```

**Note**

most backends don’t support ILIKE directly. For those, the `ColumnOperators.ilike()` operator renders an expression combining LIKE with the LOWER SQL function applied to each operand.

* `IN`:

```python
query.filter(User.name.in_(['ed', 'wendy', 'jack']))

# works with query objects too:
query.filter(User.name.in_(
    session.query(User.name).filter(User.name.like('%ed%'))
))
```

* `NOT IN`:

```python
query.filter(~User.name.in_(['ed', 'wendy', 'jack']))
```

* `IS NULL`:

```python
query.filter(User.name == None)

# alternatively, if pep8/linters are a concern
query.filter(User.name.is_(None))
```

* `IS NOT NULL`:

```python
query.filter(User.name != None)

# alternatively, if pep8/linters are a concern
query.filter(User.name.isnot(None))
```

* `AND`:

```python
# use and_()
from sqlalchemy import and_
query.filter(and_(User.name == 'ed', User.fullname == 'Ed Jones'))

# or send multiple expressions to .filter()
query.filter(User.name == 'ed', User.fullname == 'Ed Jones')

# or chain multiple filter()/filter_by() calls
query.filter(User.name == 'ed').filter(User.fullname == 'Ed Jones')
```

**Note**

Make sure you use `and_()` and **not** the Python and operator!

* `OR`:

```python
from sqlalchemy import or_
query.filter(or_(User.name == 'ed', User.name == 'wendy'))
```

**Note**

Make sure you use `or_()` and **not** the Python or operator!

* `MATCH`:

```python
query.filter(User.name.match('wendy'))
```

**Note**

`match()` uses a database-specific `MATCH` or `CONTAINS` function; its behavior will vary by backend and is not available on some backends such as SQLite.

### Returning Lists and Scalars

A number of methods on `Query` immediately issue SQL and return a value containing loaded database results. Here’s a brief tour:

* `all()` returns a list:

```python
>>> query = session.query(User).filter(User.name.like('%ed')).order_by(User.id)

>>> query.all()
```
```sql
SELECT users.id AS users_id,
	users.name AS users_name,
	users.fullname AS users_fullname,
	users.password AS users_password
FROM users
WHERE users.name LIKE ? 
ORDER BY users.id
('%ed',)
```
```python
[
	<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>,
	<User(name='fred', fullname='Fred Flinstone', password='blah')>,
]
```

`first()` applies a limit of one and returns the first result as a scalar:

```python
>>> query.first()
```
```sql
SELECT users.id AS users_id,
	users.name AS users_name,
	users.fullname AS users_fullname,
	users.password AS users_password
FROM users
WHERE users.name LIKE ? 
ORDER BY users.id
LIMIT ? OFFSET ?
('%ed', 1, 0)
```
```python
<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>
```

* `one()` fully fetches all rows, and if not exactly one object identity or composite row is present in the result, raises an error. With multiple rows found:

```python
>>> user = query.one()
Traceback (most recent call last):
...
MultipleResultsFound: Multiple rows were found for one()
```

With no rows found:

```
>>> user = query.filter(User.id == 99).one()
Traceback (most recent call last):
...
NoResultFound: No row was found for one()
```

The `one()` method is great for systems that expect to handle “no items found” versus “multiple items found” differently; such as a RESTful web service, which may want to raise a “404 not found” when no results are found, but raise an application error when multiple results are found.

* `one_or_none()` is like `one()`, except that if no results are found, it doesn’t raise an error; it just returns `None`. Like `one()`, however, it does raise an error if multiple results are found.

* `scalar()` invokes the `one()` method, and upon success returns the first column of the row:

```python
>>> query = session.query(User.id).filter(User.name == 'ed').order_by(User.id)

>>> query.scalar()
```
```sql
SELECT users.id AS users_id
FROM users
WHERE users.name = ? 
ORDER BY users.id
('ed',)
```
```python
1
```

### Using Textual SQL

Literal strings can be used flexibly with `Query`, by specifying their use with the `text()` construct, which is accepted by most applicable methods. For example, `filter()` and `order_by()`:

```python
>>> from sqlalchemy import text

>>> for user in session.query(User).filter(text("id < 224")).order_by(text("id")).all():
...     print(user.name)
```
```sql
SELECT users.id AS users_id,
	users.name AS users_name,
	users.fullname AS users_fullname,
	users.password AS users_password
FROM users
WHERE id < 224 
ORDER BY id
()
```
```python
ed
wendy
mary
fred
```

Bind parameters can be specified with string-based SQL, using a colon. To specify the values, use the `params()` method:

```python
>>> session.query(User).filter(text("id<:value and name=:name")).params(value=224, name='fred').order_by(User.id).one()
```
```sql
SELECT users.id AS users_id,
	users.name AS users_name,
	users.fullname AS users_fullname,
	users.password AS users_password
FROM users
WHERE id < ? and name = ? 
ORDER BY users.id
(224, 'fred')
```
```python
<User(name='fred', fullname='Fred Flinstone', password='blah')>
```

To use an entirely string-based statement, a `text()` construct representing a complete statement can be passed to `from_statement()`. Without additional specifiers, the columns in the string SQL are matched to the model columns based on name, such as below where we use just an asterisk to represent loading all columns:

```python
>>> session.query(User).from_statement(text("SELECT * FROM users where name=:name")).params(name='ed').all()
```
```sql
SELECT * 
FROM users 
WHERE name=?
('ed',)
```
```python
[<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>]
```

Matching columns on name works for simple cases but can become unwieldy when dealing with complex statements that contain duplicate column names or when using anonymized ORM constructs that don’t easily match to specific names. Additionally, there is typing behavior present in our mapped columns that we might find necessary when handling result rows. For these cases, the `text()` construct allows us to link its textual SQL to Core or ORM-mapped column expressions positionally; we can achieve this by passing column expressions as positional arguments to the `TextClause.columns()` method:

```python
>>> stmt = text(
... 	"SELECT name, id, fullname, password "
... 	"FROM users where name=:name"
... )

>>> stmt = stmt.columns(User.name, User.id, User.fullname, User.password)

>>> session.query(User).from_statement(stmt).params(name='ed').all()
```
```sql
SELECT name, id, fullname, password FROM users where name=?
('ed',)
```
```python
[<User(name='ed', fullname='Ed Jones', password='f8s7ccs')>]
```

_New in version 1.1_: The `TextClause.columns()` method now accepts column expressions which will be matched positionally to a plain text SQL result set, eliminating the need for column names to match or even be unique in the SQL statement.

When selecting from a `text()` construct, the `Query` may still specify what columns and entities are to be returned; instead of `query(User)` we can also ask for the columns individually, as in any other case:

```python
>>> stmt = text("SELECT name, id FROM users where name=:name")

>>> stmt = stmt.columns(User.name, User.id)

>>> session.query(User.id, User.name).from_statement(stmt).params(name='ed').all()
```
```sql
SELECT name, id FROM users where name=?
('ed',)
```
```python
[(1, u'ed')]
```

**See also**

[Using Textual SQL](https://docs.sqlalchemy.org/en/latest/core/tutorial.html#sqlexpression-text) - The `text()` construct explained from the perspective of Core-only queries.

### Counting

`Query` includes a convenience method for counting called `count()`:

```python
>>> session.query(User).filter(User.name.like('%ed')).count()
```
```sql
SELECT count(*) AS count_1
FROM (
	SELECT users.id AS users_id,
		users.name AS users_name,
		users.fullname AS users_fullname,
		users.password AS users_password
	FROM users
	WHERE users.name LIKE ?
) AS anon_1
('%ed',)
```
```python
2
```

The `count()` method is used to determine how many rows the SQL statement would return. Looking at the generated SQL above, SQLAlchemy always places whatever it is we are querying into a subquery, then counts the rows from that. In some cases this can be reduced to a simpler `SELECT count(*) FROM table`, however modern versions of SQLAlchemy don’t try to guess when this is appropriate, as the exact SQL can be emitted using more explicit means.

**Counting on `count()`**

`Query.count()` used to be a very complicated method when it would try to guess whether or not a subquery was needed around the existing query, and in some exotic cases it wouldn’t do the right thing. Now that it uses a simple subquery every time, it’s only two lines long and always returns the right answer. Use `func.count()` if a particular statement absolutely cannot tolerate the subquery being present.

For situations where the “thing to be counted” needs to be indicated specifically, we can specify the “count” function directly using the expression `func.count()`, available from the `func` construct. Below we use it to return the count of each distinct user name:

```python
>>> from sqlalchemy import func

>>> session.query(func.count(User.name), User.name).group_by(User.name).all()
```
```sql
SELECT count(users.name) AS count_1, 
	users.name AS users_name
FROM users 
GROUP BY users.name
()
```
```python
[(1, u'ed'), (1, u'fred'), (1, u'mary'), (1, u'wendy')]
```

To achieve our simple `SELECT count(*) FROM table`, we can apply it as:

```python
>>> session.query(func.count('*')).select_from(User).scalar()
```
```sql
SELECT count(?) AS count_1
FROM users
('*',)
```
```python
4
```

The usage of `select_from()` can be removed if we express the count in terms of the User primary key directly:

```python
>>> session.query(func.count(User.id)).scalar()
```
```sql
SELECT count(users.id) AS count_1
FROM users
()
```
```python
4
```

## Building a Relationship

Let’s consider how a second table, related to `User`, can be mapped and queried. Users in our system can store any number of email addresses associated with their username. This implies a basic one to many association from the `users` to a new table which stores email addresses, which we will call `addresses`. Using declarative, we define this table along with its mapped class, `Address`:

```python
>>> from sqlalchemy import ForeignKey
>>> from sqlalchemy.orm import relationship

>>> class Address(Base):
...     __tablename__ = 'addresses'
...     id = Column(Integer, primary_key=True)
...     email_address = Column(String, nullable=False)
...     user_id = Column(Integer, ForeignKey('users.id'))
...
...     user = relationship("User", back_populates="addresses")
...
...     def __repr__(self):
...         return "<Address(email_address='%s')>" % self.email_address

>>> User.addresses = relationship(
...     "Address", order_by=Address.id, back_populates="user")
```

The above class introduces the `ForeignKey` construct, which is a directive applied to `Column` that indicates that values in this column should be [constrained](https://docs.sqlalchemy.org/en/latest/glossary.html#term-constrained) to be values present in the named remote column. This is a core feature of relational databases, and is the “glue” that transforms an otherwise unconnected collection of tables to have rich overlapping relationships. The `ForeignKey` above expresses that values in the addresses.user_id column should be constrained to those values in the users.id column, i.e. its primary key.

**Note**

The `relationship.back_populates` parameter is a newer version of a very common SQLAlchemy feature called `relationship.backref`. The `relationship.backref` parameter hasn’t gone anywhere and will always remain available! The `relationship.back_populates` is the same thing, except a little more verbose and easier to manipulate. For an overview of the entire topic, see the section [Linking Relationships with Backref](https://docs.sqlalchemy.org/en/latest/orm/backref.html#relationships-backref).

The reverse side of a many-to-one relationship is always one to many. A full catalog of available `relationship()` configurations is at [Basic Relationship Patterns](https://docs.sqlalchemy.org/en/latest/orm/basic_relationships.html#relationship-patterns).

The two complementing relationships `Address.user` and `User.addresses` are referred to as a [bidirectional relationship](https://docs.sqlalchemy.org/en/latest/glossary.html#term-bidirectional-relationship), and is a key feature of the SQLAlchemy ORM. The section [Linking Relationships with Backref](https://docs.sqlalchemy.org/en/latest/orm/backref.html#relationships-backref) discusses the “backref” feature in detail.

Arguments to `relationship()` which concern the remote class can be specified using strings, assuming the Declarative system is in use. Once all mappings are complete, these strings are evaluated as Python expressions in order to produce the actual argument, in the above case the `User` class. The names which are allowed during this evaluation include, among other things, the names of all classes which have been created in terms of the declared base.

See the docstring for `relationship()` for more detail on argument style.

**Did you know?**

* a `FOREIGN KEY` constraint in most (though not all) relational databases can only link to a primary key column, or a column that has a `UNIQUE` constraint.

* a `FOREIGN KEY` constraint that refers to a multiple column primary key, and itself has multiple columns, is known as a “composite foreign key”. It can also reference a subset of those columns.

* `FOREIGN KEY` columns can automatically update themselves, in response to a change in the referenced column or row. This is known as the `CASCADE` referential action, and is a built in function of the relational database.

* `FOREIGN KEY` can refer to its own table. This is referred to as a “self-referential” foreign key.

* Read more about foreign keys at [Foreign Key - Wikipedia](http://en.wikipedia.org/wiki/Foreign_key).

We’ll need to create the `addresses` table in the database, so we will issue another CREATE from our metadata, which will skip over tables which have already been created:

```python
>>> Base.metadata.create_all(engine)
```
```sql
PRAGMA...
CREATE TABLE addresses (
	id INTEGER NOT NULL,
	email_address VARCHAR NOT NULL,
	user_id INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY(user_id) REFERENCES users (id)
)
()
COMMIT
```

## Working with Related Objects

Now when we create a `User`, a blank `addresses` collection will be present. Various collection types, such as sets and dictionaries, are possible here (see [Customizing Collection Access](https://docs.sqlalchemy.org/en/latest/orm/collections.html#custom-collections) for details), but by default, the collection is a Python list.

```python
>>> jack = User(name='jack', fullname='Jack Bean', password='gjffdd')
>>> jack.addresses
[]
```

We are free to add `Address` objects on our `User` object. In this case we just assign a full list directly:

```python
>>> jack.addresses = [
... 	Address(email_address='jack@google.com'),
... 	Address(email_address='j25@yahoo.com'),
... ]
```

When using a bidirectional relationship, elements added in one direction automatically become visible in the other direction. This behavior occurs based on attribute on-change events and is evaluated in Python, without using any SQL:

```python
>>> jack.addresses[1]
<Address(email_address='j25@yahoo.com')>

>>> jack.addresses[1].user
<User(name='jack', fullname='Jack Bean', password='gjffdd')>
```

Let’s add and commit `Jack Bean` to the database. `jack` as well as the two `Address` members in the corresponding `addresses` collection are both added to the session at once, using a process known as **cascading**:

```python
>>> session.add(jack)
>>> session.commit()
```
```sql
INSERT INTO users (name, fullname, password) VALUES (?, ?, ?)
('jack', 'Jack Bean', 'gjffdd')
INSERT INTO addresses (email_address, user_id) VALUES (?, ?)
('jack@google.com', 5)
INSERT INTO addresses (email_address, user_id) VALUES (?, ?)
('j25@yahoo.com', 5)
COMMIT
```

Querying for Jack, we get just Jack back. No SQL is yet issued for Jack’s addresses:

```python
>>> jack = session.query(User).filter_by(name='jack').one()
```
```sql
BEGIN (implicit)
SELECT users.id AS users_id,
	users.name AS users_name,
	users.fullname AS users_fullname,
	users.password AS users_password
FROM users
WHERE users.name = ?
('jack',)
```
```python
>>> jack
<User(name='jack', fullname='Jack Bean', password='gjffdd')>
```

Let’s look at the `addresses` collection. Watch the SQL:

```python
>>> jack.addresses
```
```sql
SELECT addresses.id AS addresses_id,
	addresses.email_address AS
	addresses_email_address,
	addresses.user_id AS addresses_user_id
FROM addresses
WHERE ? = addresses.user_id ORDER BY addresses.id
(5,)
```
```python
[
	<Address(email_address='jack@google.com')>, 
	<Address(email_address='j25@yahoo.com')>,
]
```
When we accessed the `addresses` collection, SQL was suddenly issued. This is an example of a [lazy loading](https://docs.sqlalchemy.org/en/latest/glossary.html#term-lazy-loading) relationship. The `addresses` collection is now loaded and behaves just like an ordinary list. We’ll cover ways to optimize the loading of this collection in a bit.

## Querying with Joins

Now that we have two tables, we can show some more features of `Query`, specifically how to create queries that deal with both tables at the same time. The [Wikipedia page on SQL JOIN](http://en.wikipedia.org/wiki/Join_%28SQL%29) offers a good introduction to join techniques, several of which we’ll illustrate here.

To construct a simple implicit join between `User` and `Address`, we can use `Query.filter()` to equate their related columns together. Below we load the `User` and `Address` entities at once using this method:

```python
>>> for u, a in session.query(User, Address).filter(User.id == Address.user_id).\
...                     filter(Address.email_address == 'jack@google.com').all():
...     print(u)
...     print(a)
```
```sql
SELECT users.id AS users_id,
	users.name AS users_name,
	users.fullname AS users_fullname,
	users.password AS users_password,
	addresses.id AS addresses_id,
	addresses.email_address AS addresses_email_address,
	addresses.user_id AS addresses_user_id
FROM users, addresses
WHERE users.id = addresses.user_id
	AND addresses.email_address = ?
('jack@google.com',)
```
```python
<User(name='jack', fullname='Jack Bean', password='gjffdd')>
<Address(email_address='jack@google.com')>
```

The actual SQL `JOIN` syntax, on the other hand, is most easily achieved using the `Query.join()` method:

```python
>>> session.query(User).join(Address).filter(Address.email_address == 'jack@google.com').all()
```
```sql
SELECT users.id AS users_id,
	users.name AS users_name,
	users.fullname AS users_fullname,
	users.password AS users_password
FROM users JOIN addresses ON users.id = addresses.user_id
WHERE addresses.email_address = ?
('jack@google.com',)
```
```python
[<User(name='jack', fullname='Jack Bean', password='gjffdd')>]
```

`Query.join()` knows how to join between `User` and `Address` because there’s only one foreign key between them. If there were no foreign keys, or several, `Query.join()` works better when one of the following forms are used:

```python
query.join(Address, User.id == Address.user_id)    # explicit condition
query.join(User.addresses)                       # specify relationship from left to right
query.join(Address, User.addresses)              # same, with explicit target
query.join('addresses')                          # same, using a string
```

As you would expect, the same idea is used for “outer” joins, using the `outerjoin()` function:

```python
query.outerjoin(User.addresses)   # LEFT OUTER JOIN
```

The reference documentation for `join()` contains detailed information and examples of the calling styles accepted by this method; `join()` is an important method at the center of usage for any SQL-fluent application.

**What does `Query` select from if there’s multiple entities?**

The `Query.join()` method will **typically join from the leftmost item** in the list of entities, when the `ON` clause is omitted, or if the `ON` clause is a plain SQL expression. To control the first entity in the list of `JOIN`s, use the `Query.select_from()` method:

```python
query = session.query(User, Address).select_from(Address).join(User)
```

### Using Aliases

When querying across multiple tables, if the same table needs to be referenced more than once, SQL typically requires that the table be _aliased_ with another name, so that it can be distinguished against other occurrences of that table. The `Query` supports this most explicitly using the `aliased` construct. Below we join to the `Address` entity twice, to locate a user who has two distinct email addresses at the same time:

```python
>>> from sqlalchemy.orm import aliased

>>> adalias1 = aliased(Address)
>>> adalias2 = aliased(Address)

>>> for username, email1, email2 in session.query(User.name, adalias1.email_address, adalias2.email_address).\
... 	join(adalias1, User.addresses).\
... 	join(adalias2, User.addresses).\
... 	filter(adalias1.email_address == 'jack@google.com').\
... 	filter(adalias2.email_address == 'j25@yahoo.com'):
... 	print(username, email1, email2)
```
```sql
SELECT users.name AS users_name,
	addresses_1.email_address AS addresses_1_email_address,
	addresses_2.email_address AS addresses_2_email_address
FROM users 
	JOIN addresses AS addresses_1
		ON users.id = addresses_1.user_id
	JOIN addresses AS addresses_2
		ON users.id = addresses_2.user_id
WHERE addresses_1.email_address = ?
	AND addresses_2.email_address = ?
('jack@google.com', 'j25@yahoo.com')
```
```python
jack jack@google.com j25@yahoo.com
```

### Using Subqueries

The `Query` is suitable for generating statements which can be used as subqueries. Suppose we wanted to load `User` objects along with a count of how many `Address` records each user has. The best way to generate SQL like this is to get the count of addresses grouped by user ids, and `JOIN` to the parent. In this case we use a `LEFT OUTER JOIN` so that we get rows back for those users who don’t have any addresses, e.g.:

```sql
SELECT users.*, adr_count.address_count 

FROM users 
	LEFT OUTER JOIN (
		SELECT user_id, 
			count(*) AS address_count
        FROM addresses 
        GROUP BY user_id
    ) AS adr_count
    	ON users.id = adr_count.user_id
```

Using the `Query`, we build a statement like this from the inside out. The `statement` accessor returns a SQL expression representing the statement generated by a particular `Query` - this is an instance of a `select()` construct, which are described in [SQL Expression Language Tutorial](https://docs.sqlalchemy.org/en/latest/core/tutorial.html):

```python
>>> from sqlalchemy.sql import func
>>> stmt = session.query(Address.user_id, func.count('*').label('address_count')).group_by(Address.user_id).subquery()
```

The `func` keyword generates SQL functions, and the `subquery()` method on `Query` produces a SQL expression construct representing a SELECT statement embedded within an alias (it’s actually shorthand for `query.statement.alias())`.

Once we have our statement, it behaves like a `Table` construct, such as the one we created for `users` at the start of this tutorial. The columns on the statement are accessible through an attribute called `c`:

```python
>>> for u, count in session.query(User, stmt.c.address_count).\
... 	outerjoin(stmt, User.id==stmt.c.user_id).order_by(User.id):
... 	print(u, count)
```
```sql
SELECT users.id AS users_id,
	users.name AS users_name,
	users.fullname AS users_fullname,
	users.password AS users_password,
	anon_1.address_count AS anon_1_address_count
FROM users 
	LEFT OUTER JOIN
		(
			SELECT addresses.user_id AS user_id,
				count(?) AS address_count
			FROM addresses 
			GROUP BY addresses.user_id
		) AS anon_1
	ON users.id = anon_1.user_id
ORDER BY users.id
('*',)
```
```python
<User(name='ed', fullname='Ed Jones', password='f8s7ccs')> None
<User(name='wendy', fullname='Wendy Williams', password='foobar')> None
<User(name='mary', fullname='Mary Contrary', password='xxg527')> None
<User(name='fred', fullname='Fred Flinstone', password='blah')> None
<User(name='jack', fullname='Jack Bean', password='gjffdd')> 2
```

