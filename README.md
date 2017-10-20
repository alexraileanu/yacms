## YaCMS

YaCMS (yet another content management system) is a small CMS I'm writing python using flask (and many other packages.
refer to the requirements.txt for the full list). I'm writing it for fun and to learn some more python. Code is far,
far from perfect (especially the frontend shenanigans) so pls bear with me.

No demo available quite yet.

I chose to have the extension for the templates as .j2 because if I had .html, PyCharm wouldn't be able to distinguish
(as far as I can tell) between an actual html file and a template file (so no syntax highlight or completions).

The admin layout was borrowed from [here](https://github.com/ConsoleTVs/UIAdmin) go check it out.

### Installation

#### Requirements

I assume you already have a mysql (or mariadb) running and also a redis instance somewhere. I prefer to have them on
different docker containers (you can have that or on your own machine, whichever) and link them to the container
running the cms. I will write installation instructions only for the first scenario.

- Fetch and run mariadb and redis. For the mariadb instance, replace `/path/to/mysql` with whatever physical location
you want to mount for the mysql data folder. (Mounting this folder is necessary if you want to preserve the data after
the container is removed. If you do not need that and also do not want phsyical access to the files, feel free to not
use the -v flag for that). I also put the mariadb instance on the host machine on port
3307 as to not have it clash with my local mysql (feel free to change to whatever port you want). Redis instance is
pretty straight forward.

```bash
    $ docker run --name mariadb -e MYSQL_ROOT_PASSWORD=root -v /path/to/mysql:/var/lib/mysql -d -p 3307:3306 mariadb:10.3.0
    $ docker run -p 6379:6379 --name redis -d redis
```

- After having those up and running (you can check with `docker ps` to see if the containers are up), build and run
the cms:

```bash
    $ docker build --tag yacms .
```

- After that's done, you will have to create a new database and username for the cms if you haven't done this already.

```bash
    $ docker exec --interactive --tty mariadb mysql -p
    MariaDB [(none)]> create database yacms;
    MariaDB [(none)]> create user 'myuser'@'%' identified by 'mypassword';
    MariaDB [(none)]> grant all privileges on yacms.* to 'myuser'@'%';
    MariaDB [(none)]> flush privileges;
    MariaDB [(none)]> exit
```

The first line allows you to enter the Docker container running mariadb. The command will ask for the password you
specified when starting the container (which is "root" if you copied the command from above).

The following lines create a database and a user with all permissions on that database. Replace "`myuser`" and
"`mypassword`" with the username and password of your choice.

- Now you can store the connection information in your configuration file.

```bash
    $ cp config/config.example.cfg config/config.cfg
```

Update the variable `SQLALCHEMY_DATABASE_URI` in `config/config.cfg` accordigly. Example:

```
    SQLALCHEMY_DATABASE_URI = 'mysql://myuser:mypassword@mariadb:3306/yacms'
```

In this case, since we're linking the yacms container to the mariadb
container, the mariadb container will be accessible via the name you
link it with (in this case just `mariadb`). This is also the reason
why we are using port 3306: this is the port inside the container that
the database is listening on.

Do the same for the redis instance:

```
    REDIS_URL = 'redis://:@redis:6379/0'
```

Same as before, the host for the redis instance can be accessed via the name you give to the link when running the yacms
container.

You also should set the `SECRET_KEY` setting to a random string.

- After that's done (it'll take a little bit of time), run the container with:

```bash
    $ docker run -p5000:5000 --name yacms -v $(pwd):/var/www/yacms -d --link mariadb:mariadb --link redis:redis yacms
```

- It will likely fail because the database won't have the correct tables, you can create the initial tables with the
following command. I also recommend seeding the database with the default user and adding the default settings
to the redis instance.

```bash
    $ docker exec -it yacms flask db upgrade
    $ docker exec -it yacms flask seed
    $ docker exec -it yacms flask prepare_redis
```

- In theory that should be everyhing and you should be able to navigate to `http://localhost:5000`.

You can log in using the username "`demo`" and password "`demo`".

#### License

[MIT](LICENSE.md), of course.
